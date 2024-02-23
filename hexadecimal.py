def hexadecimal(dec_number: int):
    alphabet = [str(i) for i in range(1, 10)] + [chr(c) for c in range(ord('A'), ord('F') + 1)]

    if dec_number == 0:
        return '0'

    if dec_number < 16:
        return alphabet[dec_number - 1]

    else:
        return hexadecimal(dec_number // 16) + hexadecimal(dec_number % 16)
