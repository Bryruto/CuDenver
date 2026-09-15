[lable:]mnemonic[operands][;comment]

mnemonic 
mnemonic[destination]
mnemonic[destination],[source]
mnemonic[destination],[source-1],[source-2]

immediate
    A numberic literal expression 
register
    Uses a named register in the CPU 
memory
    References a memory location

operand
reg8 
reg16
reg32
sreg
imm
imm16
imm32
reg/mem8
reg/mem16

Direct memory Operands 
    .data
        var1 BYTE 10h
    .code 
        mov al,var1 ;AL = 10h
        mov al,[var1] ;treat the value at that register 
        mov al,[var1 + 5]; AL = ??h

mov destination,source 
    possibly the most common instruction 
    
    Both operands must be same size

    no more than one memory operand permitted 

    Cs,EIP,IP cannot be the destination 

    EIP = instruction pointer 

    There aer no memory to memory moveas 

    destination (reg,mem,reg,mem,reg)
    source(reg,reg,mem,imm,imm)

put at the top of all files 
mov 


.data
count BYTE 100
wVal WORD 2 

.code 
mov bl,count 
mov ax,wVal
mov count,al 

mov al,wVal ; error 
mov ax,count ; error 8 bits to 16 bits does not work need to be the same size 
mov eax,count; 



.data
oneByte BYTE 78h 
oneWord WORD 1234h
oneDword DWORD 12345678h
.code 
mov eax,0; eax = 000000h
mov al,oneByte; eax = 00000078h
mov ax,oneWord ; eax = 0001234h
mov eax,oneDword;eax = 12345678h
mov as,0 ; eax= 12340000h




.data 
bVal BYTE 100
BVal2 BYTE ? 
wVal WORD 2
dval Dword 5
.code 
mov ds ,45 ; immediate move to Ds 



.data
Bvar BYTE



2 solution solution
    .data 
    val BYTE 23h
    .code 
    movzx ax,val ; ax = 0023h
    ; eax = ????0023h 


movsx 
    move with sign extend 

.data 
val Sword 2
val1 sword -2
.code 
movsx eax,val ; eax = 0000002h 
movsx eax,val1 ; eax = FFFFFFFEh


LAHF/LAHF

LAHF - load status flags into AH 
copies lower byte of eflags register 
    sign,zero ,auxiliary carrry ,parity and carry for example 

XCHG
    exchanes the contents of two operands 
    
