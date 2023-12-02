# Функция для подсчета частоты символов в строке
def count_freq(string):
    # Создаем пустой словарь для хранения частот
    freq = {}
    # Проходим по каждому символу в строке
    for char in string:
        # Если символ уже есть в словаре, увеличиваем его частоту на 1
        if char in freq:
            freq[char] += 1
        # Иначе добавляем его в словарь с частотой 1
        else:
            freq[char] = 1
    # Возвращаем словарь частот
    return freq

# Функция для разделения списка символов на две части с примерно равными суммарными частотами
def split_list(symbols):
    # Создаем два пустых списка для хранения двух частей
    part1 = []
    part2 = []
    # Создаем переменную для хранения текущей суммы частот
    total = 0
    # Проходим по каждому символу в списке
    for symbol in symbols:
        # Добавляем символ в первый список
        part1.append(symbol)
        # Увеличиваем текущую сумму на частоту символа
        total += symbol[1]
        # Если текущая сумма больше или равна половине общей суммы частот, останавливаем цикл
        if total >= sum(freq for _, freq in symbols) / 2:
            break
    # Добавляем оставшиеся символы во второй список
    part2 = symbols[len(part1):]
    # Возвращаем два списка
    return part1, part2

# Функция для присвоения кодов Шеннона-Фано для каждого символа в списке
def assign_codes(symbols, code, parent, countTab):
    # Создаем пустой словарь для хранения кодов
    codes = {}
    tab = "    "*countTab
    
    # Если список содержит только один символ, добавляем его в словарь с текущим кодом
    if len(symbols) == 1:
        codes[symbols[0][0]] = code
        return codes
    
    # Иначе разделяем список на две части с примерно одинаковыми суммарными частотами
    print(f"{tab}Делим список {parent} на две части")
    part1, part2 = split_list(symbols)
    
    # Присваиваем первой части код «0» и рекурсивно вызываем функцию для нее
    print(f"{tab}Часть 1: {part1} |0")
    codes.update(assign_codes(part1, code + "0", parent + "1.", countTab+1))
    
    # Присваиваем второй части код «1» и рекурсивно вызываем функцию для нее
    print(f"{tab}Часть 2: {part2} |1")
    codes.update(assign_codes(part2, code + "1", parent + "2.", countTab+1))
    # Возвращаем словарь кодов
    return codes

def compression_ratio(initial_data, data_after_compression):
    initial_amount = sum(map(len,initial_data))*8
    amount_after_compression = sum(map(len,data_after_compression))
    A = (initial_amount - amount_after_compression) / initial_amount * 100
    print(f"Степень сжатия: ({initial_amount}-{amount_after_compression})/{initial_amount}={A}%")

# Функция для кодирования строки по алгоритму Шеннона-Фано
def shannon_fano_encode(string):
    print(f"Строка: {string}")
    # Подсчитываем частоту символов в строке
    freq = count_freq(string)
    symbols = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print(f"Частота символов в строке: {symbols}")
    
    # Присваиваем коды Шеннона-Фано для каждого символа в списке
    codes = assign_codes(symbols, "", "", 0)
    print(f"Коды : {codes}")
    
    result = ""
    # Проходим по каждому символу во входной строке
    for char in string:
        # Добавляем его код в результат
        result += codes[char]
    
    print(f"Сжатая строка: {result}")
    compression_ratio(string, result)

    return result

shannon_fano_encode("Строка")
