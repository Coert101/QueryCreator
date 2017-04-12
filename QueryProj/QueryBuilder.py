import os
from os import listdir
from os.path import isfile, join

class QueryBuilder:

    def read_file(dir, dirTo, fileName):

        newName = dirTo + "New" + fileName + ".txt"
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
                                valCount = tableName.count(' ')

                                if (valCount == 2):
                                    tableName = tableName.split(' ', 2)[2]
                                    newFile = open(newName, "a")
                                    newFile.write(line)

    def dir_builder(dirFrom, dirTo):
        for f in listdir(dirFrom) :
            QueryBuilder.read_file(dirFrom, dirTo, f)

QueryBuilder.dir_builder("Files/", "Build/")
print("Done...")