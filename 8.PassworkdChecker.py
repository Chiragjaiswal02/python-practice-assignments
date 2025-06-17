#ask user to input a password. Check fi the password meets the criteria.
#  Criteria for Password            
# At least 8 characters
# Contains at least one uppercase letter
# Contains at least one lowercase letter
# Contains at least one digit
# Contains at least one special character

def password_checker(password):
    upper_flag = False
    lower_flag = False
    digit_flag = False
    specialChar_flag = False
    special_characters = "!@#$%^&*(),.?\":{}|<>"
    if len(password) < 8:
        return "Password Must be 8 characters long"

    for char in password:
        if char.isupper():
            upper_flag = True
        elif char.islower():
            lower_flag = True
        elif char.isdigit():
            digit_flag = True
        elif char in special_characters:
            specialChar_flag  = True

    if not upper_flag:
        return False, "Password must contain at least one uppercase letter."
    if not lower_flag:
        return False, "Password must contain at least one lowercase letter."
    if not digit_flag:
        return False, "Password must contain at least one digit."
    if not specialChar_flag:
        return False, "Password must contain at least one special character."  

    return True, "Password is Correct"


user_password = input("Enter Password: ")
print(password_checker(user_password))