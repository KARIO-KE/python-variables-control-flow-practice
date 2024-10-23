age = int(input("Enter age: "))
if age < 18:
    category = "minor"
elif 18 <= age <= 65:
    category = "adult"
else:
    category = "Senior"
print(f"Classified as a {category}.")
