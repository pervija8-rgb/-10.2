import tkinter as tk
import math

def calculate():
    # 1. Забираємо текст із полів вводу і перетворюємо на числа з крапкою (float)
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())
    
    # 2. Щоб знайти радіус і висоту, нам спочатку треба знайти площу трикутника.
    # Для цього використовуємо формулу Герона.
    # Спочатку рахуємо півпериметр (p):
    p = (a + b + c) / 2
    
    # Тепер саму площу (S) через корінь (math.sqrt):
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    
    # 3. Рахуємо те, що вимагає 15 варіант:
    # Радіус вписаного кола (r = S / p)
    r = S / p
    # Висота, проведена до сторони b (h_b = 2 * S / b)
    h_b = (2 * S) / b
    
    # 4. Виводимо готові відповіді на екран (округлюємо до 2 знаків після коми)
    label_res_r.configure(text=f"Радіус вписаного кола (r): {r:.2f}")
    label_res_h.configure(text=f"Висота до сторони b (h_b): {h_b:.2f}")

# Створюємо головне віконце
root = tk.Tk()
root.title("Трикутник - Варіант 15")
root.geometry("350x300") # Робимо вікно трохи вищим, щоб все влізло

# --- Розставляємо елементи через place(x, y) ---
# x - це відступ зліва, y - це відступ зверху.

# Сторона A
label_a = tk.Label(root, text="Сторона a (см):")
label_a.place(x=20, y=20)
entry_a = tk.Entry(root, width=10)
entry_a.place(x=150, y=20)
entry_a.insert(0, "17.8") # Значення з таблиці для 15 варіанту

# Сторона B
label_b = tk.Label(root, text="Сторона b (см):")
label_b.place(x=20, y=60)
entry_b = tk.Entry(root, width=10)
entry_b.place(x=150, y=60)
entry_b.insert(0, "20.5")

# Сторона C
label_c = tk.Label(root, text="Сторона c (см):")
label_c.place(x=20, y=100)
entry_c = tk.Entry(root, width=10)
entry_c.place(x=150, y=100)
entry_c.insert(0, "11.6")

# Кнопка для розрахунку
btn_calc = tk.Button(root, text="Обчислити", command=calculate)
btn_calc.place(x=120, y=150)

# Місця для виведення результатів
label_res_r = tk.Label(root, text="Радіус вписаного кола (r): ")
label_res_r.place(x=20, y=200)

label_res_h = tk.Label(root, text="Висота до сторони b (h_b): ")
label_res_h.place(x=20, y=240)

# Запускаємо програму
root.mainloop()
