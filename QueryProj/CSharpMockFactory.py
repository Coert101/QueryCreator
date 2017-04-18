import os
from os import listdir
from SharedFunctionality import SharedFunctionality

class CSharpMockFactory:
    @staticmethod
    def dir_builder(dir_from, dir_to, file_to_name):

        file_to_insert_to = dir_to + file_to_name + ".cs"

        if os.path.exists(file_to_insert_to):
            os.remove(file_to_insert_to)

        new_file = open(file_to_insert_to, "a")

        # will need to consider imports here later

        for f in listdir(dir_from):
            if SharedFunctionality.check_file_enum(dir_from, f) is False:
                class_name = str(SharedFunctionality.get_class_name_from_file(dir_from, f))
                plural_maker = CSharpMockFactory.get_plural_maker(class_name)

                object_name = class_name[0].lower() + class_name[1:] + plural_maker

                new_file.write("\tprivate static IList<" + class_name + "> " + class_name[0].lower() +
                               class_name[1:] + plural_maker + ";\n")
                new_file.write("\tpublic static IList<" + class_name + "> " + class_name + plural_maker + "\n")
                new_file.write("\t{\n")
                new_file.write("\t\tget\n")
                new_file.write("\t\t{\n")
                new_file.write("\t\t\tif(" + object_name + " == null)\n")
                new_file.write("\t\t\t\t" + object_name + " = Build" + class_name + plural_maker + "();\n\n")
                new_file.write("\t\t\treturn " + object_name + ";\n")
                new_file.write("\t\t}\n")
                new_file.write("\t}\n\n\n")

        new_file.close()

        for f in listdir(dir_from):
             if SharedFunctionality.check_file_enum(dir_from, f) is False:
                class_name = str(SharedFunctionality.get_class_name_from_file(dir_from, f))
                plural_maker = CSharpMockFactory.get_plural_maker(class_name)
                object_name = class_name[0].lower() + class_name[1:] + plural_maker
                CSharpMockFactory.read_file(dir_from, f, file_to_insert_to, class_name, object_name)

    @staticmethod
    def read_file(dir_from, file_from_name, file_to_script_to, class_name, object_name):

        file = open(dir_from + file_from_name, "r")
        iteration_amount = 0

        for line_check in file:
            if iteration_amount is 0:
                iteration_amount = CSharpMockFactory.get_mock_amount(line_check)

        # This should be fixed in another manner
        if iteration_amount is 0:
            iteration_amount = 1

        new_file = open(file_to_script_to, "a")
        plural_maker = CSharpMockFactory.get_plural_maker(class_name)
        new_file.write("\tprivate void Build" + class_name + plural_maker + "()\n")
        new_file.write("\t{\n")
        new_file.write("\t\t" + object_name + " = new List<" + class_name + ">();\n")
        insert = ""

        file.seek(0)

        for x in range(0, iteration_amount):
            for line in file:
                if SharedFunctionality.get_usable_line(line) is True:
                    type_line = next(
                        (typeName for typeName in SharedFunctionality.known_types if
                         typeName in line.split(" ")),
                        False)
                    if "}" not in line or "=>" in line:
                        type_line = False
                    if type_line is not False:
                        insert = insert + SharedFunctionality.extract_parameter_for_csharp(
                            type_line, line) + " = " + \
                                        str(SharedFunctionality.generate_mock_data_for_csharp(type_line)) + ", "

            new_file.write("\t\t" + object_name + ".Add("
                           + insert[:len(insert)-2] + ");\n")

        new_file.write("\t}\n\n")
        new_file.close()

    @staticmethod
    def get_mock_amount(line_to_process):
        line = line_to_process.strip()

        if ('#' in line) and ("md" in line.lower()):
            equal_index = len(line) - (line.find('=') + 1)
            return int(line[-equal_index:])

        return 0

    @staticmethod
    def get_plural_maker(word):
        if word[len(word)-1] == 'h':
            return "es"
        elif word[len(word)-1] == 's':
            return "es"
        else:
            return "s"

CSharpMockFactory.dir_builder("Files/", "Insert/", "Test")