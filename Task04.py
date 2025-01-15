from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_file(file_name, key):
    cipher = AES.new(key, AES.MODE_EAX)
    with open(file_name, 'rb') as f:
        data = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(data)
    with open(file_name + ".enc", 'wb') as f:
        for x in (cipher.nonce, tag, ciphertext):
            f.write(x)

def decrypt_file(file_name, key):
    with open(file_name, 'rb') as f:
        nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    with open(file_name[:-4], 'wb') as f:
        f.write(data)

key = get_random_bytes(32)  



import tkinter as tk
from tkinter import filedialog, messagebox

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_label.config(text=file_path)

def encrypt():
    file_path = file_label.cget("text")
    if file_path:
        try:
            encrypt_file(file_path, key)
            messagebox.showinfo("Success", "File encrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def decrypt():
    file_path = file_label.cget("text")
    if file_path:
        try:
            decrypt_file(file_path, key)
            messagebox.showinfo("Success", "File decrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("File Encryption Tool")

file_label = tk.Label(root, text="No file selected")
file_label.pack()

select_button = tk.Button(root, text="Select File", command=select_file)
select_button.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.pack()

root.mainloop()

