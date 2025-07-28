# משימת תכנות - בודק חוזק סיסמאות
def password_quality_check(users_password):
    count_of_points = 0
    password_length= len(users_password)
    #creating the list of incorrect substrings
    incorrect_substring=["123456", "admin"]

    if password_length < 8 :
        count_of_points=0
    if (password_length >= 8) and (password_length <= 11):
        count_of_points+=1
    if password_length >= 12:
        count_of_points+=2

    for char in users_password:
        if char.isupper() :
            count_of_points+=1
        if char.islower():
            count_of_points += 1
        if char.isdigit():
            count_of_points += 1
        if char.isalnum():
            count_of_points += 1

    # check if correct password(list) has incorrect substr
    for x in incorrect_substring:
        if x.lower() in users_password.lower():
            count_of_points-=2

    # last step: checking if your password is strong or weak
    if count_of_points <= 0:
        print("your password is too weak, please try again with new one!")

    if (count_of_points >=1) and (count_of_points <=3):
        print("your password normal, but if you want to have better protection of your data"
              "than change you password for the better one)")

    if count_of_points >=4:
        print("your password is strong!")

password = "1"
print(password_quality_check(password))