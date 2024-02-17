import random
import string
import requests

def generate_word_list():
    word_list = [''.join(random.choices(string.ascii_letters + string.digits, k=16)) for _ in range(10000)]
    return word_list

def save_word_list(word_list):
    with open("word_list.txt", "w") as file:
        file.write("\n".join(word_list))

def perform_login(email, password):
    login_url = "https://www.fortnite.com/login"
    
    # Make a POST request to the login URL with the email and password
    response = requests.post(login_url, data={"email": email, "password": password})
    
    # Check if the login was successful based on the response
    if response.status_code == 200:
        return True
    else:
        return False

def enter_code(url, code):
    # Make a POST request to the code entering URL with the code
    response = requests.post(url, data={"code": code})
    
    # Check if the code entry was successful based on the response
    if response.status_code == 200:
        return True
    else:
        return False

# Generate the word list
word_list = generate_word_list()

# Save the word list to a file
save_word_list(word_list)

# Get user input for email and password
email = input("Enter your email: ")
password = input("Enter your password: ")

# Perform login and enter codes
login_url = "https://www.fortnite.com/login"
code_entering_url = "https://www.fortnite.com/vbuckscard"

# Perform login using provided email and password
login_success = perform_login(email, password)

if login_success:
    for code in word_list:
        # Attempt to enter the code on the website
        success = enter_code(code_entering_url, code)
        
        if success:
            print("Successfully entered code:", code)
            break
    else:
        print("No valid code found.")
else:
    print("Login failed. Please check your credentials.")
