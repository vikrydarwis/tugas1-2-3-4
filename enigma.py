import tkinter as tk
from tkinter import messagebox

class EnigmaCipher:
    def _init_(self, rotor1_pos=0, rotor2_pos=0, rotor3_pos=0):
        self.rotor1 = list(range(26))
        self.rotor2 = list(range(26))
        self.rotor3 = list(range(26))
        self.reflector = list(range(25, -1, -1))

        self.rotor1_pos = rotor1_pos
        self.rotor2_pos = rotor2_pos
        self.rotor3_pos = rotor3_pos

    def rotate_rotors(self):
        self.rotor1_pos = (self.rotor1_pos + 1) % 26
        if self.rotor1_pos == 0:
            self.rotor2_pos = (self.rotor2_pos + 1) % 26
            if self.rotor2_pos == 0:
                self.rotor3_pos = (self.rotor3_pos + 1) % 26

    def encrypt_decrypt_char(self, char):
        if not char.isalpha():
            return char

        is_lower = char.islower()
        offset = ord(char.upper()) - ord('A')

        # Forward pass through rotors
        offset = (self.rotor1[(offset + self.rotor1_pos) % 26] + self.rotor1_pos) % 26
        offset = (self.rotor2[(offset + self.rotor2_pos) % 26] + self.rotor2_pos) % 26
        offset = (self.rotor3[(offset + self.rotor3_pos) % 26] + self.rotor3_pos) % 26

        # Reflector
        offset = self.reflector[offset]

        # Backward pass through rotors
        offset = (self.rotor3.index((offset - self.rotor3_pos) % 26) - self.rotor3_pos) % 26
        offset = (self.rotor2.index((offset - self.rotor2_pos) % 26) - self.rotor2_pos) % 26
        offset = (self.rotor1.index((offset - self.rotor1_pos) % 26) - self.rotor1_pos) % 26

        self.rotate_rotors()

        result = chr(offset + ord('A'))
        return result.lower() if is_lower else result

    def process(self, text):
        return ''.join(self.encrypt_decrypt_char(char) for char in text)

def encrypt_text():
    input_text = input_entry.get()
    if not input_text:
        messagebox.showerror("Error", "Input text cannot be empty!")
        return

    rotor1_pos = int(rotor1_entry.get()) % 26
    rotor2_pos = int(rotor2_entry.get()) % 26
    rotor3_pos = int(rotor3_entry.get()) % 26

    enigma = EnigmaCipher(rotor1_pos, rotor2_pos, rotor3_pos)
    encrypted_text = enigma.process(input_text)

    output_entry.delete(0, tk.END)
    output_entry.insert(0, encrypted_text)

# GUI setup
root = tk.Tk()
root.title("Enigma Cipher")

# Input text
input_label = tk.Label(root, text="Input Text:")
input_label.grid(row=0, column=0, padx=5, pady=5)
input_entry = tk.Entry(root, width=40)
input_entry.grid(row=0, column=1, padx=5, pady=5)

# Rotor positions
rotor1_label = tk.Label(root, text="Rotor 1 Position:")
rotor1_label.grid(row=1, column=0, padx=5, pady=5)
rotor1_entry = tk.Entry(root, width=5)
rotor1_entry.grid(row=1, column=1, sticky='w', padx=5, pady=5)
rotor1_entry.insert(0, "0")

rotor2_label = tk.Label(root, text="Rotor 2 Position:")
rotor2_label.grid(row=2, column=0, padx=5, pady=5)
rotor2_entry = tk.Entry(root, width=5)
rotor2_entry.grid(row=2, column=1, sticky='w', padx=5, pady=5)
rotor2_entry.insert(0, "0")

rotor3_label = tk.Label(root, text="Rotor 3 Position:")
rotor3_label.grid(row=3, column=0, padx=5, pady=5)
rotor3_entry = tk.Entry(root, width=5)
rotor3_entry.grid(row=3, column=1, sticky='w', padx=5, pady=5)
rotor3_entry.insert(0, "0")

# Output text
output_label = tk.Label(root, text="Output Text:")
output_label.grid(row=4, column=0, padx=5, pady=5)
output_entry = tk.Entry(root, width=40)
output_entry.grid(row=4, column=1, padx=5, pady=5)

# Encrypt button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()