import os

class PreAdapter:

    def reconfigure_file(fileName):

        fileConfig = open("config-files/type_config.txt")
        tempFileName = "temp.txt"

        str_known_types = "" ;
        str_type_equivalent = "" ;

        for configLine in fileConfig:
            index = len(configLine.strip()) - (configLine.strip()).find(':')
            type = (configLine.strip())[:-index]
            assocType = (configLine.strip())[-(index-1):]

            str_known_types = str_known_types + ", \"" + type + "\""
            str_type_equivalent = str_type_equivalent + ", \"" + PreAdapter.get_type(assocType) + "\""

        str_known_types = str_known_types + ']'
        str_type_equivalent = str_type_equivalent + ']'

        if os.path.exists(tempFileName):
            os.remove(tempFileName)

        file = open(fileName, "r")

        for line in file:

            if "known_types = [" in line:
                stringConfig = (line.strip())[:-1]
                stringConfig = "    " + stringConfig + str_known_types + '\n';
                line = stringConfig

            if "type_equivalent = [" in line:
                typeEqString = (line.strip())[:-1]
                typeEqString = "    " + typeEqString + str_type_equivalent + '\n';
                line = typeEqString

            file2 = open(tempFileName, "a")
            file2.write(line)

        file.close()
        file2.close()

        file2 = open(tempFileName, 'r')

        file = open(fileName, "w")

        for adaptedLines in file2:

            file.write(adaptedLines)

        file.close()
        file2.close()

        if os.path.exists(tempFileName):
            os.remove(tempFileName)

    def get_type(csCommonType):
        return {
            "string" : "VARCHAR (255)",
            "int" : "INT",
            "double" : "DECIMAL",
            "decimal" : "DECIMAL",
            "bool" : "BIT",
            "DateTime" : "DATETIME",
        }.get(csCommonType, "VARCHAR (255)")