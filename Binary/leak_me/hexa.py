# 1 byte = 8 bit
def convert_to_big_end(x):
    to_left = (x & 0x00000000000000ff) << 56
    to_mid_left1 = (x & 0x000000000000ff00) << 40
    to_mid_left2 = (x & 0x0000000000ff0000) << 24
    to_mid_left3 = (x & 0x00000000ff000000) << 8

    to_right = (x & 0xff00000000000000) >> 56
    to_mid_right1 = (x & 0x00ff000000000000) >> 40
    to_mid_right2 = (x & 0x0000ff0000000000) >> 24
    to_mid_right3 = (x & 0x000000ff00000000) >> 8

    return to_left | to_mid_left1 | to_mid_left2 | to_mid_left3 | to_mid_right3 | to_mid_right2 | to_mid_right1 | to_right

arr = [0x6e7261656c465443, 0x5f336b316c5f317b, 0x745f74346d723066, 0x7d3030745f356734, 0xa, 0x1, 0x562295be9040, 0x7f9fb381185c, 0x7025207025207025, 0x2520702520702520, 0x2070252070252070, 0x7025207025207025, 0x2520702520702520]
for i in arr:
    # Replace x to 0 because 0x0000ff will display 0xff
    big_end = hex(convert_to_big_end(i)).replace('0x','')
    print(big_end, end="")