from src.password_checker import score, rating, has_symbol


def test_empty_password_is_zero():
    assert score("") == 0


def test_common_password_is_zero():
    assert score("Password") == 0


def test_strong_password():
    assert score("Tr0ub4dor&3xyz") == 5
    assert rating("Tr0ub4dor&3xyz") == "strong"


def test_weak_password():
    assert rating("abc") == "weak"


def test_medium_password():
    assert rating("abcDEF12") == "medium"


def test_symbol_detection():
    assert has_symbol("hi!")
    assert not has_symbol("hi")
