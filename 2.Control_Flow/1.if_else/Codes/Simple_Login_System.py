#Write a program to check login:
# Username = "admin"
# Password = "1234"
# Display:
# “Login successful” or
# “Invalid credentials”
Username = input("Enter your USERNAME: ")
Password = input("Enter your PASSWORD: ")
if (Username == "admin" and Password == "1234"):
    print("Login successful")
else:
    print("Invalid credentials")