import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.converter import MorseCodeConverter

def main():
    print("="*40)
    print("Text to Morse Code Converter")
    print("="*40)

    converter = MorseCodeConverter()
    while True:
        text = input("Enter text to convert: ")
        morse_code = converter.text_to_morse(text)
        print("Text: ", text)
        print("Morse Code: ", morse_code)
        
        choice = input("Do you want to convert another text? (y/n): ")
        if choice.lower() != "y":
            break

if __name__ == "__main__":
    main()