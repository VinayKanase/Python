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
