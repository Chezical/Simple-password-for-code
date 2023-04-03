import time

password = "Password"
max_attempts = 3

for attempt in range(max_attempts):
    user_password = input("Enter the password: ")
    if user_password == password:
        #Put your code here.
       time.sleep(.05)
       print("YAY")
        break
    else:
        print("Incorrect password. Try again.")
else:
    print("Maximum number of attempts reached. Access denied.")
    exit()
