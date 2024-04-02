"""
Email Validator Utility

This module provides an EmailValidator class for validating and normalizing email addresses.

Usage:
  validator = EmailValidator()
  if validator.validate(email):
    normalized_email = validator.normalize(email)
"""


class EmailValidator:

    def validate(self, email):
        """Validates an email address."""
        if not isinstance(email, str):  # Good type checking.
            raise ValueError("Email must be a string")
        if "@" not in email:  # Simple check for '@', but does not fully validate the domain part.
            return False
        localpart, domain = email.split("@")
        # No validation for domain part, consider adding domain validation (e.g., presence of a top-level domain).
        if len(localpart) < 1 or len(localpart) > 64:
            # Validates length of local part but does not check domain length.
            return False
        return True  # Consider implementing regex for comprehensive email validation.

    def normalize(self, email):
        """Normalizes an email address."""
        email = email.strip()  # Good use of strip to remove leading/trailing whitespaces.

        # Bug: localpart.replace(".", "") does not update localpart since strings are immutable.
        localpart, domain = email.split("@")
        localpart.replace(".", "")  # Fix: Assign the result back to localpart.

        # Lowercasing the domain is good, but consider also lowercasing the localpart if case-insensitive.
        normalized = f"{localpart}@{domain.lower()}"
        return normalized


if __name__ == "__main__":
    validator = EmailValidator()

    emails = [
        "alice@example.com",
        "bob.smith@example.com",
        "invalid.email",  # No indication of what makes an email valid or invalid in the docstring.
        "toolonglocalpartxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@example.com",
        # Example helps illustrate limitations.
        "   carol@example.com   "
    ]

    for email in emails:
        if validator.validate(email):
            print(f"Valid: {email}")  # This is a good practice, clearly showing which emails are considered valid.
            normalized = validator.normalize(email)
            print(f"Normalized: {normalized}")
        else:
            print(f"Invalid: {email}")  # Helps in quickly identifying invalid emails.

"""
**Result**
----------


Valid: alice@example.com
Normalized: alice@example.com
Valid: bob.smith@example.com  #The email is valid, but not normalized correctly.
Normalized: bob.smith@example.com
Invalid: invalid.email
Invalid: toolonglocalpartxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@example.com
Valid:    carol@example.com
Normalized: carol@example.com

"""
