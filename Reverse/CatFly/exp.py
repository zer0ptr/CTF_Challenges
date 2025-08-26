dword_E1E8 = 0x1106
dword_E120 = [
    0x27fb, 0x27a4, 0x464e, 0x0e36, 0x7b70, 0x5e7a, 0x1a4a, 0x45c1,
    0x2bdf, 0x23bd, 0x3a15, 0x5b83, 0x1e15, 0x5367, 0x50b8, 0x20ca,
    0x41f5, 0x57d1, 0x7750, 0x2adf, 0x11f8, 0x09bb, 0x5724, 0x7374,
    0x3ce6, 0x646e, 0x010c, 0x6e10, 0x64f4, 0x3263, 0x3137, 0x00b8,
    0x229c, 0x7bcd, 0x73bd, 0x480c, 0x14db, 0x68b9, 0x5c8a, 0x1b61,
    0x6c59, 0x5707, 0x09e6, 0x1fb9, 0x2ad3, 0x76d4, 0x3113, 0x7c7e,
    0x11e0, 0x6c70
]
 
 
def sub_62B5():
    global dword_E1E8
    dword_E1E8 = (1103515245 * dword_E1E8 + 12345) & 0xFFFFFFFF
    return (dword_E1E8 >> 10) & 0x7FFF
 
 
def llog(n):
    a = 0
    while n >= 10:
        n //= 10
        a += 1
    return a
 
 
def sub_62E3(a1):
    return 0x7E >= (a1 & 0x7F) > 0x20
 
 
count = 0
while True:
    for i in range(50):
        dword_E120[i] ^= sub_62B5()
 
    count += 1
    dword_E1E8 += 42 + llog(count)
 
    if count % 1000000 == 0:
        print(f"Count: {count}")
 
    flag = bytearray(51)
    for i in range(50):
        if not sub_62E3(dword_E120[i]):
            break
        flag[i] = dword_E120[i] & 0xFF
    else:
        continue
 
    if flag[:6] == b'CatCTF':
        print(flag.decode())
        print(f"Count: {count}")
        break