import numpy as np

def compression_ratio(initial_data, data_after_compression):
    data_after_compression = data_after_compression.replace("Ctrl", "C")
    initial_amount = sum(map(len,initial_data))
    amount_after_compression = sum(map(len,data_after_compression))
    A = (initial_amount - amount_after_compression) / initial_amount * 100
    print(f"Степень сжатия: ({initial_amount}-{amount_after_compression})/{initial_amount}={A}%")

def GenImage():
    # Создаем список допустимых символов
    symbols = ['00000000', '11111111']
    # Создаем список
    li = []
    print("Рисунок 10x10:")
    print("____________"*7)  
    for x in np.random.choice(symbols, size=(10, 10)):
      x = ''.join(map(str, x))
      print(f"|{x}|")
      li.append(x)
    print("¯¯¯¯¯¯¯¯¯¯¯¯"*7) 
    return li

def AddCompressed(count, image_bytes):
    if count > 3:
        # Добавить к сжатому результату предыдущий байт и его количество повторений (если оно больше единицы)
        return "Ctrl" + image_bytes + str(count)
    else:
        return image_bytes * count

# Функция для компрессии рисунка методом символного подавления
def compress_image(image):
   image_bytes = ''.join(image)
   print(f"Cтрока: {image_bytes}")
   
   compressed = ""
   count = 1
   for i in range(1, len(image_bytes)):
        if image_bytes[i] == image_bytes[i-1]:
            count += 1
        else:
            compressed += AddCompressed(count, image_bytes[i-1])
            # Сбросить счетчик повторений на единицу
            count = 1
   
   compressed += AddCompressed(count, image_bytes[i-1])
   print(f"Строка после сжатия: {compressed}")
   compression_ratio(image_bytes, compressed)
   return compressed
        
   
compress_image(GenImage())

