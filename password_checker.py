password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_chars = "@#!$%&*"

for char in password:
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if char.isdigit():
         has_digit = True
    if char in special_chars:
         has_special = True

if len(password) < 8:
    print("Password is weak")
    print("Password must be at least 8 characters long")

elif not has_upper:
    print("Password is weak")
    print("Password must be at least 1 one uppercase")

elif not has_lower:
    print("Password is weak")
    print("Password must be at least 1 lower case")

elif not has_digit:
     print("Password is weak")
     print("password must contain at least one number")
elif not has_special:
    print("Password is weak ❌")
    print("Reason: Password must contain at least one special character (@#$%!&*)")
else:
        print("Password has passed security checks ✅")




