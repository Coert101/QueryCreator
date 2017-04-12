import os
from os import listdir
from os.path import isfile, join

class QueryBuilder:
    known_types = ["string", "int", "double", "decimal", "bool", "DateTime"]
    type_equivalent = ["VARCHAR (255)", "INT", "DECIMAL", "DECIMAL", "BIT", "DATETIME"]



    def extract_parameter(typeName, paramLine):
        paramLine = paramLine.split(" ")

        paramName = "["+paramLine[paramLine.index(typeName)+1]+"]"

        typeName = QueryBuilder.type_equivalent[ QueryBuilder.known_types.index(typeName) ]

        # how do we determine whether it is nullable?
        return paramName + "\t\t" + typeName + "\t\tNOT NULL"

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
                                    newFile.write(tableName)

                            typeLine = next((typeName for typeName in QueryBuilder.known_types if typeName in line.split(" ")), False)
                            # ignore calculated fields. We assume that any basic property will have the closing
                            # bracket on the same line we further assume that a line using arrow notation (=>) is
                            # also calculating
                            if "}" not in line or "=>" in line:
                                typeLine = False
                            if typeLine is not False:
                                newFile = open(newName, "a")
                                newFile.write("\n"+QueryBuilder.extract_parameter(typeLine, line))


    def dir_builder(dirFrom, dirTo):
        for f in listdir(dirFrom) :
            QueryBuilder.read_file(dirFrom, dirTo, f)

QueryBuilder.dir_builder("Files/", "Build/")
print("Done...")