"""
Email Validator Utility

This module provides an EmailValidator class for validating and normalizing email addresses.

Usage:
  validator = EmailValidator()
  if validator.validate(email):
    normalized_email = validator.normalize(email)
"""

import re

class EmailValidator:
  
  def validate(self, email):
    """Validates an email address."""
    if not isinstance(email, str):
      raise ValueError("Email must be a string")
    if "@" not in email:
      return False
    localpart, domain = email.split("@")
    if len(localpart) < 1 or len(localpart) > 64:
      return False  
    return True

  def normalize(self, email):
    """Normalizes an email address."""
    # remove leading/trailing whitespace
    email = email.strip()
    
    # remove dots from localpart
    localpart, domain = email.split("@")
    localpart.replace(".", "")

    # convert domain to lowercase
    normalized = f"{localpart}@{domain.lower()}"
    return normalized

if __name__ == "__main__":
  validator = EmailValidator()
  
  emails = [
    "alice@example.com",
    "bob.smith@example.com",
    "invalid.email",
    "toolonglocalpartxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@example.com",
    "   carol@example.com   "
  ]

  for email in emails:
    if validator.validate(email):
      print(f"Valid: {email}")
      normalized = validator.normalize(email)
      print(f"Normalized: {normalized}")
    else:
      print(f"Invalid: {email}")
