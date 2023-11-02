import pymongo

# Replace these values with your MongoDB connection details
mongodb_uri = "mongodb://admin:password@mydb-service:27017"
database_name = "myfastapi"

try:
    # Create a MongoDB client
    client = pymongo.MongoClient(mongodb_uri)

    # Check if the database exists
    if database_name in client.list_database_names():
        print(f"Connected to the MongoDB database: {database_name}")
    else:
        print(f"Database '{database_name}' not found.")
except Exception as e:
    print(f"Error connecting to MongoDB: {str(e)}")
finally:
    # Close the MongoDB client to release resources
    client.close()

"""
echo -e "import pymongo\nmongodb_uri = 'mongodb://admin:password@mydb-service:27017'\ndatabase_name = 'myfastapi'\ntry:\n\tclient = pymongo.MongoClient(mongodb_uri)\n\tif database_name in client.list_database_names():\n\t\tprint(f'Connected to the MongoDB database: {database_name}')\n\telse:\n\t\tprint(f'Database \'{database_name}\' not found.')\nexcept Exception as e:\n\tprint(f'Error connecting to MongoDB: {str(e)}')\nfinally:\n\tclient.close()" > connect.py
"""
