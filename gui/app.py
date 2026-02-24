import tkinter as tk
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.converter import MorseCodeConverter

class MorseGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Morse Code Converter")
        self.root.geometry("400x450")
        self.converter = MorseCodeConverter()

        # --- UI Elements ---
        
        # Label Instruksi
        self.label_input = tk.Label(root, text="Masukkan Teks:", font=("Arial", 10, "bold"))
        self.label_input.pack(pady=10)

        # Text Box Input
        self.text_input = tk.Text(root, height=5, width=40)
        self.text_input.pack(pady=5)

        # Tombol Konversi
        self.btn_convert = tk.Button(root, text="Konversi ke Morse", command=self.handle_conversion, 
                                     bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        self.btn_convert.pack(pady=15)

        # Label Output
        self.label_output = tk.Label(root, text="Hasil Kode Morse:", font=("Arial", 10, "bold"))
        self.label_output.pack(pady=5)

        # Text Box Output (ReadOnly)
        self.text_output = tk.Text(root, height=8, width=40, bg="#f0f0f0")
        self.text_output.pack(pady=5)

        # Tombol Clear
        self.btn_clear = tk.Button(root, text="Hapus Semua", command=self.clear_fields)
        self.btn_clear.pack(pady=10)

    def handle_conversion(self):
        raw_text = self.text_input.get("1.0", tk.END).strip()
        
        if not raw_text:
            messagebox.showwarning("Peringatan", "Silakan masukkan teks terlebih dahulu!")
            return

        try:
            morse_result = self.converter.text_to_morse(raw_text)
            
            self.text_output.config(state=tk.NORMAL)
            self.text_output.delete("1.0", tk.END)
            self.text_output.insert(tk.END, morse_result)
            self.text_output.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

    def clear_fields(self):
        self.text_input.delete("1.0", tk.END)
        self.text_output.config(state=tk.NORMAL)
        self.text_output.delete("1.0", tk.END)
        self.text_output.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = MorseGui(root)
    root.mainloop()