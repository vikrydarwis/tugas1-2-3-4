import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# Function to encode the message into the image
def encode_message():
    try:
        # Open the image file
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg")])
        if not file_path:
            return

        image = Image.open(file_path)
        message = text_message.get("1.0", tk.END).strip()

        if not message:
            messagebox.showerror("Error", "Message cannot be empty!")
            return

        binary_message = ''.join([format(ord(char), '08b') for char in message]) + '00000000'
        pixels = list(image.getdata())

        if len(binary_message) > len(pixels) * 3:
            messagebox.showerror("Error", "Message is too long for the image!")
            return

        encoded_pixels = []
        binary_index = 0

        for pixel in pixels:
            if binary_index < len(binary_message):
                r = pixel[0] & ~1 | int(binary_message[binary_index])
                binary_index += 1
                g = pixel[1] & ~1 | int(binary_message[binary_index]) if binary_index < len(binary_message) else pixel[1]
                binary_index += 1
                b = pixel[2] & ~1 | int(binary_message[binary_index]) if binary_index < len(binary_message) else pixel[2]
                binary_index += 1
                encoded_pixels.append((r, g, b))
            else:
                encoded_pixels.append(pixel)

        encoded_image = Image.new(image.mode, image.size)
        encoded_image.putdata(encoded_pixels)

        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if save_path:
            encoded_image.save(save_path)
            messagebox.showinfo("Success", "Message encoded and image saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to decode the message from the image
def decode_message():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg")])
        if not file_path:
            return

        image = Image.open(file_path)
        pixels = list(image.getdata())

        binary_message = ""
        for pixel in pixels:
            binary_message += str(pixel[0] & 1)
            binary_message += str(pixel[1] & 1)
            binary_message += str(pixel[2] & 1)

        decoded_message = "".join([chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8)])
        decoded_message = decoded_message.split("\x00")[0]

        text_message.delete("1.0", tk.END)
        text_message.insert("1.0", decoded_message)
        messagebox.showinfo("Success", "Message decoded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Steganography Tool")
root.geometry("600x400")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill=tk.BOTH, expand=True)

label_message = tk.Label(frame, text="Enter your message:")
label_message.pack(anchor=tk.W)

text_message = tk.Text(frame, height=10)
text_message.pack(fill=tk.BOTH, expand=True)

button_encode = tk.Button(frame, text="Encode Message", command=encode_message, bg="lightblue")
button_encode.pack(fill=tk.X, pady=5)

button_decode = tk.Button(frame, text="Decode Message", command=decode_message, bg="lightgreen")
button_decode.pack(fill=tk.X, pady=5)

button_exit = tk.Button(frame, text="Exit", command=root.quit, bg="red", fg="white")
button_exit.pack(fill=tk.X, pady=5)

root.mainloop()
