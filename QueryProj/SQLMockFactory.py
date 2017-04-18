import os
from os import listdir
from SharedFunctionality import SharedFunctionality


class SQLMockFactory:
    @staticmethod
    def dir_builder(dir_from, dir_to, file_to_name, db_name):

        file_to_insert_to = dir_to + file_to_name + ".sql"

        if os.path.exists(file_to_insert_to):
            os.remove(file_to_insert_to)

        new_file = open(file_to_insert_to, "a")
        new_file.write("USE [" + db_name + "]\nGO\n")
        new_file.close()

        for f in listdir(dir_from):
            if SharedFunctionality.check_file_enum(dir_from, f) is False:
                SQLMockFactory.read_file(dir_from, f, file_to_insert_to)

    @staticmethod
    def read_file(dir_from, file_from_name, file_to_script_to):

        file = open(dir_from + file_from_name, "r")
        iteration_amount = 0

        for line_check in file:
            if iteration_amount is 0:
                iteration_amount = SQLMockFactory.get_mock_amount(line_check)

        # This should be fixed in another manner
        if iteration_amount is 0:
            iteration_amount = 1

        for x in range(0, iteration_amount):

            file.close()
            file = open(dir_from + file_from_name, "r")
            model_class = False
            string_insert = "INSERT"

            for line in file:

                if SharedFunctionality.get_usable_line(line) is True:

                    if "class" in line.lower():
                        model_class = True
                        table_name = line.strip()
                        table_name = SharedFunctionality.remove_parent_classes(table_name)

                        string_count = table_name.count(' ')

                        if string_count == 2:
                            table_name = table_name.split(' ', 2)[2]
                        elif string_count > 2:
                            table_name = table_name.split(' ', 3)[3]

                        string_insert = string_insert + " [dp].[" + table_name + "] ("

                    type_line = next(
                        (typeName for typeName in SharedFunctionality.known_types if
                         typeName in line.split(" ")),
                        False)
                    if "}" not in line or "=>" in line:
                        type_line = False
                    if type_line is not False:
                        string_insert = string_insert + SharedFunctionality.extract_parameter(
                            type_line, line) + ','

            if model_class:
                string_insert = string_insert[:-1]
                string_insert = string_insert + ") VALUES ()\nGO"

                insert_file = open(file_to_script_to, "a")
                insert_file.write(string_insert + '\n')

            # Go on here

            file.close()

    @staticmethod
    def get_mock_amount(line_to_process):
        line = line_to_process.strip()

        if ('#' in line) and ("md" in line.lower()):
            equal_index = len(line) - (line.find('=') + 1)
            return int(line[-equal_index:])

        return 0


SQLMockFactory.dir_builder("Files/", "Insert/", "Test", "YamahaEOHIntegration")
