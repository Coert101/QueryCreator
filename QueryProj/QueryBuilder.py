import os
from os import listdir

import SharedFunctionality
from app import app
from flask import request


import time


class QueryBuilder:

    def extract_primary_keys(line):
        return line[line.index("=")+1:].strip().split(",")

    def extract_foreign_keys(line):
        foreignKey = []
        temp = line[line.index("NAME=")+len("NAME="):]
        length = len(temp) if temp.find("#") == -1 else temp.index("#")
        foreignKey.append(temp[:length].strip())

        temp = line[line.index("REF=")+len("REF="):]
        length = len(temp) if temp.find("#") == -1 else temp.index("#")
        foreignKey.append(temp[:length].strip())

        temp = line[line.index("FK=")+len("FK="):]
        length = len(temp) if temp.find("#") == -1 else temp.index("#")
        foreignKey.append(temp[:length].strip())

        return foreignKey


    def read_file(dir, dirTo, fileName, dbName):

        newName = dirTo + "/New" + fileName[:-3] + ".txt"
        file = open(dir +"/"+ fileName,"r")
        newName = dirTo + "/" + fileName[:-3] + ".sql"
        modelClass = False
        primaryKeys = []
        foreignKeys = []

        if os.path.exists(newName):
            os.remove(newName)

        newFile = open(newName, "a")
        newFile.write("USE [" + dbName + "]\nGO\n\nSET ANSI_NULLS ON\nGO\n\nSET QUOTED_IDENTIFIER ON\nGO\n\n")

        for line in file:

            if "//#pk" in line.lower():
                primaryKeys = QueryBuilder.extract_primary_keys(line)
            elif "//#fk" in line.lower():
                foreignKeys.append(QueryBuilder.extract_foreign_keys(line))
            elif SharedFunctionality.SharedFunctionality.get_usable_line(line) is True:

                if ("class" in line.lower()):
                    modelClass = True
                    tableName = line.strip()
                    tableName = SharedFunctionality.SharedFunctionality.remove_parent_classes(tableName)

                    stringCount = tableName.count(' ')
                    newFile = open(newName, "a")

                    if (stringCount == 2):
                        tableName = tableName.split(' ', 2)[2]
                    elif (stringCount > 2):
                        tableName = tableName.split(' ', 3)[3]

                    newFile.write("CREATE TABLE [dp].[" + tableName + "] (")


                typeLine = next((typeName for typeName in SharedFunctionality.SharedFunctionality.known_types if typeName in line.split(" ")), False)
                # ignore calculated fields. We assume that any basic property will have the closing
                # bracket on the same line we further assume that a line using arrow notation (=>) is
                # also calculating
                if "}" not in line or "=>" in line:
                    typeLine = False
                if typeLine is not False:
                    newFile = open(newName, "a")
                    newFile.write("\n"+SharedFunctionality.SharedFunctionality.extract_parameter_create(typeLine, line))

        newFile.close()

        if (modelClass == True):
            newFile = open(newName, "r")
            lines = newFile.readlines()
            topLines = lines[:-1]
            bottomLine = (lines[len(lines)-1:])[0]
            if "," in bottomLine:
                botStr = bottomLine[:-1]
                newFile.close()

                if os.path.exists(newName):
                    os.remove(newName)

                newFile = open(newName, "a")
                newFile.writelines("%s" % item for item in topLines)
                newFile.write(botStr)
                newFile.close()

        newFile = open(newName, "a")

        if len(primaryKeys) > 0:
            newFile.write(", \n\tCONSTRAINT [PK_"+tableName+"] PRIMARY KEY CLUSTERED (")
            for pk in primaryKeys[:-1]:
                newFile.write("["+pk+"] ASC, ")
            newFile.write("["+primaryKeys[-1]+"] ASC)")

        if len(foreignKeys) > 0:
            for fk in foreignKeys:
                newFile.write(", \n\tCONSTRAINT [FK_"+fk[0]+"] FOREIGN KEY (")
                fields = fk[2].split(",")
                for item in fields[:-1]:
                    newFile.write("[" + item + "], ")
                newFile.write("[" + fields[-1] + "]) REFERENCES [dp].[" + fk[1] + "] (")
                for item in fields[:-1]:
                    newFile.write("[" + item + "], ")
                newFile.write("[" + fields[-1] + "])")

        newFile.write("\n)\n\nGO")


    def dir_builder(dirFrom, dirTo, dbName):
        for f in listdir(dirFrom) :
            QueryBuilder.read_file(dirFrom, dirTo, f, dbName)


    def get_usable_line(currentLine):
        if ((currentLine.strip() is "")):
            return False;

        if (('{' in currentLine.lstrip()[0]) or ('}' in currentLine.lstrip()[0])):
            return False;

        if ("[required" in currentLine.lower()):
            return False;

        if (("using" in currentLine.lower()) or ("namespace" in currentLine.lower())):
            return False;

        if ('#' in currentLine.strip()) and ("md" in (currentLine.strip()).lower()):
            return False;

        return True;


    @app.route("/stop/<test>")
    def test(test):
        return "<h1>Button clicked</h1>"


@app.route("/build", methods=["POST"])
def dir_builder():
    dirFrom = request.form['dirFrom']
    dirTo = request.form['dirTo']
    startTime = time.time()
    QueryBuilder.dir_builder(dirFrom, dirTo, "YamahaEOHIntegration")
    timeElapsed = time.time() - startTime
    return "<h1>Created " + str(len(listdir(dirTo))) + " scripts in " + str(timeElapsed) + "seconds </h2>"