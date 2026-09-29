def caesar(text, k):
    result = ""
    for ch in text:
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        else:
            result += ch          
    return result
def encrypt(text, k):
    return caesar(text, k)
def decrypt(text, k):
    return caesar(text, -k)
def main():
    print("1. Ma hoa (EN)")
    print("2. Giai ma (DE)")
    choice = input("Chon (1/2): ")
    in_name = input("Ten file dau vao (vd: input.txt): ")
    out_name = input("Ten file dau ra (vd: output.txt): ")
    k = int(input("Nhap khoa k (so nguyen): "))
    with open(in_name, "r", encoding="utf-8") as f:
        data = f.read()
    if choice == "1":
        result = encrypt(data, k)
    else:
        result = decrypt(data, k)
    with open(out_name, "w", encoding="utf-8") as f:
        f.write(result)
    print("Ket qua:")
    print(result)
    print("Da ghi vao file", out_name)
main()


def vigenere(text, key, direction):
    shifts = [ord(c) - ord('A') for c in key.upper() if 'A' <= c.upper() <= 'Z']
    if len(shifts) == 0:
        print("Khoa phai co it nhat 1 chu cai A-Z!")
        return text
    result = ""
    i = 0                         
    for ch in text:
        if 'A' <= ch <= 'Z':
            base = ord('A')
        elif 'a' <= ch <= 'z':
            base = ord('a')
        else:
            result += ch           
            continue
        k = shifts[i % len(shifts)] * direction
        result += chr((ord(ch) - base + k) % 26 + base)
        i += 1
    return result
def encrypt(text, key):
    return vigenere(text, key, 1)
def decrypt(text, key):
    return vigenere(text, key, -1)
def main():
    print("1. Ma hoa (EN)")
    print("2. Giai ma (DE)")
    choice = input("Chon (1/2): ")
    in_name = input("Ten file dau vao (vd: input.txt): ")
    out_name = input("Ten file dau ra (vd: output.txt): ")
    key = input("Nhap khoa (chu cai A-Z): ")
    with open(in_name, "r", encoding="utf-8") as f:
        data = f.read()
    if choice == "1":
        result = encrypt(data, key)
    else:
        result = decrypt(data, key)
    with open(out_name, "w", encoding="utf-8") as f:
        f.write(result)
    print("Ket qua:")
    print(result)
    print("Da ghi vao file", out_name)
main()
