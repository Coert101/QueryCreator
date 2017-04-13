class SharedFunctionality:
    known_types = ["string", "int", "double", "decimal", "bool", "DateTime", "CustomerAccount", "CustomerSubaccount", "Branch", "DocumentType", "Country", "Province", "CorporationType", "AgeGroup", "Address", "EntityType", "ProductDetailType", "YesNoQuestion", "ProductClass", "OwnerDetail", "WarrantyStatus", "CustomerAccount", "CustomerSubaccount", "Branch", "DocumentType", "Country", "Province", "CorporationType", "AgeGroup", "Address", "EntityType", "ProductDetailType", "YesNoQuestion", "ProductClass", "OwnerDetail", "WarrantyStatus"]
    type_equivalent = ["VARCHAR (255)", "INT", "DECIMAL", "DECIMAL", "BIT", "DATETIME", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "BIT", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)", "BIT", "VARCHAR (255)", "VARCHAR (255)", "VARCHAR (255)"]

    @staticmethod
    def get_usable_line(current_line):
        if current_line.strip() is "":
            return False;

        if ('{' in current_line.lstrip()[0]) or ('}' in current_line.lstrip()[0]):
            return False;

        if "[required" in current_line.lower():
            return False;

        if ("using" in current_line.lower()) or ("namespace" in current_line.lower()):
            return False;

        if ('#' in current_line.strip()) and ("md" in (current_line.strip()).lower()):
            return False;

        return True;

    @staticmethod
    def remove_parent_classes(string_to_format):
        if ':' in string_to_format:
            pre_length = string_to_format.find(':') - 1
            string_to_format = string_to_format[:-(len(string_to_format) - pre_length)]
            string_to_format = string_to_format.strip()

        return string_to_format

    @staticmethod
    def extract_parameter(type_name, param_line):
        param_line = param_line.split(" ")

        param_name = "[" + param_line[param_line.index(type_name) + 1] + "]"

        return param_name

    @staticmethod
    def extract_parameter_create(type_name, param_line, length_modifier):

        param_name = SharedFunctionality.extract_parameter(type_name, param_line)
        type_name = SharedFunctionality.type_equivalent[SharedFunctionality.known_types.index(type_name)]

        if "varchar" in type_name.lower() and length_modifier is not None:
            type_name = "VARCHAR (" + str(length_modifier) + ")"

        # how do we determine whether it is nullable?
        return '\t' + param_name + ' ' + type_name + " NOT NULL,"
