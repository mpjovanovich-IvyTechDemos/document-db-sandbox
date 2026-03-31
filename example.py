import os
from tinydb import TinyDB, Query

FILE_NAME = "db.json"

# Remove existing file; start from scratch
if os.path.exists(FILE_NAME):
  os.remove(FILE_NAME)

# Create a database file
db = TinyDB(FILE_NAME, indent=4)

# Note: we can have a subcollection by simply using
# a list; don't need to use a related child table
users = db.table("users")
users.insert({
    'name': 'Janet Jones', 
    'roles': ['Head Cook', 'Supply Manager']
})
users.insert({
    'name': 'Bobby Beebop',
    'roles': ['Food Taster', 'Jester']
})

# Get all users
results = users.all()

# Print results
print('USERS')
print('-' * 20)
for r in results:
    print(r)
print()

# Query single user
User = Query()
results = users.search(User.name == 'Bobby Beebop')

# Print results
print('USER')
print('-' * 20)
if results:
    user = results[0]
    print(f"Name: {user['name']}")
    print(f"Roles: {user['roles']}")

# Close the document
db.close()

