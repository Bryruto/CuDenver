TITLE pa2.asm
INCLUDE Irvine32.inc
SECONDS_IN_DAY TEXTEQU <mov edx, 24 * 60 * 60>
.data
;//Part 4
    A DWORD 132d
    B DWORD 01101001b
    NotC DWORD 0AF5h; //you cant use c its a key word i believe
    D DWORD 85d
.code
    main PROC; // added a tab to all inside at the end if thats ok i just like the look
    ;//Part 1
    mov eax, 0; // this will 0 the register
    mov eax, 2d* 3d* 4d* 5d* 6d* 7d* 8d* 9d;// this will give the product
    
    ;// Part 2
    mov ebx, 0
    mov ecx, 0
    
    ;//CY carry flag unsigned
    mov ebx, 0FFFFFFFFh
    add ebx, 1h
    
    ;//OV overflow flag signed
    mov ecx, 7FFFFFFFh
    add ecx, 1h
    
    ;//Part 3
    mov edx, 0
    SECONDS_IN_DAY
    
    ;//Part 4
    mov eax, A
    sub eax, B
    mov ebx, NotC
    sub ebx, D
    add eax, ebx
    mov A,eax;// i mean its already in eax
    
    Call WriteInt
    
    exit
main ENDP
END main
