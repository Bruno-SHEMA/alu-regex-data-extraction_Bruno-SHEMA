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

# Function to validate extracted emails, based on the REGEX patterns we predefined
def validate_email(email):
    """
    Validating emails
    """
    # first condition to check if its an official ALU email address, then return 'Valid ALU official email adress'
    if ALU_mail_pattern.fullmatch(email):
        return "Valid ALU official email Adress"
    # Second condition to check if its an ALU ALUMNI email adress, then return 'Valid ALUMNI email adress'
    if ALUMNI_mail_pattern.fullmatch(email):
        return "Valid ALUMNI email Adress"
    # Third condition to check if its an ALU SI email address, then return 'Valid ALU SI email adress'
    if SI_mail_pattern.fullmatch(email):
        return "Valid ALU SI email Adress"
    # first condition to check if its an official ALU student email address, then return 'Valid ALU student email adress'
    if student_email.fullmatch(email):
        return "Valid ALU student email Adress"
    #if the email adress is malicious or doesn't fit in those other categories return 'Invalid email adress!'
    return "Invalid email address! "

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

def main():
    try :
        text = file.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"File not found")
        return
    emails = extract_emails(text)
    print("Email Extraction results: ")
    print(" = " *8 )
    print(
          f"{'Email Adress':60}"
          f"{'Status'}"
    )
    for item in emails:
        print(
            f"{item['Email Address']:60} "
            f"{item['Status']}"
        )
if __name__ == "__main__":
    main()
