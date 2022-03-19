user = {
    "name": "Vinay Kanse",
    "email": "xyz@gmail.com",
    "cartItems": []
}

print(user["name"])


user["cartItems"] = [1, 2, 3, 4, 5]

print(user)

for key in user:
    print(key)

print(user.items())

for key, val in user.items():
    print(key)
    print(val)

if "name" in user:
    print("Name is available in user")

# using get method on dict
# get can be used when we are not sure about key present in dict it takes second argument as default value if no key is found
print(user.get("random", "Not Found"))
