import time
import QueryBuilder
import PreAdapter

class MasterClass:

    @staticmethod
    def edit_shared_functionality(file_name):
        startTime = time.time()
        PreAdapter.PreAdapter.reconfigure_file(file_name)
        print("Elapsed Time: " + str(time.time() - startTime) + " seconds")
        print("Done Creating Tables...")

    def create_tables_sql(dirFrom, dirTo, dbName):
        startTime = time.time()
        QueryBuilder.QueryBuilder.dir_builder(dirFrom, dirTo, dbName)
        print("Elapsed Time: " + str(time.time() - startTime) + " seconds")
        print("Done Creating Tables...")


######Perform calls for the MasterClass functions here############
MasterClass.edit_shared_functionality("SharedFunctionality.py")
MasterClass.create_tables_sql("Files/", "Build/", "YamahaEOHIntegration")
#################################################################
