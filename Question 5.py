#age checker
def age_checker(age):
    if age < 18:
        print("minor")
    elif 18<=age<=65:
        print("adult")
    else:
        print("senior")

age=int(input("Enter your age:"))

age_checker(age)