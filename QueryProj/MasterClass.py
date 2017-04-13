import time
from QueryBuilder import QueryBuilder
from PreAdapter import PreAdapter

class MasterClass:

    @staticmethod
    def edit_shared_functionality(file_name):
        startTime = time.time()
        PreAdapter.reconfigure_file(file_name)
        print("Elapsed Time: " + str(time.time() - startTime) + " seconds")
        print("Done Creating Tables...")

    @staticmethod
    def create_tables_sql(dir_from, dir_to, dbName):
        start_time = time.time()
        QueryBuilder.dir_builder(dir_from, dir_to, dbName)
        print("Elapsed Time: " + str(time.time() - start_time) + " seconds")
        print("Done Creating Tables...")


######Perform calls for the MasterClass functions here############
MasterClass.edit_shared_functionality("SharedFunctionality.py")
MasterClass.create_tables_sql("Files/", "Build/", "YamahaEOHIntegration")
#################################################################
