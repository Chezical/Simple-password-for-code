password = "mypassword"
max_attempts = 3

for attempt in range(max_attempts):
    user_password = input("Enter the password: ")
    if user_password == password:
        print("Access granted.")
        # add your code here
        break
    else:
        print("Incorrect password. Try again.")
else:
    print("Maximum number of attempts reached. Access denied.")
    exit()
