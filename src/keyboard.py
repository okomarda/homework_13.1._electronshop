from src.item import Item

class Mixing_lang():
    lang_count = 0

    def __init__(self):
        pass

    def change_lang(self):
        self.lang_count += 1
        if self.lang_count % 2 == 0:
            self._language = "EN"
            return self
        else:
            self._language = "RU"
            return self


class KeyBoard(Item, Mixing_lang):

    def __init__(self, name, price, quantity, language="EN"):
        super().__init__(name, price, quantity)
        self._language = language

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        if value == "RU" or value == "EN":
            return self._language
        else:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")




# kb = KeyBoard('Dark Project KD87A', 9600, 5)
# print(kb.language)
# # kb.change_lang()
# # print(kb.language)
# # kb.change_lang()
# # print(kb.language)
# #kb.language = "CH"
# kb.change_lang().change_lang().change_lang().change_lang()
# print(kb.language)


