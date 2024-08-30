import re
text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(emails)
#2. Python Regular Expressions Deep Dive
#Task 1: Email Extraction Enhancement
import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print("First in this app we will print all the emails in the list then we will use regex to print the filtered emailes. ")
print(emails)
filtered_emails = []
for email in emails:
    if not re.match("[A-Za-z0-9._%+-]+@exclude\.com", email):
        filtered_emails.append(email)

print("we will now print all the filtered emailes")
print(filtered_emails)
