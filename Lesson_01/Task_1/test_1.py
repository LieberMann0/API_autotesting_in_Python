from checkTest import checkText


def test_step1(good, bad):
    assert good in checkText(bad)
