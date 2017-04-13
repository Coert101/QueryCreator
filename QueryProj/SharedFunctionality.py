import os
from os import listdir

class SharedFunctionality:
    known_types = ["string", "int", "double", "decimal", "bool", "DateTime"]
    type_equivalent = ["VARCHAR (255)", "INT", "DECIMAL", "DECIMAL", "BIT", "DATETIME"]

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

    def remove_parent_classes(stringToFormat):
        if (':' in stringToFormat):
            preLength = stringToFormat.find(':') - 1
            stringToFormat = stringToFormat[:-(len(stringToFormat) - preLength)]
            stringToFormat = stringToFormat.strip()

        return stringToFormat

    def extract_parameter(typeName, paramLine):
        paramLine = paramLine.split(" ")
        paramName = "[" + paramLine[paramLine.index(typeName) + 1] + "]"

        return paramName

    def extract_parameter_create(typeName, paramLine):
        #paramLine = paramLine.split(" ")
        paramName = SharedFunctionality.extract_parameter(typeName, paramLine)

        typeName = SharedFunctionality.type_equivalent[ SharedFunctionality.known_types.index(typeName) ]

        # how do we determine whether it is nullable?
        return '\t' + paramName + ' ' + typeName + " NOT NULL,"