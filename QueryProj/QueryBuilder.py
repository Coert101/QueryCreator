import os
from os import listdir

from SharedFunctionality import SharedFunctionality
from app import app
from flask import request

import time


class QueryBuilder:
    @staticmethod
    def extract_primary_keys(line):
        return line[line.index("=") + 1:].strip().split(",")

    @staticmethod
    def extract_foreign_keys(line):
        foreign_key = []
        temp = line[line.index("NAME=") + len("NAME="):]
        length = len(temp) if temp.find("#") == -1 else temp.index("#")
        foreign_key.append(temp[:length].strip())

        temp = line[line.index("REF=") + len("REF="):]
        length = len(temp) if temp.find("#") == -1 else temp.index("#")
        foreign_key.append(temp[:length].strip())

        temp = line[line.index("FK=") + len("FK="):]
        length = len(temp) if temp.find("#") == -1 else temp.index("#")
        foreign_key.append(temp[:length].strip())

        return foreign_key

    @staticmethod
    def read_file(dir_name, dirTo, file_name, db_name):

        global table_name
        file = open(dir_name + "/" + file_name, "r")
        new_name = dirTo + "/" + file_name[:-3] + ".sql"
        model_class = False
        primaryKeys = []
        foreignKeys = []
        lengthModifier = None

        if os.path.exists(new_name):
            os.remove(new_name)

        new_file = open(new_name, "a")
        new_file.write("USE [" + db_name + "]\nGO\n\nSET ANSI_NULLS ON\nGO\n\nSET QUOTED_IDENTIFIER ON\nGO\n\n")

        for line in file:

            if "//#pk" in line.lower():
                primaryKeys = QueryBuilder.extract_primary_keys(line)
            elif "//#fk" in line.lower():
                foreignKeys.append(QueryBuilder.extract_foreign_keys(line))
            elif "//#maxlength" in line.lower():
                lengthModifier = int(line[line.index("MAXLENGTH=") + len("MAXLENGTH="):].strip())
            elif SharedFunctionality.get_usable_line(line) is True:

                if "class" in line.lower():
                    model_class = True
                    table_name = line.strip()
                    table_name = SharedFunctionality.remove_parent_classes(table_name)

                    stringCount = table_name.count(' ')
                    new_file = open(new_name, "a")

                    if (stringCount == 2):
                        table_name = table_name.split(' ', 2)[2]
                    elif (stringCount > 2):
                        table_name = table_name.split(' ', 3)[3]

                    new_file.write("CREATE TABLE [dp].[" + table_name + "] (")

                type_line = next(
                    (typeName for typeName in SharedFunctionality.known_types if typeName in line.split(" ")), False)
                # ignore calculated fields. We assume that any basic property will have the closing
                # bracket on the same line we further assume that a line using arrow notation (=>) is
                # also calculating
                if "}" not in line or "=>" in line:
                    type_line = False
                if type_line is not False:
                    new_file = open(new_name, "a")
                    new_file.write("\n" + SharedFunctionality.extract_parameter_create(type_line, line, lengthModifier))
                    lengthModifier = None

        new_file.close()

        if model_class:
            new_file = open(new_name, "r")
            lines = new_file.readlines()
            top_lines = lines[:-1]
            bottom_line = (lines[len(lines) - 1:])[0]
            if "," in bottom_line:
                botStr = bottom_line[:-1]
                new_file.close()

                if os.path.exists(new_name):
                    os.remove(new_name)

                new_file = open(new_name, "a")
                new_file.writelines("%s" % item for item in top_lines)
                new_file.write(botStr)
                new_file.close()

        new_file = open(new_name, "a")

        if len(primaryKeys) > 0:
            new_file.write(", \n\tCONSTRAINT [PK_" + table_name + "] PRIMARY KEY CLUSTERED (")
            for pk in primaryKeys[:-1]:
                new_file.write("[" + pk + "] ASC, ")
            new_file.write("[" + primaryKeys[-1] + "] ASC)")

        if len(foreignKeys) > 0:
            for fk in foreignKeys:
                new_file.write(", \n\tCONSTRAINT [FK_" + fk[0] + "] FOREIGN KEY (")
                fields = fk[2].split(",")
                for item in fields[:-1]:
                    new_file.write("[" + item + "], ")
                new_file.write("[" + fields[-1] + "]) REFERENCES [dp].[" + fk[1] + "] (")
                for item in fields[:-1]:
                    new_file.write("[" + item + "], ")
                new_file.write("[" + fields[-1] + "])")

        new_file.write("\n)\n\nGO")

    @staticmethod
    def dir_builder(dir_from, dir_to, db_name):
        for f in listdir(dir_from):
            QueryBuilder.read_file(dir_from, dir_to, f, db_name)

    @staticmethod
    def get_usable_line(current_line):
        if current_line.strip() is "":
            return False

        if ('{' in current_line.lstrip()[0]) or ('}' in current_line.lstrip()[0]):
            return False

        if "[required" in current_line.lower():
            return False

        if ("using" in current_line.lower()) or ("namespace" in current_line.lower()):
            return False

        if ('#' in current_line.strip()) and ("md" in (current_line.strip()).lower()):
            return False

        return True


@app.route("/build", methods=["POST"])
def dir_builder():
    dirFrom = request.form['dirFrom']
    dirTo = request.form['dirTo']
    startTime = time.time()
    QueryBuilder.dir_builder(dirFrom, dirTo, "YamahaEOHIntegration")
    timeElapsed = time.time() - startTime
    return "<h1>Created " + str(len(listdir(dirTo))) + " scripts in " + str(timeElapsed) + "seconds </h2>"
