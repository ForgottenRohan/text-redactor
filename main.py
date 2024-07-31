import tkinter as tk
from tkinter import filedialog, messagebox
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
    if not file_path:
        return
    else:
        try:
            with open(file_path, 'w') as file:
                file.write(text.get('1.0', tk.END))
            messagebox.showinfo('Success', 'File saved')
        except Exception as e:
            messagebox.showerror('Error', f'File not saved: {e}')

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not file_path:
        return
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            text.delete("1.0", tk.END)  # Очистить текущее содержимое
            text.insert("1.0", content)  # Вставить содержимое из файла
        messagebox.showinfo("Success", "File opened successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open file:\n{e}")



root = tk.Tk()
root.title('Text Redactor by Dim')
text = tk.Text(root, wrap='word', width=50, height=20)
text.pack(padx=10, pady=10)
frame = tk.Frame(root)
frame.pack(pady=5)
save_button = tk.Button(frame, text='Save', command=save_file)
save_button.pack(side='left', padx=5)

open_button = tk.Button(frame, text='Open', command=open_file)
open_button.pack(side='right', padx=5)

if __name__ == '__main__':
    root.mainloop()
