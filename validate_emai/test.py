from email_task import is_valid_email


def test_invalid_email():
    assert is_valid_email('invalid-email') == False


def test_valid_email():
    assert is_valid_email('umelbaneen_almousawi@sigmalabs.com') == True
