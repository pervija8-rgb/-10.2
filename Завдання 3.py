import tkinter as tk

def calculate():
    # 1. Забираємо число x з поля вводу
    x = float(entry_x.get())
    
    # Створюємо скарбничку для нашої суми, спочатку там 0
    total_sum = 0
    
    # 2. Робимо цикл. Завдання каже, що k йде від 6 до 11.
    # В Python у range() останнє число не включається, тому пишемо 12.
    for k in range(6, 12):
        # Рахуємо шматочок формули для поточного k
        # x**k означає x у степені k
        term = (x**k) / (k**3 + x**(k+2))
        
        # Додаємо цей шматочок до нашої спільної суми
        total_sum += term
        
    # 3. Виводимо готову відповідь на екран (округлюємо до 4 знаків)
    label_res.configure(text=f"Результат суми: {total_sum:.4f}")

# Створюємо головне віконце
root = tk.Tk()
root.title("Сума - Варіант 15")
root.geometry("300x150")

# --- Розставляємо елементи через grid() ---

# Напис і поле для введення ікса
label_x = tk.Label(root, text="Введіть x:")
label_x.grid(row=0, column=0, padx=10, pady=15)

entry_x = tk.Entry(root, width=15)
entry_x.grid(row=0, column=1, padx=10, pady=15)
entry_x.insert(0, "2") # Підставив 2 для швидкої перевірки

# Кнопка, яка запускає підрахунок
btn_calc = tk.Button(root, text="Обчислити суму", command=calculate)
btn_calc.grid(row=1, column=0, columnspan=2, pady=5)

# Місце для виведення результату
label_res = tk.Label(root, text="Результат суми: ")
label_res.grid(row=2, column=0, columnspan=2, pady=10)

# Запускаємо програму
root.mainloop()
