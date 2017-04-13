import os
from os import listdir
import app as app
import time

class SQLMockFactory:
    known_types = ["string", "int", "double", "decimal", "bool", "DateTime"]
    type_equivalent = ["VARCHAR (255)", "INT", "DECIMAL", "DECIMAL", "BIT", "DATETIME"]

    def dir_builder(dirFrom, dirTo, fileName, dbName):

        insertName = dirTo + fileName + ".sql"

        if os.path.exists(insertName):
            os.remove(insertName)

        newFile = open(insertName, "a")
        newFile.write("USE [" + dbName + "]\nGO\n")
        newFile.close()

        for f in listdir(dirFrom):
            SQLMockFactory.read_file(dirFrom, dirTo, f, insertName, dbName)

    def extract_parameter(typeName, paramLine):
        paramLine = paramLine.split(" ")
        paramName = "[" + paramLine[paramLine.index(typeName) + 1] + "]"

        return paramName

    def read_file(dir, dirTo, fileName, insertQueriesFile, dbName):

        file = open(dir + fileName, "r")
        modelClass = False

        stringInsert = "INSERT" ;

        for line in file:
            if (line.strip() != ""):
                if (("using" not in line.lower()) and ("namespace" not in line.lower())):
                    if (('{' not in line.lstrip()[0]) and ('}' not in line.lstrip()[0])):
                        if ("[required" not in line.lower()):

                            if ("class" in line.lower()):
                                modelClass = True
                                tableName = line.strip()
                                tableName = SQLMockFactory.remove_parent_classes(tableName)

                                stringCount = tableName.count(' ')

                                if (stringCount == 2):
                                    tableName = tableName.split(' ', 2)[2]
                                elif (stringCount > 2):
                                    tableName = tableName.split(' ', 3)[3]

                                stringInsert = stringInsert + " [dp].[" + tableName + "] ("

                            typeLine = next(
                                (typeName for typeName in SQLMockFactory.known_types if typeName in line.split(" ")),
                                False)
                            if "}" not in line or "=>" in line:
                                typeLine = False
                            if typeLine is not False:
                                stringInsert = stringInsert + SQLMockFactory.extract_parameter(typeLine, line) + ','

        if (modelClass == True):
            stringInsert = stringInsert[:-1]
            stringInsert = stringInsert + ") VALUES ()\nGO"

            insertFile = open(insertQueriesFile, "a")
            insertFile.write(stringInsert + '\n')

        #Go on here

    def remove_parent_classes(stringToFormat):
        if (':' in stringToFormat):
            preLength = stringToFormat.find(':') - 1
            stringToFormat = stringToFormat[:-(len(stringToFormat) - preLength)]
            stringToFormat = stringToFormat.strip()

        return stringToFormat

SQLMockFactory.dir_builder("Files/", "Insert/", "Test", "YamahaEOHIntegration")