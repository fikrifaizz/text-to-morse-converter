from . import mappings
from .utils import clean_text

class MorseCodeConverter:
    def __init__(self):
        self.morse_code_dict = mappings.MORSE_CODE_DICT

    def text_to_morse(self, text):
        text = clean_text(text)
        morse_code = []
        for char in text:
            if char == " ":
                morse_code.append("/")
            elif char in self.morse_code_dict:
                morse_code.append(self.morse_code_dict[char])
        return " ".join(morse_code)    