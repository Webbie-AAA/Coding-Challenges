import re


def is_valid_email(email: str) -> bool:
    return bool(re.match(r'\b[A-Za-z0-9][A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b', email))


print(is_valid_email('invalid-email'))
# def is_valid_email_with_regex(email: str) -> bool:
#     pattern = r'\b[A-Za-z0-9._-]+@[A-Za-z0-9-]+.[A-Za-z]{2,6}'
#     return bool(re.match(pattern, email))


class EmailAddress:
    def __init__(self, raw_email: str):
        # 1. Clean the data (remove accidental spaces)
        self.raw = raw_email.strip()

        # 2. Run the specialized validation checks
        self._validate_length()
        self._validate_no_double_dots()
        self._validate_structure()

        # If we get here, the email is officially "Valid"
        self.email = self.raw

    def _validate_length(self):
        if len(self.raw) > 254:
            raise ValueError("Email is too long (Max 254 chars)")

    def _validate_no_double_dots(self):
        if ".." in self.raw:
            raise ValueError("Email cannot contain consecutive dots (..)")

    def _validate_structure(self):
        # We use a cleaner Regex here because we already handled
        # length and double-dots above!
        pattern = r'^[A-Za-z0-9][A-Za-z0-9._-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}$'
        if not re.match(pattern, self.raw):
            raise ValueError(
                "Invalid email structure or illegal starting character")

    def __str__(self):
        return self.email
