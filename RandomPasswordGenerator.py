from random import randint

password = ""

for i in range(10):
    i = chr(randint(65,90))
    password = str(password) + i
print(password)

print()

# Upper and Lowercase password
password = ""

for i in range(5):
    i = chr(randint(65,90))
    for j in range(5):
        j = chr(randint(65,90)).lower()
    password = str(password) + i + j
print(password)
