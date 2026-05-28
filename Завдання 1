import tkinter as tk
import math

def calculate():
    # Беремо текст, який ми ввели у віконця, і робимо з нього числа (float)
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())
    
    # Рахуємо нашу формулу. 
    # math.tan(c) - це тангенс c
    # math.sqrt(...) - це квадратний корінь
    f = math.tan(c) - math.sqrt(c / b + a)
    
    # Виводимо готовий результат у наш текстовий напис знизу
    label_result.configure(text=f"Результат: f = {f:.4f}")

# 1. Робимо головне віконце
root = tk.Tk()
root.title("Варіант 15")
root.geometry("350x250")

# 2. Розставляємо елементи як у табличці (через grid)

# Напис із формулою на самому верху
label_title = tk.Label(root, text="Обчислення: f = tg(c) - √(c/b + a)")
label_title.grid(row=0, column=0, columnspan=2, pady=10)

# Рядочок для змінної A
tk.Label(root, text="Введіть a:").grid(row=1, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=1, column=1)
entry_a.insert(0, "4")  # Одразу вписуємо сюди 4, щоб не вводити вручну

# Рядочок для змінної B
tk.Label(root, text="Введіть b:").grid(row=2, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=2, column=1)
entry_b.insert(0, "3.2")  # Вписуємо 3.2

# Рядочок для змінної C
tk.Label(root, text="Введіть c:").grid(row=3, column=0)
entry_c = tk.Entry(root)
entry_c.grid(row=3, column=1)
entry_c.insert(0, "0.1")  # Вписуємо 0.1

# Кнопочка, яка запускає наші підрахунки
btn_calc = tk.Button(root, text="Обчислити", command=calculate)
btn_calc.grid(row=4, column=0, columnspan=2, pady=10)

# Місце, де з'явиться відповідь
label_result = tk.Label(root, text="Результат: f = ")
label_result.grid(row=5, column=0, columnspan=2)

# Запускаємо віконце, щоб воно не закривалося
root.mainloop()
