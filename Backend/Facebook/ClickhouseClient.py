from clickhouse_driver import Client

class ClickhouseClient:

    def __init__(self, ipAddress):
        self.ipAddress = ipAddress

    # Queries for databases
    def createDatabase(self,dbName):
        # Create database in clickhouse server
        client = Client(self.ipAddress)
        query = "CREATE DATABASE {}".format(dbName)
        client.execute(query)
        print("Database is created successfully")

    def showDatabases(self):
        # Return databases in clickhouse server
        client = Client(self.ipAddress)
        query = "SHOW DATABASES;"
        return client.execute(query)

    def dropDatabase(self,dbName):
        # Drop the database
        client = Client(self.ipAddress)
        query = "DROP DATABASE IF EXISTS {};".format(dbName)
        client.execute(query)
        print("Database is dropped successfully")

    # Queries for tables
    def showTables(self,dbName):
        # Return tables in specific database
        client = Client(self.ipAddress)
        query = 'SHOW TABLES FROM {};'.format(dbName)
        return client.execute(query)

    def createTable(self,dbName,tableName):
        # Create a new table in clickhouse server
        client = Client(self.ipAddress)
        # Drop the table if table name already exists
        self.dropTable(dbName,tableName)
        # Create the table
        query = 'CREATE TABLE {}.{} (date Date DEFAULT today(), date_time String, user_id UInt64, user_name String, text_id String, text String, score Float32, magnitude Float32) ENGINE = MergeTree(date, (date), 8192);'.format(dbName,tableName)
        client.execute(query)
        print("Table is created successfully")

    def insertData(self,dbName,tableName,listOfDictionaries):
        # Inserting the data into the table
        client = Client(self.ipAddress)
        query = 'INSERT INTO {}.{} (date_time,user_id,user_name,text_id,text,score,magnitude) VALUES'.format(dbName,tableName)
        client.execute(query,listOfDictionaries)
        print('Record is added successfully')

    def selectData(self,dbName,tableName):
        # Retrive table data
        client = Client(self.ipAddress)
        query = 'SELECT * FROM {}.{};'.format(dbName,tableName)
        return client.execute(query)

    def dropTable(self,dbName,tableName):
        # Drop the table
        client = Client(self.ipAddress)
        query = 'DROP TABLE IF EXISTS {}.{};'.format(dbName,tableName)
        client.execute(query)
        print("Table is dropped successfully")

    def addColumn(self,dbName,tableName,columnName,dataType):
        # Add column to existing table
        client = Client(self.ipAddress)
        query = 'ALTER TABLE {}.{} ADD {} {};'.format(dbName,tableName,columnName,dataType)
        client.execute(query)
        print("Table column is added successfully")

    # Additional Functions
    def dropAllTables(self,dbName):
        # Drop all all tables from database
        client = Client(self.ipAddress)
        # Drop current database
        self.dropDatabase(dbName)
        # Create a new database
        self.createDatabase(dbName)

    
#obj = ClickhouseClient("10.0.0.30")

#obj.createTable("twitter","test")

#obj.insertData('twitter','test','Fri Sep 06 07:40:45 +0000 2019','1151806655744450123','dexter','1169878084759089152','@wavenlp damn it')

#print(obj.selectData("twitter","test"))


