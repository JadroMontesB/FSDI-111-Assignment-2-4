import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/users/"

SAMPLE_USER = {
    "first_name": "Bill",
    "last_name": "Gates",
    "hobbies": "Program"
}

def update_user(user_id):
    SAMPLE_USER["first_name"] = input("Enter a first name: ")
    SAMPLE_USER["last_name"] = input("Enter a last name: ")
    SAMPLE_USER["hobbies"] = input("Enter hobbies: ")
    url = "%s%s" % (URL, user_id)
    response = requests.put(url, json=SAMPLE_USER)
    if response.status_code == 204:
        print("User updated.")
    else:
        print("Error while trying to update user.")


def get_user():
    user_id = input("Type in the desired user id: ")
    url = "%s%s" % (URL, user_id)
    response = requests.get(url)
    user = {}
    if response.status_code == 200:
        response_json = response.json()
        user = response_json["user"][0]
        print("User: ")
        pprint(user)
    else:
        print("Error while trying to retrieve user.")
    return user.get("id")


if __name__ == "__main__":
    print("UPDATE USER")
    print("-------------")
    user_id = get_user()
    update_user(user_id)
