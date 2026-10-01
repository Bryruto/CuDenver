TITLE pa2.asm
INCLUDE Irvine32.inc

.data
    myArray WORD 5767h,2132h,4798h 
    arrayCount = ($ - myArray) / 2 ;2bytes = word
.code 

main PROC
    ;this was my first try 10 seconds 
    ;mov ax, [myArray] ; ax = 5767h
    ;mov bx, [myArray + 2] ; bx = 2132h
    ;mov cx, [myArray + 4] ; cx = 4798h

    ;mov [myArray], bx
    ;mov [myArray + 2], cx
    ;mov [myArray + 4], ax

    ;but this is better 
    mov ax, [myArray]; ax = 5767h
    xchg ax, [myArray + 4]; ax = 4798h 
    xchg ax, [myArray + 2]; ax = 2132h
    mov [myArray],ax ;myArray = 2132h 
    

    mov esi, OFFSET myArray
    mov ecx, arrayCount
    mov ebx, sizeof [myArray]

    call DumpMem
    exit

main ENDP
END main
