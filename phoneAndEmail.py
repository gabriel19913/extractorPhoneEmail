#! python3
# phoneAndEmail.py – Search the phone numbers and email address in the clipboard.
import pyperclip, re

# Create regex for phone number
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separator
    (\d{3}) # first 3 digits
    (\s|-|\.) # separator
    (\d{4}) # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''', re.VERBOSE)

# Create regex for email
emailRegex = re.compile(r'''(
    [a-zA-Z0-9.-_%+-]+ # user name
    @ # symbol @
    [a-zA-Z0-9.-]+ # domain name
    (\.[a-zA-Z]{2,4}) # dot followed by other characters
)''', re.VERBOSE)

# Find the phone numbers and email address in the text on the clipboard
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copies the result for the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    pyperclip.copy('\n'.join(matches))
else:
    print('No phone numbers or email address found!')
