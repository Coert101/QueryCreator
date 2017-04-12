import time
import QueryBuilder

class MasterClass:

    def create_tables_sql(dirFrom, dirTo, dbName):
        startTime = time.time()
        QueryBuilder.QueryBuilder.dir_builder(dirFrom, dirTo, dbName)
        print("Elapsed Time: " + str(time.time() - startTime) + " seconds")
        print("Done Creating Tables...")


######Perform calls for the MasterClass functions here############
MasterClass.create_tables_sql("Files/", "Build/", "YamahaEOHIntegration")

#################################################################
