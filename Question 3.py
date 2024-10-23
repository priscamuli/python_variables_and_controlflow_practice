#user to input a score
score=int(input("Enter your score: "))

#using a function called score_category

if score < 0 or score > 100:
    print("invalid score")
elif score >=90:
    grade='A'
elif score >=80:
    grade='B'
elif score >=70:
    grade='C'
elif score >=60:
    grade='D'
else:
    grade='F'

# Output the grade
print(f"The grade for the score {score} is: {grade}")


