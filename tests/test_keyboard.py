from src.keyboard import KeyBoard


kb = KeyBoard ('Dark Project KD87A', 9600, 5)

def test_str():
    assert str(kb) == "Dark Project KD87A"

def test_lang():
    assert str (kb.language) == "EN"


def test_change_lang():
    if kb.change_lang():
        assert str (kb.language) == "RU"
    elif kb.change_lang().kb.change_lang():
        assert str (kb.language) == "EN"

def test_other_lang():
    if kb.language != "EN":
        assert str (kb.language) == "RU"
    if kb.language != "RU":
        assert str (kb.language) == "EN"
    if kb.language == "CH":
        assert "AttributeError: property 'language' of 'KeyBoard' object has no setter"


