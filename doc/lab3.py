import serial  # Импорт модуля для работы с последовательными портами
import time  # Импорт модуля для работы с задержками
import serial.tools.list_ports  # Импорт инструмента для поиска доступных COM-портов

# Список возможных скоростей передачи данных
speeds = ['1200', '2400', '4800', '9600', '19200', '38400', '57600', '115200']

# Получаем список доступных COM-портов
ports = [p.device for p in serial.tools.list_ports.comports()]

# Выбираем первый найденный порт
port_name = ports[0]

# Устанавливаем максимальную скорость передачи данных
port_speed = int(speeds[-1])

# Таймаут соединения в секундах
port_timeout = 10

# Открываем соединение с устройством через COM-порт
ard = serial.Serial(port_name, port_speed, timeout=port_timeout)

# Даем устройству время на инициализацию
time.sleep(1)

# Очищаем входной буфер
ard.flushInput()

try:
    # Считываем данные из буфера устройства
    msg_bin = ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())

    # Декодируем бинарные данные в строку
    msg_str_ = msg_bin.decode()

    # Выводим количество считанных байт
    print(len(msg_bin))
except Exception as e:
    # В случае ошибки выводим сообщение
    print('Error!')

# Закрываем соединение с устройством
ard.close()

# Даем устройству время на завершение работы
time.sleep(1)

# Выводим полученное сообщение
print(msg_str_)

