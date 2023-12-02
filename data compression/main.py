from WordToCode import WordToCode
from data_compression import data_compression
import numpy as np

def main():
    data = WordToCode()
    data = np.array(data)
    data_compression(data)


if __name__ == '__main__':
    main()