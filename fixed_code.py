""" Email Validator Utility

This module provides an EmailValidator class for validating and normalizing email addresses.

Usage:
  validator = EmailValidator()
  if validator.validate(email):
    normalized_email = validator.normalize(email)
"""
import re


class EmailValidator:
    """
    A class for validating and normalizing email addresses.

    Methods:
    - validate: Checks if the provided email address is valid.
    - normalize: Normalizes the email address for consistency.
    """

    def __init__(self):
        # Precompile regex for performance and reuse.
        self.email_regex = re.compile(
            r"(^[a-zA-Z0-9_.+-]{1,64}@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        )

    def validate(self, email):
        """
        Validates an email address based on standard criteria.

        Parameters:
        - email (str): The email address to validate.

        Returns:
        - bool: True if valid, False otherwise.
        """
        if not isinstance(email, str):
            raise ValueError("Email must be a string")

        # Use regex for comprehensive validation.
        return bool(self.email_regex.match(email.strip()))

    def normalize(self, email):
        """
        Normalizes an email address by trimming spaces, removing dots from
        the local part, and converting the domain part to lowercase.

        Parameters:
        - email (str): The email address to normalize.

        Returns:
        - str: The normalized email address.
        """
        if not self.validate(email):  # Ensure email is valid before normalization.
            raise ValueError("Cannot normalize an invalid email address.")

        # Normalize email.
        email = email.strip()
        local_part, domain = email.split("@")
        local_part = local_part.replace(".", "")
        normalized_email = f"{local_part.lower()}@{domain.lower()}"

        return normalized_email


if __name__ == "__main__":
    validator = EmailValidator()

    emails = [
        "alice@example.com",
        "bob.smith@example.com",
        "invalid.email",
        "toolonglocalpartxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@example.com",
        "   carol@example.com   "
    ]

    for email_address in emails:
        try:
            if validator.validate(email_address):
                print(f"Valid: {email_address}")
                normalized = validator.normalize(email_address)
                print(f"Normalized: {normalized}")
            else:
                print(f"Invalid: {email_address}")
        except ValueError as e:
            print(f"Error: {e}")
"""
**Result**
----------


Valid: alice@example.com
Normalized: alice@example.com
Valid: bob.smith@example.com
Normalized: bobsmith@example.com
Invalid: invalid.email
Invalid: toolonglocalpartxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@example.com
Valid:    carol@example.com   
Normalized: carol@example.com


**Key Improvements Made**:
-------------------------

 - Enhanced Email Validation: 
    The validation method now uses a regular expression to ensure that the email address conforms to a more precise and widely accepted format. This regex checks for the presence of a username part followed by a domain part, with appropriate characters and structure.
    
 - Normalization Check:
    Before normalizing an email, it now checks if the email is valid. This prevents attempts to normalize invalid email addresses.
    
 - Regex Optimization:
    The regular expression for email validation is compiled in the __init__ method for better performance, especially when validating multiple email addresses.
    
 - Error Handling:
    Added error handling in the main execution block to gracefully handle invalid email addresses during normalization.
    
 - Documentation:
    Improved method documentation to clearly describe the purpose, parameters, and return values for better understanding and maintainability of the code.
"""
