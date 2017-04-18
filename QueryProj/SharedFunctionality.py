import os
from os import listdir

class SharedFunctionality:
    known_types = ["string", "int", "double", "decimal", "bool", "DateTime", "CustomerAccount", "CustomerSubaccount", "Branch", "DocumentType", "Country", "Province", "CorporationType", "AgeGroup", "Address", "EntityType", "ProductDetailType", "YesNoQuestion", "ProductClass", "OwnerDetail", "WarrantyStatus", "CustomerAccount", "CustomerSubaccount", "Branch", "DocumentType", "Country", "Province", "CorporationType", "AgeGroup", "Address", "EntityType", "ProductDetailType", "YesNoQuestion", "ProductClass", "OwnerDetail", "WarrantyStatus", "CustomerAccount", "CustomerSubaccount", "Branch", "DocumentType", "Country", "Province", "CorporationType", "AgeGroup", "Address", "EntityType", "ProductDetailType", "YesNoQuestion", "ProductClass", "OwnerDetail", "WarrantyStatus"]
    type_equivalent = ["VARCHAR (255)", "INT", "DECIMAL", "DECIMAL", "BIT", "DATETIME", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "BIT", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "BIT", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "BIT", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)"]

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

    def extract_parameter_create(typeName, paramLine, lengthModifier):

        paramName = SharedFunctionality.extract_parameter(typeName, paramLine)
        typeName = SharedFunctionality.type_equivalent[ SharedFunctionality.known_types.index(typeName) ]

        if "varchar" in typeName.lower() and lengthModifier is not None:
            typeName = "VARCHAR (" + str(lengthModifier) + ")"

        return '\t' + paramName + ' ' + typeName + " NOT NULL,"

    def check_file_enum(dir_name, file_name):
        file = open(dir_name + "/" + file_name, "r")

        for line in file:
            if "enum" in line.strip().lower():
                return True

        return False;


#SharedFunctionality.check_file_enum("Files/","WarrantyStatus.cs")
#SharedFunctionality.check_file_enum("Files/","AccountCheque.cs")