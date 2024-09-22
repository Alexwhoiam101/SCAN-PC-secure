import os
import subprocess
import socket
import psutil
import time

detailed_result = {
    1: "Тест 1: ",
    2: "Тест 2: ",
    3: "Тест 3: ",
    4: "Тест 4: ",
    5: "Тест 5: ",
    6: "Тест 6: "
}

def get_results(task_number):
    functions = {
        1: checking_internet_connection,
        2: checking_for_the_presence_of_an_installed_firewall,
        3: checking_for_the_operability_of_the_firewall,
        4: checking_for_the_presence_of_an_installed_antivirus,
        5: checking_for_antivirus_software_activity,
        6: checking_for_the_operability_of_antivirus_software
        }
    
    func = functions.get(task_number)  # Получаем функцию по номеру задачи
    if func:  # Проверяем, существует ли функция
        func()  # Вызываем функцию
    return detailed_result

def checking_internet_connection():
    # Проверяем интернет соединение с помощью ping
    try:
        output = subprocess.check_output("ping -n 1 google.com", shell=True)
        detailed_result[1] += "Интернет-соединение установлено."
    except subprocess.CalledProcessError:
        detailed_result[1] += "Интернет-соединение отсутствует."

def checking_for_the_presence_of_an_installed_firewall():
    antivirus_files = [
        "C:\Program Files (x86)\InfoTeCS\ViPNet Client\Monitor.exe"
    ]
    
    if any(os.path.exists(file) for file in antivirus_files):
         detailed_result[2] += "Фаервол установлен."
    else:
         detailed_result[2] += "Фаервол не установлен."

def checking_for_the_operability_of_the_firewall():
    # Проверка работоспособности фаервола
    # Проверим доступ к известному запрещенному ресурсу
    server_address = "https://superuser.com/"  # Здесь должен быть запрещенный ресурс
    try:
        s = socket.socket()
        s.connect((socket.gethostbyname(server_address), 80))  # Попытка соединения
        detailed_result[3] += "Фаервол не блокирует доступ, возможно, он не работает."
    except socket.error:
        detailed_result[3] += "Фаервол работает исправно."

def checking_for_the_presence_of_an_installed_antivirus():
    # Проверка наличия файлов антивируса
    antivirus_files = [
        "antivirus_test.exe",
        "C:\Program Files\Windows Defender\MsMpEng.exe"
    ]
    
    if any(os.path.exists(file) for file in antivirus_files):
        detailed_result[4] += "Антивирус установлен."
    else:
        detailed_result[4] += "Антивирус не установлен, пожалуйста, установите."

def checking_for_the_operability_of_antivirus_software():
    # Проверка работоспособности антивирусного ПО через файл EICAR 
    eicar_test_file = "EICAR_test_file.txt"
    eicar_test_string = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
    with open(eicar_test_file, 'w') as file:
        file.write(eicar_test_string)
    
    try:
        with open(eicar_test_file, "r") as file:
            content = file.read()
    except:
        pass
    
    time.sleep(15) 
    
    if os.path.isfile(eicar_test_file) == False:
        detailed_result[6] += "Антивирус работает исправно."
    else:
        detailed_result[6] += "Антивирус не работает"

def checking_for_antivirus_software_activity():
    # Проверка процессов
    defender_processes = ['MsMpEng.exe', 'MpCmdRun.exe', 'MsMpEng.exe']

    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            # Проверяем, если один из процессов Windows Defender запущен
            if process.info['name'] in defender_processes:
                detailed_result[5] += f"Запущен процесс: {process.info['name']} (PID: {process.info['pid']})"
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Проверка службы Windows Defender
    try:
        output = subprocess.check_output('sc query Windefend', shell=True, universal_newlines=True)
        if "RUNNING" in output:
            detailed_result[5] += "Служба Windows Defender запущена."
        else:
            detailed_result[5] += "Служба Windows Defender не запущена."
    except subprocess.CalledProcessError as e:
        detailed_result[5] += f"Ошибка при выполнении команды: {str(e)}"
     

'''
# Вызываем проверки
for i in range(1, 6):
    get_results(i)

# Печатаем результаты
for key, value in detailed_result.items():
    print(value)
'''