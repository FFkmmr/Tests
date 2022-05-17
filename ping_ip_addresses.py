import platform    # Для того чтобы получить имя платформы (ОС)

import subprocess  # Для выполнения команд
def ping(host):
# Кол-во пакетов
    param = '-n' if platform.system().lower() =='windows' else '-c'
# Сама команда "ping -c 1 host"
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0

# Используем функцию так

ping('google.com')