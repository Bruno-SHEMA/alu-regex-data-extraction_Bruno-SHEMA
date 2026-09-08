# Data Extraction & Secure Validation Assignment
In this assignment, I had the task of creating a regex-based program that will:
1. Extract different types of data from the sample input text called 'raw-text.txt'
2. Validate those extracted data using REGEX patterns, make sure there is no suspacios or malicious content
3. Prevent unnecessary exposure of Sensitive data like card numbers
 # Project Folder structure  

    alu-regex-data-extraction_Bruno-SHEMA/
    ├── input/
    │     └── raw-text.txt
    ├── src/
    │   └── main.py
    ├── output/
    │   └── sample-output.json
    └── README.md

# How this program works
This program works: , validate those data to check if the extracted data matches those patterns, masks sensitive data, check 
I used Python regex patterns to extract and validate four main data types:
 # 1. Extract raw data from 'raw-text.txt'
this program Searches through the 'raw-text.txt' input file using regular explession(REGEX) patterns I wrote, and then extract matching data. It basically go into the raw-text.txt file and check if for example something looks like an email, or phone number, or URL link or even a Visa card number, then extract it and move to the validation stage.
 # 2. Validates the extracted data.
On this part I wrote regex-patterns to validate four main data types:
 1. Email Adresses

This program extracts many different email addresses that match the regular email pattern and checks whether they belong to recognized ALU email domains.
regex_pattern I used to extract everything that looks like an email: 
    (r"[a-zA-Z0-9\_\-\.]+@[a-zA-Z0-9\_\-\.]+\.com")
I then used other After extracting them I used other patterns to validate the extracted emails to make sure they match ALU's specific email adresses. Patterns I used to I dentify them:

    (r"^[a-zA-Z0-9\.]+@alueducation\.com$")
    (r"^[a-zA-Z0-9\.]+@alumni.alueducation\.com$")
    (r"^[a-zA-Z0-9\.]+@si.alueducation\.com$")
    (r"^[a-zA-Z0-9\.\_\-]+@alustudent\.com$")

The supported ALU domains are:

    @alueducation.com
    @alumni.alueducation.com
    @si.alueducation.com

Student email addresses that end with '@alustudent.com' are also checked according to the student email validation pattern defined in the source code.
Other email addresses that do not match the supported formats are classified as ' invalid '.

 2. Credit Card Numbers

This program identifies 16-digit credit card numbers written with spaces or hyphens using the following regex-pattern: 

    (r"\b(?:\d{4}[- ]?){3}\d{4}")

 - Pattern description:
-'\b'for telling regex to bound it together a single sequence, not to select just 16-digits from a long number
-'(?:\d{4}[- ])' '(?...)' is for treating everything in there a single unit i.e: four digits will be grouped togehter as a single unit, then separeted by either a '-' or ' '(space)
-{3}: repeat thet 4 digits pattern three times
-\d{4} equals the last four digits

For security , credit card numbers are not displayed in full. Only the last four digits are shown.

Example:

4243 4512 6242 4242

is displayed as:

**** **** **** 4242
I did this to prevent unnecessary exposure of sensitive data.

 3. Phone Numbers

This program also extracts Rwandan phone numbers using supported formats, and then validate it.
Real rwandan phone numbers are flagged valid, while others are displayed as invalid.
 
 4. URL Links

In this program I also chose to also extract and validate URL links, all links that begin with 'https://', 'http://', and 'www.' then a domain name, and '.com', '.rw' were validated.
 # 3. Masks sensitive data and ignore malicious inputs.
After extracting and validating the extracted data, I used a 'mask' technique to hide senstive data. for this part I masked the credit card numbers to ensure its security.
The program also checks for any text designed to manipulate application logic, alter data interpretation, or compromise it, and say that 'suspicious inputs were detected' and skip them.
The system doesn't also trust all input text, it ignores suspicious inputs, and treat them as regular text.
 # 4. Displays Validation results and status.

# How to run: 
Before running this program, you must have ' python' installed, no external python libraries required.
First clone the repository into your local computer using link: 

    https://github.com/Bruno-SHEMA/alu-regex-data-extraction_Bruno-SHEMA.git

After cloning it navigate into the root directory, then navigate into src/ directory because it is where the source code is at:

    cd alu-regex-data-extraction_Bruno-SHEMA
    cd src/

To run it use (Within the src/ directory):

    python3 main.py

You can also use: ' python3 src/main.py ' within the parent folder (alu-regex-data-extraction_Bruno-SHEMA)
