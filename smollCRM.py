# smollCRM V0.2 — save client as Markdown note

print("\n==============================")
print("      Sile's SmollCRM")
print("==============================\n")

name = input("Client name: ")
phone = input("Phone number: ")
email = input("Email: ")
niche = input("Niche: ")
last_contact = input("Last contact date: ")

filename = name.replace(" ", "_") + ".md"

content = f"""
# Client: {name}

## Contact Information
- **Phone:** {phone}
- **Email:** {email}

## Business
- **Niche:** {niche}

## Last Contact
- {last_contact}

## Notes
-
"""

with open(filename, "w", encoding="utf-8") as file:
    file.write(content)

print(f"\nMarkdown file '{filename}' created successfully.")