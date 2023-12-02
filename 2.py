# Функция для перевода строки в десятичные числа
def GetString():
    # Запрашиваем у пользователя строку на русском
    s = input("Введите строку на русском: ")
    # Кодируем строку в windows-1251
    b = s.encode('windows-1251')

    # Создаем пустой список для хранения десятичных кодов
    codes = []

    # Проходим по каждому байту в закодированной строке
    for byte in b:
        # Применяем функцию ord, чтобы получить десятичный код байта
        code = byte
        # Добавляем код в список
        codes.append(code)

    # Выводим список десятичных кодов на экран
    print("Буквы: ", s)
    print("Десятичный код: ", codes)
    return codes

# Функция для перевода десятичного числа в двоичное
def decimal_to_binary(decimal):
    # Инициализируем пустую строку для результата
    result = ""
    # Пока десятичное число больше нуля
    while decimal > 0:
        # Делим его на 2 и записываем остаток от деления (0 или 1) в начало результата
        result = str(decimal % 2) + result
        # Делим частное от предыдущего деления нацело на 2 и присваиваем его десятичному числу
        decimal = decimal // 2
    # Возвращаем результат
    return result

# Функция для выполнения операции логического кодирования 4B/5B
def encode_4b5b(data):
    # Словарь для хранения соответствия между 4-битными и 5-битными кодами
    code_dict = {
        "0000": "11110",
        "0001": "01001",
        "0010": "10100",
        "0011": "10101",
        "0100": "01010",
        "0101": "01011",
        "0110": "01110",
        "0111": "01111",
        "1000": "10010",
        "1001": "10011",
        "1010": "10110",
        "1011": "10111",
        "1100": "11010",
        "1101": "11011",
        "1110": "11100",
        "1111": "11101"
    }

    # Проверка, что длина входных данных кратна 4
    if len(data) % 4 != 0:
        return None
    
    result = ""
    # Цикл по каждым 4 битам входных данных
    for i in range(0, len(data), 4):
        # Извлечение 4-битного блока
        block = "".join(map(str,data[i:i+4]))
        # Поиск соответствующего 5-битного кода в словаре
        code = code_dict.get(block)
        result += code
    return result

# Функция для выполнения операции логического кодирования скремблирование
def scramble(A):
    B = []
    for i in range(len(A)):
        if len(B) > 4:
            B.append(A[i] ^ B[i-3] ^ B[i-5])
        elif len(B) > 2:
            B.append(A[i] ^ B[i-3])
        else:
            B.append(A[i])
    return B

# Функция для поиска максимальной последовательности одинаковых битов в коде
def max_sequence(code):
  # Инициализация переменных
  max_ones = 0 # Максимальное количество подряд идущих единиц
  max_zeros = 0 # Максимальное количество подряд идущих нулей
  current_ones = 0 # Текущее количество подряд идущих единиц
  current_zeros = 0 # Текущее количество подряд идущих нулей

  # Перебор всех битов в коде
  for bit in code:
    # Если бит равен 1, то увеличиваем текущее количество единиц на 1
    if bit == "1":
      current_ones += 1
      # Если текущее количество единиц больше максимального, то обновляем максимальное
      if current_ones > max_ones:
        max_ones = current_ones
      # Обнуляем текущее количество нулей, так как началась новая последовательность
      current_zeros = 0
    # Если бит равен 0, то аналогично делаем для нулей
    elif bit == "0":
      current_zeros += 1
      if current_zeros > max_zeros:
        max_zeros = current_zeros
      current_ones = 0
    # Если бит не равен ни 1, ни 0, то пропускаем его
    else:
      continue

  # Возвращаем результат в виде кортежа из двух чисел: максимальное количество единиц и нулей
  return (max_ones, max_zeros)



data = []
for item in GetString():
    data += decimal_to_binary(item)
data = list(map(int,data))

encoded = encode_4b5b(data)
print(f"Двоичный код:          {''.join(map(str,data))}")
print(f"Избыточные коды 4B/5B: {encoded}")
scrambled = scramble(data)
print(f"Cкремблирование:       {''.join(map(str,scrambled))}")

print("Двоичный код:", max_sequence(''.join(map(str,data))))
print("Избыточные коды 4B/5B:", max_sequence(encoded))
print("Скремблирование:", max_sequence(''.join(map(str,scrambled))))