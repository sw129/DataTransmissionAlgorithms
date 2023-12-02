import numpy as np
from WordToCode import WordToCode as WtoC

def SplitData(data, part=4):
    return np.reshape(data, [part, -1])

# Контроль по паритету
def  Parity_control(data):
    print(f"\nКонтроль по паритету")
    checksum = data[0]
    for i in range(1, len(data)):
        print(f"{checksum} ⊕  {data[i]} = {checksum ^ data[i]}")
        checksum = checksum ^ data[i]
    print(f"Контрольная сумма: {checksum}")


# Вертикальный и горизонтальный контроль по паритету
def VH_parity_control(data):
    data = SplitData(data)
    i = len(data)-1
    j = len(data[0])-1
    print(f"\nВертикальный и горизонтальный контроль по паритету")
    print(f"Матрица:\n{data}")
    print(f"Контрольная сумма: {data[i,:]} {data[:, j]}")

def crc_remainder(input_bitstring, polynomial_bitstring, initial_filler):
    print("\nЦиклический избыточный контроль")
    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    len_input = len(input_bitstring)
    initial_padding = (len(polynomial_bitstring) - 1) * initial_filler
    input_padded_array = list(input_bitstring + list(initial_padding))
    print(f"Делитель: {polynomial_bitstring}")
    print(f"Начальная строка и дополнительные нули:{''.join(input_bitstring)} | {''.join(initial_padding)}")
    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index('1')
        #print("Текущий сдвиг:", cur_shift)
        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] \
            = str(int(polynomial_bitstring[i] != input_padded_array[cur_shift + i]))
        print("Результат деления:", ''.join(input_padded_array[input_padded_array.index('1'):]))
    
    return ''.join(input_padded_array)[len_input:]


code = WtoC()
Parity_control(code)
VH_parity_control(code)
crc = crc_remainder(list(map(str,code)), "10101011111111111", "0")
print(f"\nКонтрольная сумма: {crc}")
