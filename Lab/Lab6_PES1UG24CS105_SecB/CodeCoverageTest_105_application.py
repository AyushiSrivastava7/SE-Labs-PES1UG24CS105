import pytest
from scholarship_awards import award_amount, is_eligible, application_status


# Tests for award_amount()

def test_below_cutoff():
    assert award_amount("merit", 70, "low", False) == 0


def test_unknown_category():
    with pytest.raises(ValueError):
        award_amount("science", 90, "low", False)


def test_negative_marks():
    with pytest.raises(ValueError):
        award_amount("merit", -1, "low", False)


def test_merit_renewal():
    assert award_amount("merit", 71, "low", True) == 100


def test_sports_renewal():
    assert award_amount("sports", 61, "low", True) == 100


def test_low_income_normal_award():
    assert award_amount("merit", 81, "low", False) == 600


def test_high_income_normal_award():
    assert award_amount("merit", 81, "high", False) == 360


def test_low_income_high_marks():
    assert award_amount("arts", 81, "low", False) == 2560


def test_high_income_high_marks():
    assert award_amount("merit", 91, "high", False) == 1600


# Tests for is_eligible()

def test_special_quota_eligible():
    assert is_eligible(50, 2, True) is True


def test_special_quota_not_eligible():
    assert is_eligible(90, 3, True) is False


def test_low_attendance():
    assert is_eligible(74, 0, False) is False


def test_normal_eligible():
    assert is_eligible(90, 1, False) is True


def test_normal_not_eligible():
    assert is_eligible(90, 2, False) is False


# Tests for application_status()

def test_application_open():
    assert application_status(20, False, False) == "open"


def test_application_closing():
    assert application_status(10, False, False) == "closing"


def test_application_closed():
    assert application_status(4, False, False) == "closed"


def test_renewal_open():
    assert application_status(30, True, False) == "open"


def test_paper_application_open():
    assert application_status(30, False, True) == "open"


def test_paper_application_closing():
    assert application_status(15, False, True) == "closing"
