import re # REGEX library
from pathlib import Path # Library to help access file in a certain path
file = Path(__file__).parent.parent / "input" / "raw-text.txt"  # Access the 'raw-text.txt' file from the 'input' directory, and asign its content to the 'file' variable

# We will use 're.compile' to create a reusable regex pattern
regular_mail_pattern = re.compile(r"[a-zA-Z0-9\_\-\.]+@[a-zA-Z0-9\_\-\.]+\.com") # First REGEX pattern to extract everything with an email pattern
# REGEX to be used to validate ALU's Official email adress, We used compile to say that this regex pattern can be used multiple times.
ALU_mail_pattern = re.compile(r"^[a-zA-Z0-9\.]+@alueducation\.com$")

# Function to validate extracted emails, based on the REGEX patterns we predefined
def validate_email(email):
    """
    Validating emails
    """
    # first condition to check if its an official ALU email address, then return 'Valid ALU official email adress'
    if ALU_mail_pattern.fullmatch(email):
        return "Valid ALU official email Adress"
