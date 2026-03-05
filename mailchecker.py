email = input("Enter an email address: ")

if "@" in email and "." in email and email.count("@") == 1:
    username, domain = email.split("@")
    if username.strip() and domain.strip() and "." in domain:
        print("Valid email address.")
    else:
        print("Invalid email address.")       
else:
    print("Invalid email address.")
    
