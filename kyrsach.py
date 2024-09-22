import tkinter as tk
from tkinter import ttk
import time
from tkinter import filedialog
from backend import *

# Список для хранения подробных результатов выполнения
detailed_results = []

def on_button_click(button, progress_bar, result_label, task_number):
    for btn in buttons:
        btn['state'] = 'disabled'
        
    progress_bar['value'] = 0
    result_label['text'] = ''
    window.update()

    # Симуляция выполнения задачи
    time.sleep(2)  # Замените это на вашу логику выполнения

    # Обновляем прогресс-бар
    for i in range(101):
        time.sleep(0.005)
        progress_bar['value'] = i
        window.update()
    
    for btn in buttons:
        btn['state'] = 'normal'

    # Устанавливаем текст "Выполнено" в соответствующий result_label
    result_label['text'] = "Выполнено"

    # Сохраняем подробную информацию об выполнении в список
    detailed_result = get_results(task_number)
    
    result = detailed_result.get(task_number)
    detailed_results.append(result)  # Сохраняем результат в список

def display_results():
    # Выводим сохраненные подробные результаты в текстовое поле
    output_output_textbox.delete("1.0", tk.END)  # Очищаем текстовое поле
    for result in detailed_results:
        output_output_textbox.insert(tk.END, result + "\n")

def save_results():
    results = "\n".join(detailed_results)  # Берем текст из списка
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(results)

def exit_program():
    window.destroy()  # Закрываем окно

# Создаем основное окно
window = tk.Tk()
window.title("SOC by didenko")
window.geometry("700x450")
window.resizable(False, False)

# Заголовок
title_label = tk.Label(window, text="Тестирвание безопасности ПК", font=("Arial", 16))
title_label.grid(row=0, column=0, columnspan=3, pady=10)

frame_titles = [
    "Проверка подключения к интернету                                     ",
    "Проверка наличия установленного межсетевого экрана",
    "Проверка работоспособности межсетевого экрана          ",
    "Проверка наличия установленного антивируса                 ",
    "Проверка на активность работы антивирусного ПО         ",
    "Проверка работоспособности антивирусного ПО             "
]

progress_bars = []
result_labels = []
buttons = []

# Создание строк с кнопками, прогресс-барами и метками
for i, frame_title in enumerate(frame_titles):
    frame = tk.Frame(window)
    frame.grid(row=i + 1, pady=5, sticky="ew")

    progress_bar = ttk.Progressbar(frame, length=200, mode='determinate')
    progress_bar.grid(row=0, column=1, padx=(5, 0), sticky="ew")

    result_label = tk.Label(frame, text='', width=20)
    result_label.grid(row=0, column=2, padx=(5, 0), sticky="ew")

    button = tk.Button(frame, text=frame_title, command=lambda b=progress_bar, r=result_label, f=i + 1: on_button_click(button, b, r, f))
    button.grid(row=0, column=0, padx=(5, 0), sticky="ew")

    progress_bars.append(progress_bar)
    result_labels.append(result_label)

    buttons.append(button)

# Сделать все колонки одинаковыми по размеру
for i in range(3):
    window.grid_columnconfigure(i, weight=1)

for i in range(len(frame_titles)):
    window.grid_rowconfigure(i + 1, weight=1)

# Создание кнопок и текстового поля для вывода подробной информации
button_frame = tk.Frame(window)
button_frame.grid(row=len(frame_titles) + 1, pady=10, sticky="ew")

output_output_textbox = tk.Text(window, height=6, width=50)
output_output_textbox.grid(row=len(frame_titles) + 2, column=0, columnspan=3, pady=5)

# Кнопки
result_button = tk.Button(button_frame, text="Вывести результаты", command=display_results)
result_button.grid(row=0, column=0, padx=5)

save_button = tk.Button(button_frame, text="Сохранить в файл", command=save_results)
save_button.grid(row=0, column=1, padx=5)

exit_button = tk.Button(button_frame, text="Выход", command=exit_program)
exit_button.grid(row=0, column=2, padx=5)

# Запуск основного цикла
window.mainloop()
