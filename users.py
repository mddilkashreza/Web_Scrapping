import requests

USERS_URL = "https://dummyjson.com/users"


response = requests.get(USERS_URL)
# print(response)
result =  response.json()
# print(result)
user = result.get("users")
# print(user)
f = open("users.txt", "w")
for person in user:
    # print(f"FullName: {person.get('firstName')} {person.get('lastName')}\n")
    # # print(f"LastName: {person.get('lastName')}\n")
    # print(f"Email: {person.get('email')}\n")
    # print(f"Phone: {person.get('phone')}\n")
    # print(f"Birth_to_date: {person.get('birthdate')}\n")

    # print("\n\n")
    f.write(f"FullName: {person.get('firstName')} {person.get('lastName')}\n")
    f.write(f"Email: {person.get('email')}\n")
    f.write(f"Phone: {person.get('phone')}\n")
    f.write(f"Birth_to_Date: {person.get('birthdate')}\n")
    f.write("\n\n")
f.close()