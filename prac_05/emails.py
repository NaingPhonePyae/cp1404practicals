"""
Emails
Estimate: 15 minutes
Actual: 22 minutes
"""


def main():
    """program to create dictionary of email to name"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        name_confirm = input(f"Is your name {name}? (Y/n) ").upper()
        if name_confirm != "Y" and name_confirm != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """get name from email"""
    parts = email.split('@')[0]
    parts = parts.split('.')
    name = " ".join(parts).title()
    return name


main()
