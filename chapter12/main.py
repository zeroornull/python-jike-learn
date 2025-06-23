from chapter12.utils.utils import get_sum
from chapter12.utils.class_utils import *

if __name__ == '__main__':
    print(get_sum(1, 2))

    encoder = Encoder()
    decoder = Decoder()

    print(encoder.encode('abcde'))
    print(encoder.encode('edcba'))
