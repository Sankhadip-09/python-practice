import random 
import string
pass_len = 4
charvalues = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(pass_len):
    password += random.choice(charvalues)
print("your random passwoed is:", password)
