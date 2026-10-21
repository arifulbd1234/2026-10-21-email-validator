"""
Day 15 - 2026-10-21
Tool: Email Validator
What it does: Checks whether an email address looks valid - one @ sign,
a sensible username, a real-looking domain with a dot and ending -
and explains exactly what is wrong when it is not, before a form is
submitted or a message bounces.
Who it helps: Anyone filling in online forms, shop owners checking a
customer's email, or developers sanity-checking sign-up data.
"""


def check_email(raw):
    """Return (True, 'OK') or (False, reason) for an email address."""
    email = raw.strip()
    if not email:
        return False, "Email is empty."
    if " " in email:
        return False, "Email must not contain spaces."
    if email.count("@") != 1:
        return False, "Email must contain exactly one @."
    username, domain = email.split("@")
    if not username:
        return False, "Nothing before the @."
    if username.startswith(".") or username.endswith("."):
        return False, "Username must not start or end with a dot."
    if ".." in email:
        return False, "Email must not contain two dots together."
    if "." not in domain:
        return False, "Domain needs a dot, like gmail.com."
    if domain.startswith(".") or domain.endswith("."):
        return False, "Domain must not start or end with a dot."
    ending = domain.rsplit(".", 1)[-1]
    if len(ending) < 2 or not ending.isalpha():
        return False, "Domain ending (like .com) looks wrong."
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._%+-")
    if any(ch not in allowed for ch in username):
        return False, "Username has an unusual character in it."
    return True, "OK"


def is_valid_email(raw):
    return check_email(raw)[0]


def domain_of(raw):
    """Return the domain part (after @), lower case, if valid."""
    if not is_valid_email(raw):
        raise ValueError(check_email(raw)[1])
    return raw.strip().split("@")[1].lower()


if __name__ == "__main__":
    tests = [
        "arifulbd1234@gmail.com",   # a normal valid address
        "shop.owner@my-shop",       # domain has no dot
        "two@@signs.com",           # two @ signs
    ]
    for email in tests:
        ok, reason = check_email(email)
        print(email, "-> valid?", ok, "-", reason)
    print("Domain of first:", domain_of(tests[0]))
