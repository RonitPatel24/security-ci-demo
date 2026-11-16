"""Simple password strength checker used to demo CI/CD with security scanning."""

import string

COMMON_PASSWORDS = {"password", "123456", "qwerty", "letmein", "admin", "welcome"}


def has_upper(pw: str) -> bool:
    return any(c.isupper() for c in pw)


def has_lower(pw: str) -> bool:
    return any(c.islower() for c in pw)


def has_digit(pw: str) -> bool:
    return any(c.isdigit() for c in pw)


def has_symbol(pw: str) -> bool:
    return any(c in string.punctuation for c in pw)


def score(pw: str) -> int:
    """Return a strength score from 0 to 5."""
    if not pw or pw.lower() in COMMON_PASSWORDS:
        return 0
    points = 0
    if len(pw) >= 12:
        points += 1
    points += has_upper(pw) + has_lower(pw) + has_digit(pw) + has_symbol(pw)
    return points


def rating(pw: str) -> str:
    """Return 'weak', 'medium', or 'strong'."""
    s = score(pw)
    if s <= 2:
        return "weak"
    if s <= 3:
        return "medium"
    return "strong"
