"""
Exercice 1 — Reboot Python
Les consignes sont dans enonce.md (section EXO 1).
"""

users = [
    {"id": 1,  "name": "Alice",   "age": 25, "active": True,  "role": "admin"},
    {"id": 2,  "name": "Bob",     "age": 17, "active": False, "role": "user"},
    {"id": 3,  "name": "Charlie", "age": 32, "active": True,  "role": "user"},
    {"id": 4,  "name": "Diana",   "age": 16, "active": True,  "role": "user"},
    {"id": 5,  "name": "Evan",    "age": 42, "active": False, "role": "admin"},
    {"id": 6,  "name": "Fatima",  "age": 29, "active": True,  "role": "organizer"},
    {"id": 7,  "name": "Gael",    "age": 15, "active": True,  "role": "user"},
    {"id": 8,  "name": "Hana",    "age": 38, "active": True,  "role": "organizer"},
    {"id": 9,  "name": "Igor",    "age": 51, "active": False, "role": "user"},
    {"id": 10, "name": "Julia",   "age": 22, "active": True,  "role": "user"},
    {"id": 11, "name": "Karim",   "age": 19, "active": True,  "role": "user"},
    {"id": 12, "name": "Lena",    "age": 17, "active": True,  "role": "user"},
    {"id": 13, "name": "Marco",   "age": 45, "active": True,  "role": "admin"},
    {"id": 14, "name": "Nadia",   "age": 28, "active": False, "role": "organizer"},
    {"id": 15, "name": "Omar",    "age": 33, "active": True,  "role": "user"},
    {"id": 16, "name": "Priya",   "age": 14, "active": False, "role": "user"},
]


# ----- Partie A : les bases -----

# Q1 — Afficher le nom de chaque utilisateur.
print("---------------Q1---------------")
for user in users:
    print(user['name'])

# Q2 — Afficher uniquement les utilisateurs actifs.
print("---------------Q2---------------")
for user in users:
    if user["active"]:
        print(user)

# Q3 — Compter les utilisateurs actifs et afficher "<n> utilisateurs actifs".
print("---------------Q3---------------")

count = 0
for user in users:
    if user["active"]:
        count += 1
print(f'Il y a {count} utilisateurs actifs.')
# Q4 — Afficher uniquement les utilisateurs majeurs (18 ans ou plus).
print("---------------Q4---------------")
for user in users:
    if user ["age"]>=18:
        print(user["name"],user["age"])

# Q5 — Afficher les utilisateurs qui sont à la fois actifs ET majeurs.
print("---------------Q5---------------")
for user in users:
    if user["age"] >= 18 and user["active"]:
        print(user) 
# ----- Partie B : les fonctions -----

# Q6
def is_adult(user):
    return user["age"] >= 18

# Q7
def get_active_users( users):
    # return [u for u in users if u["active"]]
    actives = []
    for u in users :
        if u [  "active"  ] : actives.append(  u)
    return actives

# Q8
def get_active_adults(users):
    # return [u for u in users if u["active"] and is_adult(u)]
    actives = []
    for u in users:
        if u ["active"] and is_adult(u):
            actives.append(u) 
    return actives



# Q9
def find_user_by_id(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None


# ----- Partie C : le challenge -----

# Q10
def get_statistics(users):
    stats = {
        "total": len(users),
        "actives": len([user for user in users if user["active"]]),
        "inactives": len([user for user in users if not user["active"]]),
        "adults": len([user for user in users if user["age"] >= 18]),
        "minors": len([user for user in users if user["age"] < 18])
    }
    return stats


print('--------------Fonctions--------------')
