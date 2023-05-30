import pickle
import json

# Task 1

users_contacts = {
    "Tom": "+380993993939",
    "Jack": "+380989989898",
    "Bob": "+380978889088",
    "Bill": "+380990990988",
}

users_ratig = {
    "Tom": "96",
    "Jack": "100",
    "Bob": "78",
    "Bill": "85",
}

with open("contacts.bin", "wb") as d:
    pickle.dump(users_contacts, d)
    pickle.dump(users_ratig, d)

# Task 2

a = {"key": 1, "key2": True}
b = {"key": "Hello"}
c = {}
identical_keys = []

for i in a.keys():
    if i in b.keys():
        identical_keys.append(a[i])
        identical_keys.append(b[i])
        b[i] = identical_keys
    identical_keys = []

c = a | b

print(c)

with open("contacts.json", "w") as j:
    json.dump(c, j)
