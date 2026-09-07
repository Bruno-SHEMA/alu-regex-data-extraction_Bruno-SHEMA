import re # REGEX library
from pathlib import Path # Library to help access file in a certain path
file = Path(__file__).parent.parent / "input" / "raw-text.txt"  # Access the 'raw-text.txt' file from the 'input' directory, and asign its content to the 'file' variable

# We will use 're.compile' to create a reusable regex pattern
regular_mail_pattern = re.compile(r"[a-zA-Z0-9\_\-\.]+@[a-zA-Z0-9\_\-\.]+\.com") # First REGEX pattern to extract everything with an email pattern
# REGEX to be used to validate ALU's Official email adress, We used compile to say that this regex pattern can be used multiple times.
ALU_mail_pattern = re.compile(r"^[a-zA-Z0-9\.]+@alueducation\.com$")
ALUMNI_mail_pattern = re.compile(r"^[a-zA-Z0-9\.]+@alumni.alueducation\.com$") # REGEX Pattern to Validate ALU alumni email addresses that end with '@alumni.alueducation'
SI_mail_pattern = re.compile(r"^[a-zA-Z0-9\.]+@si.alueducation\.com$") # REGEX Pattern to Validate ALU SI email addresses that end with '@si.alueducation.com'
student_email = re.compile(r"^[a-zA-Z0-9\.\_\-]+@alustudent\.com$") # REGEX Pattern to Validate ALU student email addresses
### Validating Card Section
# REGEX pattern to help search for anynumbers in format of a VISA card number. 
    # '\b'for telling regex to bound it together a single sequence, not to select just 16-digits from a long number
    # '(?:\d{4}[- ])' '(?...)' is for treating everything in there a single unit i.e: four digits will be grouped togehter as a single unit, then separeted by either a '-' or ' '(space)
    #{3}: repeat thet 4 digits pattern three times
    #\d{4} equals the last four digits
general_card_pattern = re.compile(r"\b(?:\d{4}[- ]?){3}\d{4}")


def validate_email(email):    # Function to validate extracted emails, based on the REGEX patterns we predefined
    """
    Validating emails
    """
    if ALU_mail_pattern.fullmatch(email):     # first condition to check if its an official ALU email address, then return 'Valid ALU official email adress'
        return "Valid ALU official email Adress"
    if ALUMNI_mail_pattern.fullmatch(email):    # Second condition to check if its an ALU ALUMNI email adress, then return 'Valid ALUMNI email adress'
        return "Valid ALUMNI email Adress"
    if SI_mail_pattern.fullmatch(email):    # Third condition to check if its an ALU SI email address, then return 'Valid ALU SI email adress'    
        return "Valid ALU SI email Adress"
    if student_email.fullmatch(email):     # condition to check if its an official ALU student email address, then return 'Valid ALU student email adress'
        return "Valid ALU student email Adress"
    #if the email adress is malicious or doesn't fit in those other categories return 'Invalid email adress!'
    return "Invalid email address! "

# function to validate card number
def validate_card(card):
    card_numbers = re.sub(r"\D", "", card)  # this to remove none-digit characters from the number
    if len(card_numbers) != 16:
        return False
    return "**** **** **** " + card_numbers[-4:]

Function for extracting all email adresses from the 'raw-text.txt' file based on the 'regular_mail_pattern' 
    # and then checking their status using the 'validate_email()' function 
def extract_emails(text):
    """
    Extracting emails from text
    """
    emails = regular_mail_pattern.findall(text)
    results = []
    for email in emails:
        results.append({
            "Email Address":email,
            "Status":validate_email(email)
        })
    return results


def extract_card(text):    #  Function to extract card_numbers
    cards = general_card_pattern.findall(text)  # extract cards, using findall() function, and depending on the 'general_card_pattern' regex pattern we defined
    results = []
    for card in cards:
        if validate_card(card): #if extracted card match our validation condition, append that card to the 'results' list
            results.append({
                "Card Number": validate_card(card),
                "Status": "Valid card Number"
            })
    return results

def main():
    try :
        text = file.read_text(encoding="utf-8")  #asssigning the file contents to the text variable, to help us use it 
    except FileNotFoundError:
        print(f"File not found")
        return
    
    emails = extract_emails(text) # assign extracted emails that match our regex patterns to the 'emails' variable so that we can print them
    print("Email Extraction results: ")
    print(" = " *8 )
    print(
          f"{'Email Adress':60}"
          f"{" Status"}"
    )
    for item in emails:
        print(
            f"{item['Email Address']:60} "
            f"{item['Status']}"
        )
    print("")
    cards = extract_card(text)
    print(f"    Cards result")
    print(
        f"{'Card Number' :60}"
        f"{'Status'}"
    )
    for card in cards:
        print(
            f"{card['Card Number'] :60}"
            f"{card['Status']}"
        )
if __name__ == "__main__":
    main()
