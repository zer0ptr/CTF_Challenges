#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            decrypted = chr((ord(char) - base - shift + 26) % 26 + base)
            result += decrypted
        else:
            result += char
    return result

def main():
    while True:
        encrypted_text = input("\n请输入要解密的文本: ").strip()
        
        if encrypted_text.lower() == 'quit':
            print("Bye!")
            break
        
        if encrypted_text:
            print("\n所有偏移量的解密结果:")
            for shift in range(1, 26):
                decrypted = caesar_decrypt(encrypted_text, shift)
                print(f"偏移量 {shift:2d}: {decrypted}")
        else:
            print("请输入有效的文本")

if __name__ == "__main__":
    main()