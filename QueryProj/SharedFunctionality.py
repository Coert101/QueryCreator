import os
from os import listdir
from random import randint
import random
import decimal
import time

class SharedFunctionality:
    known_types = ["string", "int", "double", "decimal", "bool", "DateTime", "CustomerAccount", "CustomerSubaccount", "Branch", "DocumentType", "Country", "Province", "CorporationType", "AgeGroup", "Address", "EntityType", "ProductDetailType", "YesNoQuestion", "ProductClass", "OwnerDetail", "WarrantyStatus", "CustomerAccount", "CustomerSubaccount", "Branch", "DocumentType", "Country", "Province", "CorporationType", "AgeGroup", "Address", "EntityType", "ProductDetailType", "YesNoQuestion", "ProductClass", "OwnerDetail", "WarrantyStatus"]
    type_equivalent = ["VARCHAR (255)", "INT", "DECIMAL", "DECIMAL", "BIT", "DATETIME", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "BIT", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "BIT", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)"]

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

    def extract_parameter_for_csharp(typeName, paramLine):
        paramLine = paramLine.split(" ")

        paramName = paramLine[paramLine.index(typeName) + 1]

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
            if " enum " in line.lower():
                return True

        return False;

    def generate_mock_data(data_type):
        typeName = SharedFunctionality.type_equivalent[SharedFunctionality.known_types.index(data_type)]
        return SharedFunctionality.data_for_type(typeName)

    def generate_mock_data_for_csharp(data_type):
        return SharedFunctionality.data_for_type_for_csharp(data_type)

    @staticmethod
    def data_for_type(type):
        return {
            "VARCHAR (255)": "N'test data'",
            "INT": randint(0,100),
            "DECIMAL": decimal.Decimal(random.randrange(10000))/100,
            "DECIMAL": decimal.Decimal(random.randrange(10000))/100,
            "BIT": False,
            "DATETIME": "GETDATE()",
        }.get(type, "test data")

        return False

    @staticmethod
    def data_for_type_for_csharp(type):
        return {
            "string": "\"test data\"",
            "int": randint(0, 100),
            "decimal": str(decimal.Decimal(random.randrange(10000)) / 100)+"M",
            "double": str(decimal.Decimal(random.randrange(10000)) / 100)+"M",
            "bool": False,
            "DateTime": "DateTime.Now",
        }.get(type, "null")

        return False

    def get_class_name_from_file(dir_name, file_name):
        file = open(dir_name + "/" + file_name, "r")

        for line in file:
            if " class " in line.lower():
                temp_line = line[line.index(" class ")+len(" class "):]
                length = temp_line.find("\n") if temp_line.find(" ") == -1 else temp_line.index(" ")
                return temp_line[:length]

        return False
