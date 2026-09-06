import re # REGEX library
from pathlib import Path # Library to help access file in a certain path
file = Path(__file__).parent.parent / "input" / "raw-text.txt"  # Access the 'raw-text.txt' file from the 'input' directory, and asign its content to the 'file' variable

# We will use 're.compile' to create a reusable regex pattern
regular_mail_pattern = re.compile(r"[a-zA-Z0-9\_\-\.]+@[a-zA-Z0-9\_\-\.]+\.com") # First REGEX pattern to extract everything with an email pattern
