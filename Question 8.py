#getting day of week by input a number

def get_day_of_week(number):
    days = {
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday",
        7:"Sunday"
    }
    return days.get(number, "invalid input.")
#the user input
user_input = int(input("Enter a number (1 to 7): "))
day = get_day_of_week(user_input)
print(day)