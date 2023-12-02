import numpy as np
import matplotlib.pyplot as plt


def draf(x, y, title):
    Y = [y[0]] + y + [y[len(y) - 1]]
    X = np.arange(len(Y))
    plt.grid(True)
    plt.step(X, Y)
    plt.xticks(X, [""] + x + [""])
    plt.yticks([0, 0.25, 0.5, 0.85, 1], ["0", "", "", "", "1"])
    plt.title(title)
    plt.show()


def draf1(x, y, title):
    Y = [y[0]] + y + [y[len(y) - 1]]
    X = np.arange(len(Y))
    plt.grid(True)
    plt.step(X, Y)
    plt.xticks(X[4 : len(X) : 4], x)
    plt.yticks([0, 0.25, 0.5, 0.85, 1], ["0", "", "", "", "1"])
    plt.title(title)
    plt.show()


# Функция для перевода строки в десятичные числа
def GetString():
    # Запрашиваем у пользователя строку на русском
    s = input("Введите строку на русском: ")
    # Кодируем строку в windows-1251
    b = s.encode("windows-1251")

    # Создаем пустой список для хранения десятичных кодов
    codes = []

    # Проходим по каждому байту в закодированной строке
    for byte in b:
        # Применяем функцию ord, чтобы получить десятичный код байта
        code = byte
        # Добавляем код в список
        codes.append(code)

    # Выводим список десятичных кодов на экран
    print("Десятичный код ASCII: ", codes)
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


# Функция для вызова отрисовки графика NRZ
def NRZ(x):
    y = []

    for item in x:
        if item == "1":
            y.append(1)
        else:
            y.append(0)
    print(y)
    draf(x, y, "NRZ")


def NRZI(x):
    y = []

    for item in x:
        if item == "1":
            y.append(0)
        else:
            y.append(1)

    print(y)
    draf(x, y, "NRZI")


def AMI(x):
    y = []
    t = True

    for item in x:
        if item == "1":
            if t:
                y.append(1)
                t = False
            else:
                y.append(0)
                t = True
        else:
            y.append(0.5)

    print(y)
    draf(x, y, "AMI")


def RZ(x):
    y = []
    for item in x:
        if item == "1":
            y.append(1)
            y.append(1)
            y.append(0.5)
            y.append(0.5)
        else:
            y.append(0)
            y.append(0)
            y.append(0.5)
            y.append(0.5)

    print(y)
    draf1(x, y, "RZ")


def manchester(x):
    y = []
    for item in x:
        if item == "1":
            y.append(0)
            y.append(0)
            y.append(1)
            y.append(1)
        else:
            y.append(1)
            y.append(1)
            y.append(0)
            y.append(0)

    print(y)
    draf1(x, y, "Манчестерский код")


li = []
for a in GetString():
    li += decimal_to_binary(a)

NRZ(li)
NRZI(li)
AMI(li)
RZ(li)
manchester(li)
