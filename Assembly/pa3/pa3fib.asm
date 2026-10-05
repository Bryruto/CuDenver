TITLE pa2.asm
INCLUDE Irvine32.inc

.data
fibArray DWORD 0, 1, 7 dup(? )
.code

;i did macros before 

main PROC

mov eax, [fibArray + 4];eax = 1

mov edx, eax ; edx = 1
add edx, edx ; edx = 2 
add edx, edx ; edx = 4 bytes per 

mov esi, edx ; start at element 2 
mov ecx, edx ; ecx = 4
add ecx, edx ; ecx = 8
dec ecx ; ecx = 7 

fib: 
    sub esi, edx ;esi - 4 
	add eax, [fibArray + esi]
	add esi, edx 
    add esi, edx ;esi + 8
	mov[fibArray + esi], eax
Loop fib

mov bl, byte ptr[fibArray + 28]; fib(7) = 13
mov bh, byte ptr[fibArray + 32]; fib(8) = 21

mov ecx,edx ; ecx = 4
imul ecx, ecx  ; exc = 4 *4 = 16 

shift:
    add ebx,ebx
loop shift

mov bl, byte ptr[fibArray + 20]; fib(5) = 5
mov bh, byte ptr[fibArray + 24]; fib(6) = 8

call DumpRegs

mov esi, offset fibArray
mov ecx, lengthof fibArray
mov ebx, type fibArray
call DumpMem

exit

main ENDP
END main
