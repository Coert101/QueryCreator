import os
from os import listdir
import app as app
import time
from flask import Flask
app = Flask(__name__)

class QueryBuilder:
    known_types = ["string", "int", "double", "decimal", "bool", "DateTime"]
    type_equivalent = ["VARCHAR (255)", "INT", "DECIMAL", "DECIMAL", "BIT", "DATETIME"]


    def extract_parameter(typeName, paramLine):
        paramLine = paramLine.split(" ")

        paramName = "["+paramLine[paramLine.index(typeName)+1]+"]"

        typeName = QueryBuilder.type_equivalent[ QueryBuilder.known_types.index(typeName) ]

        # how do we determine whether it is nullable?
        return '\t' + paramName + ' ' + typeName + " NOT NULL,"

    def read_file(dir, dirTo, fileName, dbName):

        newName = dirTo + fileName[:-3] + ".sql"
        file = open(dir + fileName,"r")
        modelClass = False

        if os.path.exists(newName):
            os.remove(newName)

        newFile = open(newName, "a")
        newFile.write("USE [" + dbName + "]\nGO\n\nSET ANSI_NULLS ON\nGO\n\nSET QUOTED_IDENTIFIER ON\nGO\n\n")

        for line in file:
            if (line.strip() != ""):
                if (("using" not in line.lower()) and ("namespace" not in line.lower())):
                    if (('{' not in line.lstrip()[0]) and ('}' not in line.lstrip()[0])):
                        if ("[required" not in line.lower()):

                            if ("class" in line.lower()):
                                modelClass = True
                                tableName = line.strip()
                                tableName = QueryBuilder.remove_parent_classes(tableName)

                                stringCount = tableName.count(' ')
                                newFile = open(newName, "a")

                                if (stringCount == 2):
                                    tableName = tableName.split(' ', 2)[2]
                                elif (stringCount > 2):
                                    tableName = tableName.split(' ', 3)[3]

                                newFile.write("CREATE TABLE [dp].[" + tableName + "] (")


                            typeLine = next((typeName for typeName in QueryBuilder.known_types if typeName in line.split(" ")), False)
                            # ignore calculated fields. We assume that any basic property will have the closing
                            # bracket on the same line we further assume that a line using arrow notation (=>) is
                            # also calculating
                            if "}" not in line or "=>" in line:
                                typeLine = False
                            if typeLine is not False:
                                newFile = open(newName, "a")
                                newFile.write("\n"+QueryBuilder.extract_parameter(typeLine, line))

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

    def remove_parent_classes(stringToFormat):
        if (':' in stringToFormat):
            preLength = stringToFormat.find(':') - 1
            stringToFormat = stringToFormat[:-(len(stringToFormat) - preLength)]
            stringToFormat = stringToFormat.strip()

        return stringToFormat

startTime = time.time()
QueryBuilder.dir_builder("Files/", "Build/", "YamahaEOHIntegration")
print("Elapsed Time: " + str(time.time() - startTime) + " seconds")
print("Done...")