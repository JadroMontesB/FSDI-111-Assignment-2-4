import requests


URL = "http://127.0.0.1:5000/users/"

SAMPLE_USER = {
    "first_name": "Bill",
    "last_name": "Gates",
    "hobbies": "Program",
}

def create_user():
    first_name = input("Enter a first name: ")
    last_name = input("Enter a last name: ")
    hobbies = input("Enter hobbies: ")
    SAMPLE_USER["first_name"] = first_name
    SAMPLE_USER["last_name"] = last_name
    SAMPLE_USER["hobbies"] = hobbies
    response = requests.post(URL, json=SAMPLE_USER)
    if response.status_code == 204:
        print("User created.")
    else:
        print("Error while attempting to create user.")


if __name__ == "__main__":
    print("CREATE USER")
    print("------------")
    create_user()
