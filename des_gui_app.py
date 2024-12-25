import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import DES
import base64

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt(plain_text, key):
    des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted_text = des.encrypt(padded_text.encode('utf-8'))
    return base64.b64encode(encrypted_text).decode('utf-8')

def decrypt(encrypted_text, key):
    des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    decoded_encrypted_text = base64.b64decode(encrypted_text)
    decrypted_text = des.decrypt(decoded_encrypted_text).decode('utf-8')
    return decrypted_text.rstrip()

def perform_encryption():
    plain_text = plain_text_entry.get("1.0", tk.END).strip()
    key = key_entry.get().strip()

    if len(key) != 8:
        messagebox.showerror("Error", "Key must be exactly 8 characters long!")
        return

    try:
        encrypted_text = encrypt(plain_text, key)
        encrypted_text_entry.delete("1.0", tk.END)
        encrypted_text_entry.insert(tk.END, encrypted_text)
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {e}")

def perform_decryption():
    encrypted_text = encrypted_text_entry.get("1.0", tk.END).strip()
    key = key_entry.get().strip()

    if len(key) != 8:
        messagebox.showerror("Error", "Key must be exactly 8 characters long!")
        return

    try:
        decrypted_text = decrypt(encrypted_text, key)
        decrypted_text_entry.delete("1.0", tk.END)
        decrypted_text_entry.insert(tk.END, decrypted_text)
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")

# GUI setup
root = tk.Tk()
root.title("DES Encryption and Decryption")

# Plain Text Input
plain_text_label = tk.Label(root, text="Plain Text:")
plain_text_label.grid(row=0, column=0, sticky="w")
plain_text_entry = tk.Text(root, height=5, width=40)
plain_text_entry.grid(row=0, column=1, padx=10, pady=5)

# Key Input
key_label = tk.Label(root, text="Key (8 characters):")
key_label.grid(row=1, column=0, sticky="w")
key_entry = tk.Entry(root, width=20)
key_entry.grid(row=1, column=1, padx=10, pady=5)

# Encrypted Text Output
encrypted_text_label = tk.Label(root, text="Encrypted Text:")
encrypted_text_label.grid(row=2, column=0, sticky="w")
encrypted_text_entry = tk.Text(root, height=5, width=40)
encrypted_text_entry.grid(row=2, column=1, padx=10, pady=5)

# Decrypted Text Output
decrypted_text_label = tk.Label(root, text="Decrypted Text:")
decrypted_text_label.grid(row=3, column=0, sticky="w")
decrypted_text_entry = tk.Text(root, height=5, width=40)
decrypted_text_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons
encrypt_button = tk.Button(root, text="Encrypt", command=perform_encryption)
encrypt_button.grid(row=4, column=0, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=perform_decryption)
decrypt_button.grid(row=4, column=1, pady=10)

root.mainloop()
