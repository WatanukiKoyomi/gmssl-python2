import base64
import math
import struct
from decimal import Decimal, ROUND_UP

from gmssl import sm3, func

if __name__ == '__main__':
    y = sm3.sm3_hash(func.bytes_to_list("abc"))
    print y
