import re

doc = input("DOC (DD/MM/YY): ")

p = "From riding bikes i enjoy speed and freedom"

pattern = "bike"

# match (checking if string starts with "From")
r = re.match("From", p)
if r:
    print("valid start")
else:
    print("invalid start")

# search
r = re.search("bike", p)
if r:
    print("phrase valid case 1")
else:
    print("phrase invalid")

# findall
r = re.findall(pattern, p)
if r:
    print("phrase valid case 2")
else:
    print("invalid phrase")

# replace
v = re.sub("bike", "car", p)
print(v)

# extract numbers from doc
r = re.findall("[0-9]+", doc)
print(r)

# date validation
pattern = r"\d{2}/\d{2}/\d{2}$"
v = re.match(pattern, doc)

if v:
    print("valid DOC")
else:
    print("invalid DOC")