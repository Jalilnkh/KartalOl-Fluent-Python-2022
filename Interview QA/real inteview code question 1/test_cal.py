from datetime import datetime
from unittest.mock import patch
from cal import calculate, Developer, Language, HACKTOBER_BONUS

# The following code is answer of question

def test_calculate_no_languages_no_followers():
    dev = Developer(accepted_contributions=5, followers=0, languages=set())
    assert calculate(dev) == 0


def test_calculate_no_languages_no_followers():
    dev = Developer(accepted_contributions=5, followers=0, languages=set())
    assert calculate(dev) == 0


def test_calculate_python_language_some_followers():
    dev = Developer(accepted_contributions=5, followers=10, languages={Language.PYTHON})
    assert calculate(dev) == (10 * 2) + (2 * 1) ** 2


def test_calculate_not_during_hacktober():
    dev = Developer(accepted_contributions=5, followers=10, languages={Language.PYTHON})
    assert calculate(dev) == (10 * 2) + (2 * 1) ** 2


@patch('pydevcalc.calculator.datetime')
def test_calculate_during_hacktober(mock_datetime):
    mock_datetime.now.return_value = datetime(2024, 10, 1)
    dev = Developer(accepted_contributions=5, followers=10, languages={Language.PYTHON})
    expected_score = (10 * 2) + (2 * 1) ** 2 + HACKTOBER_BONUS
    assert calculate(dev) == expected_score