import os


class PreAdapter:
    @staticmethod
    def reconfigure_file(file_name):

        file_config = open("config-files/type_config.txt")
        temp_file_name = "temp.txt"

        str_known_types = ""
        str_type_equivalent = ""

        for config_line in file_config:
            index = len(config_line.strip()) - (config_line.strip()).find(':')
            type_name = (config_line.strip())[:-index]
            assoc_type = (config_line.strip())[-(index - 1):]

            str_known_types = str_known_types + ", \"" + type_name + "\""
            str_type_equivalent = str_type_equivalent + ", \"" + PreAdapter.get_type(assoc_type) + "\""

        str_known_types = str_known_types + ']'
        str_type_equivalent = str_type_equivalent + ']'

        if os.path.exists(temp_file_name):
            os.remove(temp_file_name)

        file = open(file_name, "r")

        for line in file:

            if "known_types = [" in line:
                string_config = (line.strip())[:-1]
                string_config = "    " + string_config + str_known_types + '\n';
                line = string_config

            if "type_equivalent = [" in line:
                type_eq_string = (line.strip())[:-1]
                type_eq_string = "    " + type_eq_string + str_type_equivalent + '\n';
                line = type_eq_string

            file2 = open(temp_file_name, "a")
            file2.write(line)

        file.close()
        file2.close()

        file2 = open(temp_file_name, 'r')

        file = open(file_name, "w")

        for adapted_lines in file2:
            file.write(adapted_lines)

        file.close()
        file2.close()

        if os.path.exists(temp_file_name):
            os.remove(temp_file_name)

    @staticmethod
    def get_type(cs_common_type):
        return {
            "string": "VARCHAR (255)",
            "int": "INT",
            "double": "DECIMAL",
            "decimal": "DECIMAL",
            "bool": "BIT",
            "DateTime": "DATETIME",
        }.get(cs_common_type, "VARCHAR (255)")
