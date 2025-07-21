// gcc test.c -no-pie -fno-stack-protector -g
#include <stdio.h>

void func1() { printf("func1 called\n"); }

void func2() { printf("func2 called\n"); }

void func3() { printf("func3 called\n"); }

int main() {
    char str[0x20];

    read(0, str, 0x50);

    return 0;
}