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

        for f in listdir(dirFrom):
            SQLMockFactory.read_file(dirFrom, dirTo, f, insertName, dbName)

    def extract_parameter(typeName, paramLine):
        paramLine = paramLine.split(" ")

        paramName = "[" + paramLine[paramLine.index(typeName) + 1] + "]"

        typeName = SQLMockFactory.type_equivalent[SQLMockFactory.known_types.index(typeName)]

        return '\t' + paramName + ' ' + typeName + " NOT NULL,"

    def read_file(dir, dirTo, fileName, insertQueriesFile, dbName):

        #newName = dirTo + fileName[:-3] + ".sql"
        file = open(dir + fileName, "r")
        modelClass = False

        newFile = open(insertQueriesFile, "a")
      #  newFile.write("USE [" + dbName + "]\nGO\n\nSET ANSI_NULLS ON\nGO\n\nSET QUOTED_IDENTIFIER ON\nGO\n\n")

        # for line in file:
        #     if (line.strip() != ""):
        #         if (("using" not in line.lower()) and ("namespace" not in line.lower())):
        #             if (('{' not in line.lstrip()[0]) and ('}' not in line.lstrip()[0])):
        #                 if ("[required" not in line.lower()):
        #
        #                     if ("class" in line.lower()):
        #                         modelClass = True
        #                         tableName = line.strip()
        #                         tableName = SQLMockFactory.remove_parent_classes(tableName)
        #
        #                         stringCount = tableName.count(' ')
        #                         newFile = open(newName, "a")
        #
        #                         if (stringCount == 2):
        #                             tableName = tableName.split(' ', 2)[2]
        #                         elif (stringCount > 2):
        #                             tableName = tableName.split(' ', 3)[3]
        #
        #                         newFile.write("INSERT INTO [dp].[" + tableName + "] (")
        #
        #                     typeLine = next(
        #                         (typeName for typeName in SQLMockFactory.known_types if typeName in line.split(" ")),
        #                         False)
        #                     if "}" not in line or "=>" in line:
        #                         typeLine = False
        #                     if typeLine is not False:
        #                         newFile = open(newName, "a")
        #                         newFile.write("\n" + SQLMockFactory.extract_parameter(typeLine, line))
        #
        # newFile.close()
        #
        # if (modelClass == True):
        #     newFile = open(newName, "r")
        #     lines = newFile.readlines()
        #     topLines = lines[:-1]
        #     bottomLine = (lines[len(lines) - 1:])[0]
        #     if "," in bottomLine:
        #         botStr = bottomLine[:-1]
        #         newFile.close()
        #
        #         if os.path.exists(newName):
        #             os.remove(newName)
        #
        #         newFile = open(newName, "a")
        #         newFile.writelines("%s" % item for item in topLines)
        #         newFile.write(botStr)
        #         newFile.close()
        #
        # newFile = open(newName, "a")
        # newFile.write("\n)\n\nGO")

    def remove_parent_classes(stringToFormat):
        if (':' in stringToFormat):
            preLength = stringToFormat.find(':') - 1
            stringToFormat = stringToFormat[:-(len(stringToFormat) - preLength)]
            stringToFormat = stringToFormat.strip()

        return stringToFormat