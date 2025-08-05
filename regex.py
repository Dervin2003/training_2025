import re

pattern = r'^[\w.-]+@[\w-]+\.[\w+.]+$'

email = "example.user123@mail-domain.co.in"

if re.match(pattern, email):
    print("Valid email ✅")
else:
    print("Invalid email ❌")


pattern = r'^[6-9]\d{9}$'

phone_number = "9876543210"

if re.match(pattern, phone_number):
    print("Valid phone number ✅")
else:
    print("Invalid phone number ❌")

