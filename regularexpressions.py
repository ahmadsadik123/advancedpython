import re


# 1. Match a date in the format "MM/DD/YYYY", where MM is the two-digit month,
#   DD is the two-digit day, and YYYY is the four-digit year.

date_pattern = r"^(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[01])\/\d{4}$"

date_str = "02/28/2023"

dmatch = re.match(date_pattern, date_str)

if dmatch:
    print("Matched date:", dmatch.group())
else:
    print("Date not matched.")


# 2. Match an email address in the format "username@domain.com",
#   where "username" can contain letters, numbers, dots, dashes, and underscores,
#   and "domain" can contain letters and dots.

email_pattern = r"^[a-zA-Z0-9._-]+@[a-zA-Z.]+$"

email_str = "johndoe1234@example.com"

ematch = re.match(email_pattern, email_str)

if ematch:
    print("Matched email:", ematch.group())
else:
    print("Email not matched.")


# 3. Match a URL in the format "http(s)://www.domain.com/path/to/page.html",
#   where "(s)" is optional and indicates that the connection should be secure,
#   "www" is optional and can be replaced by any subdomain,
#   "domain.com" can be any valid domain name, and "/path/to/page.html" can be any path or file name.

url_pattern = r"^https?://[a-zA-Z0-9.-]+(/[a-zA-Z0-9./_-]*)?$"

url_str = "https://www.example.com/path/to/page.html"

umatch = re.match(url_pattern, url_str)

if umatch:
    print("Matched URL:", umatch.group())
else:
    print("URL not matched.")


# 4. Match a phone number in the format "(XXX) XXX-XXXX", where "X" is a digit.

phone_pattern = r"^\(\d{3}\) \d{3}-\d{4}$"

phone_str = "(123) 456-7890"

pmatch = re.match(phone_pattern, phone_str)

if pmatch:
    print("Matched phone number:", pmatch.group())
else:
    print("Phone number not matched.")


# 5. Match a string that contains at least one uppercase letter,
#   one lowercase letter, and one digit, and is between 8 and 20 characters long.

password_pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}$"

password_str = "Abc123def"

passmatch = re.match(password_pattern, password_str)

if passmatch:
    print("Matched password:", passmatch.group())
else:
    print("Password not matched.")


# 6. Match a string that contains only letters, numbers, and spaces,
#   and is between 5 and 50 characters long.

string_pattern = r"^[a-zA-Z0-9 ]{5,50}$"

string_str = "Hello World 123"

smatch = re.match(string_pattern, string_str)

if smatch:
    print("Matched string:", smatch.group())
else:
    print("String not matched.")


# 7. Match a string that contains at least one uppercase letter,
#   one lowercase letter, one digit, and one special character,
#   and is between 8 and 20 characters long.

password2_pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&+=]).{8,20}$"

password2_str = "Abc123!def"

p2match = re.match(password2_pattern, password2_str)

if p2match:
    print("Matched password:", p2match.group())
else:
    print("Password not matched.")


# 8. Match a credit card number in the format "XXXX-XXXX-XXXX-XXXX",
#   where "X" is a digit.

credit_card_pattern = r"\d{4}-\d{4}-\d{4}-\d{4}"

credit_card_str = "1234-5678-9012-3456"

cmatch = re.match(credit_card_pattern, credit_card_str)

if cmatch:
    print("Matched credit card number:", cmatch.group())
else:
    print("Credit card number not matched.")
