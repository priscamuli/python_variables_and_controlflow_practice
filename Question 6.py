#password validator program

correct_password = "python123"
#user to enter the password
user_input = input("Enter your password: ")

#check whether the passwords are similar
if user_input == correct_password:
        print("access granted")
else:
        print("access denied")

