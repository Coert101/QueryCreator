import os
from os import listdir
import SharedFunctionality
from app import app
from flask import request

import time


class QueryBuilder:

    def read_file(dir, dirTo, fileName, dbName):

        newName = dirTo + "/New" + fileName[:-3] + ".txt"
        file = open(dir +"/"+ fileName,"r")
        newName = dirTo + "/" + fileName[:-3] + ".sql"
        modelClass = False

        if os.path.exists(newName):
            os.remove(newName)

        newFile = open(newName, "a")
        newFile.write("USE [" + dbName + "]\nGO\n\nSET ANSI_NULLS ON\nGO\n\nSET QUOTED_IDENTIFIER ON\nGO\n\n")

        for line in file:

            if SharedFunctionality.SharedFunctionality.get_usable_line(line) is True:

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
        newFile.write("\n)\n\nGO")


    def dir_builder(dirFrom, dirTo, dbName):
        for f in listdir(dirFrom) :
            QueryBuilder.read_file(dirFrom, dirTo, f, dbName)

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