email = input("Enter email address: ")

email = email.strip().lower()

# Find @ posititon
at_position = email.find("@")

username = email[0:at_position]
print(username)

domain = email[at_position + 1:]
print(domain)

print("Contains one @:", email.count("@") == 1)

print("Ends with .com or .co.za:", (email.endswith((".com", ".co.za"))))