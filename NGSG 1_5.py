import tkinter as tk
from tkinter import filedialog, messagebox

cipher_dict = {
    'A': '00101', 'B': '10011', 'C': '01000', 'D': '00111',
    'E': '11010', 'F': '11011', 'G': '01110', 'H': '10000',
    'I': '11110', 'J': '00100', 'K': '01111', 'L': '11111',
    'M': '11101', 'N': '00010', 'O': '10110', 'P': '01000',
    'Q': '00001', 'R': '01010', 'S': '11000', 'T': '11100',
    'U': '00011', 'V': '01100', 'W': '01011', 'X': '01111',
    'Y': '00110', 'Z': '00000', ' ': ';', '\n': ']', '\t': '[;]'
}

decipher_dict = {v: k for k, v in cipher_dict.items()}

def text_to_cipher(text):
    cipher_text = ""
    for char in text.upper():
        cipher_text += cipher_dict.get(char, '')  # игнорируем символы, которых нет в словаре
    return cipher_text

def cipher_to_text(cipher, case_option):
    text = ""
    i = 0
    while i < len(cipher):
        if cipher[i:i+4] == '[;]':
            text += decipher_dict['[;]']
            i += 4
        elif cipher[i] == ']':
            text += decipher_dict[']']
            i += 1
        elif cipher[i] == ';':
            text += decipher_dict[';']
            i += 1
        else:
            text += decipher_dict.get(cipher[i:i+5], '')
            i += 5

    if case_option == 'lower':
        return text.lower()
    else:
        return text.upper()

def save_to_ngsg(filename, text):
    with open(filename, 'w') as file:
        file.write(text)

def load_from_ngsg(filename):
    with open(filename, 'r') as file:
        return file.read()

def encrypt_text():
    input_text = text_entry.get("1.5", tk.END)
    cipher_text = text_to_cipher(input_text)
    
    file_path = filedialog.asksaveasfilename(defaultextension=".ngsg", filetypes=[("NGSG files", "*.ngsg")])
    if file_path:
        save_to_ngsg(file_path, cipher_text)
        messagebox.showinfo("Успех", f"Шифрованный текст сохранен в файл:\n{file_path}")

def decrypt_text():
    file_path = filedialog.askopenfilename(filetypes=[("NGSG files", "*.ngsg")])
    if file_path:
        case_option = case_var.get()
        cipher_text = load_from_ngsg(file_path)
        decrypted_text = cipher_to_text(cipher_text, case_option)
        result_entry.delete("1.0", tk.END)
        result_entry.insert(tk.END, decrypted_text)
        messagebox.showinfo("Успех", "Текст успешно расшифрован!")

app = tk.Tk()
app.title("Шифратор и Дешифратор")

frame = tk.Frame(app, padx=10, pady=10)
frame.pack(padx=10, pady=10)

text_label = tk.Label(frame, text="Введите текст для шифрования:")
text_label.pack()

text_entry = tk.Text(frame, height=10, width=50, font=("Helvetica", 12))
text_entry.pack(pady=5)

encrypt_button = tk.Button(frame, text="Шифровать и сохранить", command=encrypt_text, bg="lightblue", fg="black", font=("Helvetica", 12))
encrypt_button.pack(pady=10)

load_button = tk.Button(frame, text="Загрузить и дешифровать", command=decrypt_text, bg="lightgreen", fg="black", font=("Helvetica", 12))
load_button.pack(pady=10)

case_var = tk.StringVar(value='upper')
case_frame = tk.Frame(frame)
case_frame.pack(pady=5)
case_upper_radio = tk.Radiobutton(case_frame, text="Заглавные буквы", variable=case_var, value='upper', font=("Helvetica", 12))
case_upper_radio.pack(side=tk.LEFT, padx=5)
case_lower_radio = tk.Radiobutton(case_frame, text="Строчные буквы", variable=case_var, value='lower', font=("Helvetica", 12))
case_lower_radio.pack(side=tk.LEFT, padx=5)

result_label = tk.Label(frame, text="Расшифрованный текст:")
result_label.pack()

result_entry = tk.Text(frame, height=10, width=50, font=("Helvetica", 12))
result_entry.pack(pady=5)

app.mainloop()
