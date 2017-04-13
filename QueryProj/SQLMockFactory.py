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
        iterationAmount = 0

        for lineCheck in file:
            if iterationAmount is 0:
                iterationAmount = SQLMockFactory.get_mock_amount(lineCheck)

        ####This should be fixed in another manner########################
        if iterationAmount is 0:
            iterationAmount = 1
        ##################################################################

        for x in range (0,iterationAmount):

            file.close()
            file = open(dir + fileName, "r")
            modelClass = False
            stringInsert = "INSERT"

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
                        (typeName for typeName in SharedFunctionality.SharedFunctionality.known_types if typeName in line.split(" ")),
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

            file.close()

    def get_mock_amount(lineToProcess):
        line = lineToProcess.strip()

        if ('#' in line) and ("md" in line.lower()):

            equalIndex = len(line) - ((line).find('=') + 1)
            return int((line)[-equalIndex:])

        return 0

SQLMockFactory.dir_builder("Files/", "Insert/", "Test", "YamahaEOHIntegration")