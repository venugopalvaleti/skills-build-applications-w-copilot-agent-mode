from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Initialize the database
db = client["octofit_db"]

# Create collections
collections = ["users", "teams", "activity", "leaderboard", "workouts"]
# Update the collection creation to remove invalid parameters
for collection in collections:
    db.create_collection(collection)

# Ensure unique index for the users collection
db["users"].create_index("email", unique=True)

# List and print all collections in the database
collections = db.list_collection_names()
print("Collections in octofit_db:", collections)

print("Database and collections initialized successfully.")
