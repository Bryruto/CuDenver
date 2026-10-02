TITLE pa2.asm
INCLUDE Irvine32.inc

next = 4
loopAmount = 7
shift = 16

.data
fibArray DWORD 0, 1, 7 dup(? )
.code

main PROC
;mov eax, [fibArray]; eax = 0000 0000

;element 3
;add eax, [fibArray]; eax = 0000 0001
;mov[fibArray + 8], eax;

;element 4
;add eax, [fibArray + 4]; eax = 0000 0002
;mov[fibArray + 12], eax;

;element 5
;add eax, [fibArray + 8];eax = 0000 0003
;mov[fibArray + 16], eax

;element 6
;add eax, [fibArray + 12]; eax = 0000 0005
;mov[fibArray + 20], eax

;element 7
;add eax, [fibArray + 16]; eax = 0000 0008
;mov[fibArray + 24], eax

;element 8
;add eax, [fibArray + 20];eax = 0000 000D == 13
;mov[fibArray + 28], eax

;element 9
;add eax, [fibArray + 24]; eax = 0000 0015 == 21
;mov[fibArray + 32], eax

mov eax, [fibArray + next];eax = 1
mov esi, next; next is 4 because 4 bytes
mov ecx, loopAmount;get the nth element

fib: ;ok i want to loop this but dont know how yet let me cook for a little

	add eax, [fibArray + esi - next]
	add esi, next
	mov[fibArray + esi], eax

Loop fib

mov bl, byte ptr[fibArray + next * 7]; fib(7) = 13
mov bh, byte ptr[fibArray + next * 8]; fib(8) = 21

shl ebx, shift; i thought i could just add a lot to shift but this is much better

mov bl, byte ptr[fibArray + next * 5]; fib(5) = 5
mov bh, byte ptr[fibArray + next * 6]; fib(6) = 8


mov esi, offset fibArray
mov ecx, lengthof fibArray
mov ebx, type fibArray
call DumpMem

exit

main ENDP
END main
