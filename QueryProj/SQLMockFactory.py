import os
from os import listdir
import app as app
import time
import SharedFunctionality

class SQLMockFactory:

    def dir_builder(dirFrom, dirTo, fileName, dbName):

        insertName = dirTo + fileName + ".sql"

        if os.path.exists(insertName):
            os.remove(insertName)

        newFile = open(insertName, "a")
        newFile.write("USE [" + dbName + "]\nGO\n")
        newFile.close()

        for f in listdir(dirFrom):
            SQLMockFactory.read_file(dirFrom, dirTo, f, insertName, dbName)


    def read_file(dir, dirTo, fileName, insertQueriesFile, dbName):

        file = open(dir + fileName, "r")
        modelClass = False

        stringInsert = "INSERT" ;

        for line in file:

            if SharedFunctionality.SharedFunctionality.get_usable_line(line) is True:

                if ("class" in line.lower()):
                    modelClass = True
                    tableName = line.strip()
                    tableName = SharedFunctionality.SharedFunctionality.remove_parent_classes(tableName)

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
                    stringInsert = stringInsert + SharedFunctionality.SharedFunctionality.extract_parameter(typeLine, line) + ','

        if (modelClass == True):
            stringInsert = stringInsert[:-1]
            stringInsert = stringInsert + ") VALUES ()\nGO"

            insertFile = open(insertQueriesFile, "a")
            insertFile.write(stringInsert + '\n')

        #Go on here

SQLMockFactory.dir_builder("Files/", "Insert/", "Test", "YamahaEOHIntegration")