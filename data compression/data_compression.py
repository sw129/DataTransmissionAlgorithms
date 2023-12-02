import numpy as np

#Функция десятичной упаковки
def decimal_packing(data):
    part = 4
    HighestPart = []
    find = False

    data = SplitData(data)

    for i in range(len(data[0])):
        h = None
        for j in range(part):
            if h == None:
                h = data[j][i]
            elif h != data[j][i]:
                find  = True
                break
            elif j == part-1:
                HighestPart.append(h)
        if find:
            break
    
    newData = np.delete(data, range(len(HighestPart)), axis=1)
    print(f"        Десятичная упаковка")
    print(f"Исходные байты: \n{data}")
    print(f"Cтаршая часть: {HighestPart}")
    print(f"Конечный байты: \n{newData}")
    compression_ratio(data, newData)


#Функция относительного кодирования
def relative_encoding(data):
    data = SplitData(data)
    A = [data[0]]
    print(f"        Относительное кодирование")
    print(f"Исходные байты: \n{data}")
    print(f"опорное значение: {data[0]}")

    for i in range(1, len(data)):
        A.append(binary_subtraction(data[i], data[i-1]))
    A = AddData(A)
    print(f"Конечный байты:")
    for i in A:
        print(i)
    compression_ratio(data, A)

def compression_ratio(initial_data, data_after_compression):
    initial_amount = sum(map(len,initial_data))
    amount_after_compression = sum(map(len,data_after_compression))
    A = (initial_amount - amount_after_compression) / initial_amount * 100
    print(f"Степень сжатия: ({initial_amount}-{amount_after_compression})/{initial_amount}={A}%")


def binary_subtraction(a, b):
    # Преобразовать двоичные числа в десятичные
    a = ''.join(map(str,a))
    b = ''.join(map(str,b))

    c = int(a,2) - int(b,2) # 2

    # Преобразовать результат в двоичное число
    x = 1
    if (c > 0):
        x = 0
    
    s = ''.join(map(str,bin(c)[2+x:]))

    print(f"{a} - {b} = {x}|{s}")

    s = f"{x}" + s
    return np.array(list(map(int, s)))
    

def SplitData(data):
    part = 4
    # Дополняем входные данные нулями слева, если их длина не кратна четырем
    if len(data) % part != 0:
        data =  np.concatenate((np.repeat(0, (part - len(data) % part)), data), axis=1)
    
    return np.reshape(data, [part, -1])

def AddData(data):
    maxLen = max(map(len, data[1::]))
    s = 0
    for i in data[1::]:
        s += 1
        if len(i) < maxLen:
            pre = np.concatenate((i[:1:], np.repeat(0, (maxLen - len(i)))), axis=0)
            data[s] = np.concatenate((pre, i[1::]), axis=0)
    return data
    

def data_compression(data):
    decimal_packing(data)
    relative_encoding(data)