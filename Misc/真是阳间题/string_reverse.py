#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def reverse_string(text):
    """反转字符串"""
    return text[::-1]

def main():
    print("字符串反转工具")
    print("输入 'quit' 退出")
    
    while True:
        user_input = input("\n请输入要反转的字符串: ").strip()
        
        if user_input.lower() == 'quit':
            print("再见!")
            break
        
        if user_input:
            reversed_text = reverse_string(user_input)
            print(f"反转结果: {reversed_text}")
        else:
            print("请输入有效的字符串")

if __name__ == "__main__":
    main()
