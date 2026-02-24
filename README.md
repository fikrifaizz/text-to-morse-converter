# Text to Morse Code Converter

## Deskripsi

Sebuah aplikasi sederhana yang berfungsi untuk mengubah teks menjadi kode Morse.

## Alur Logika

1. Input Teks
2. Membersihkan Teks (Menghapus karakter khusus)
3. Mengubah Teks menjadi Kode Morse
4. Output Kode Morse

## Contoh Penggunaan

Input: "Hello World"

Output: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."

## Fitur

- Konversi Teks ke Morse
- Penanganan Input (Membersihkan karakter khusus)
- Pengujian Unit (Unit Testing)
- GUI (Graphical User Interface)

## Instalasi

1. Clone repositori:
   ```bash
   git clone https://github.com/fikrifaizz/text-to-morse-converter.git
   cd text-to-morse-converter
   ```

2. (Opsional) Buat dan aktifkan virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # venv\Scripts\activate  # Windows
   ```

## Penggunaan

### Menjalankan Aplikasi

```bash
python3 main.py
```

### Menjalankan Unit Tests

```bash
python3 -m unittest test/test_converter.py
```

### Menjalankan GUI

```bash
python3 gui/app.py
```

## Struktur Proyek

```
text-to-morse-converter/
├── src/
│   ├── __init__.py
│   ├── converter.py      # Logika konversi
│   ├── mappings.py         # Kamus kode Morse
│   └── utils.py            # Fungsi utilitas
├── test/
│   ├── __init__.py
│   └── test_converter.py   # Unit tests
├── main.py                 # Entry point aplikasi
└── README.md               # Dokumentasi
```

## Demo Aplikasi

![Demo Aplikasi](assets/demo_app.gif)