import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydb"]
mycol = mydb["users"]

mycol.create_index("username", unique=True)
mycol.create_index("age")
mycol.create_index("city")

def insert_user(username,age,city):
    user = {
        'username': username,
        'age': age,
        'city': city
    }

    try:
        result = mycol.insert_one(user)
        print("User inserted with ID:", result.inserted_id)
    except pymongo.errors.DuplicateKeyError:
        print("Username must be unique. Document not inserted.")
    except pymongo.errors.WriteError as e:
        print("Error:", e)

def userInfo(username):
    user = mycol.find_one({"username": username})
    if user:
        print("User found:")
        print(user)
    else:
        print("User not found.")

def changeAge(username,new_age):
    result = mycol.update_one({"username": username}, {"$set": {"age": new_age}})
    if result.modified_count > 0:
        print("User's age updated successfully.")
    else:
        print("User not found or age unchanged.")

def changeCity(username,new_city):
    result = mycol.update_one({"username": username}, {"$set": {"city": new_city}})

    if result.modified_count > 0:
        print("User's city updated successfully.")
    else:
        print("User not found or city unchanged.")


def deleteUser(username):
    result = mycol.delete_one({"username": username})

    if result.deleted_count > 0:
        print("User deleted successfully.")
    else:
        print("User not found.")