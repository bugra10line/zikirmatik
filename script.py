import tkinter as tk

def increment_count():
    current_count = int(counter_label["text"])
    counter_label.config(text=str(current_count + 1))

def reset_count():
    counter_label.config(text="0")

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Zikirmatik")
root.geometry("300x200")

# Sayaç etiketi
counter_label = tk.Label(root, text="0", font=("Arial", 48), fg="green")
counter_label.pack(pady=20)

# Sayacı artıran buton
increment_button = tk.Button(root, text="➕ Zikir Çek", font=("Arial", 16), bg="lightblue", command=increment_count)
increment_button.pack(fill="x", padx=20, pady=5)

# Sıfırlayan buton
reset_button = tk.Button(root, text="🔄 Sıfırla", font=("Arial", 16), bg="lightcoral", command=reset_count)
reset_button.pack(fill="x", padx=20, pady=5)

# Uygulamayı çalıştır
root.mainloop()
