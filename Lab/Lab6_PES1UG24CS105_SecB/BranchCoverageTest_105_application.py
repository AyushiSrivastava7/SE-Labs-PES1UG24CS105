import pytest
from scholarship_awards import award_amount, is_eligible, application_status


# Branch tests for award_amount()

def test_unknown_category():
    with pytest.raises(ValueError):
        award_amount("science", 90, "low", False)


def test_negative_marks():
    with pytest.raises(ValueError):
        award_amount("merit", -1, "low", False)


def test_renewal_merit():
    assert award_amount("merit", 71, "low", True) == 100


def test_renewal_sports():
    assert award_amount("sports", 61, "low", True) == 100


def test_nonrenewal():
    assert award_amount("merit", 80, "low", False) == 500


def test_at_cutoff():
    assert award_amount("merit", 75, "low", False) == 0


def test_low_income_above_15():
    assert award_amount("merit", 91, "low", False) == 2560


def test_high_income_above_15():
    assert award_amount("merit", 91, "high", False) == 1600


def test_low_income_at_most_15():
    assert award_amount("merit", 81, "low", False) == 600


def test_high_income_at_most_15():
    assert award_amount("merit", 81, "high", False) == 360


# Branch tests for is_eligible()

def test_special_quota_eligible():
    assert is_eligible(50, 2, True) is True


def test_special_quota_not_eligible():
    assert is_eligible(50, 3, True) is False


def test_normal_low_attendance():
    assert is_eligible(74, 0, False) is False


def test_normal_eligible():
    assert is_eligible(75, 1, False) is True


def test_normal_too_many_backlogs():
    assert is_eligible(90, 2, False) is False


# Branch tests for application_status()

def test_renewal_open():
    assert application_status(30, True, False) == "open"


def test_nonrenewal_open():
    assert application_status(20, False, False) == "open"


def test_paper_open():
    assert application_status(30, False, True) == "open"


def test_closing():
    assert application_status(10, False, False) == "closing"


def test_paper_closing():
    assert application_status(15, False, True) == "closing"


def test_renewal_closed():
    assert application_status(14, True, False) == "closed"


def test_paper_closed():
    assert application_status(4, False, True) == "closed"
