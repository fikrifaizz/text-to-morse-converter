def clean_text(text):
    # Menghapus jika simbol yang tidak didukung
    text = text.upper().strip()
    text = ''.join(char for char in text if char.isalnum() or char.isspace())
    return text