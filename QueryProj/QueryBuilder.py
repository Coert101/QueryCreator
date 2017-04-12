import os
from os import listdir
from os.path import isfile, join

class QueryBuilder:

    def read_file(dir, dirTo, fileName):

        newName = dirTo + "New" + fileName[:-3] + ".txt"
        file = open(dir + fileName,"r")

        if os.path.exists(newName):
            os.remove(newName)

        for line in file:
            if (line.strip() != ""):
                if (("using" not in line.lower()) and ("namespace" not in line.lower())):
                    if (('{' not in line.lstrip()[0]) and ('}' not in line.lstrip()[0])):
                        if ("[required" not in line.lower()):

                            if ("class" in line.lower()):
                                tableName = line.strip()
                                tableName = QueryBuilder.remove_parent_classes(tableName)

                                stringCount = tableName.count(' ')
                                newFile = open(newName, "a")

                                if (stringCount == 2):
                                    tableName = tableName.split(' ', 2)[2]
                                elif (stringCount > 2):
                                    tableName = tableName.split(' ', 3)[3]

                                newFile.write("[dp].[" + tableName + "]")


    def dir_builder(dirFrom, dirTo):
        for f in listdir(dirFrom) :
            QueryBuilder.read_file(dirFrom, dirTo, f)

    def remove_parent_classes(stringToFormat):
        if (':' in stringToFormat):
            preLength = stringToFormat.find(':') - 1
            stringToFormat = stringToFormat[:-(len(stringToFormat) - preLength)]
            stringToFormat = stringToFormat.strip()

        return stringToFormat

QueryBuilder.dir_builder("Files/", "Build/")
print("Done...")