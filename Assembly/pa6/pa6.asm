Comment @/*
Brycen Anderson
11/03/2026
PA6
Description: Add this after
functions: GetInt so far 
*/@

Include Irvine32.inc

;-------------------------------------------------------------------------------- -
;// Proc name: main 
;// Description: 
;// Receives:
;// Requires: 
;// Returns: 
;-------------------------------------------------------------------------------- -

.data

Menu byte "Main menu",0
;add a loop of 50 to make a line -
option1 byte "1. Display all primes between 2 and n (max of 10000)" ,0
option2 byte "2. Euclid's Algorithm for GCD" ,0
option3 byte "3. Exit" ,0
maininputerror byte "enter 1,2,or 3 please",0
.code

main PROC

call GetInt

promptuser:
call Clrscr

;edx will look at 'M' or main menu
mov edx, offset Menu
call WriteString;print till you hit null
call Crlf 

;make a dash line i think 50 is ok
mov ecx,50
mov al,'-'
dash:
    call WriteChar
loop dash
call Crlf

;just print the options
;print option1
mov edx, offset option1
call writeString
call Crlf 

;print option2 
mov edx,offset option2
call writeString
call Crlf 

;print option3
mov edx,offset option3
call writeString
call Crlf 

;store in eax 
call readint
;go to option1
cmp eax,1
je option1run

;go to option2
cmp eax,2
je option2run

;go to option3
cmp eax,3
je option3run

;invalid input not an option
mov edx,offset maininputerror
call writeString
call Crlf
call waitmsg
jmp promptuser

;print the results 
option1run:
call PrintResults

;find the prime for a given number
option2run:
call FindPrimes

option3run:
exit

main ENDP


;-------------------------------------------------------------------------------- -
;// Proc name: GetInt 
;// Description: accepts an unsigned integer from the user and verifies that the number is a valid input
;// Receives:eax,edx
;// Requires: eax,edx
;// Returns: eax
;-------------------------------------------------------------------------------- -

GetInt PROC

.data

prompt byte "Enter a valid positive number between 2 and 10,000:",0
error byte "That is not between 2 and 10,000 or is not a number",0 

.code

push edx
; get the in from the user
readinput: 
    call clrscr
   
   ;prompt the user for the input
    mov edx, offset prompt
    call writeString
    
    ;store the value in eax
    call ReadInt

    ;if less then 2
    cmp eax,2
    jl again
    
    ;if greater then 10,000
    cmp eax,10000
    jg again
    
    ;only will go if input is valid
    pop edx
    ret

;print the error run again
again:
    mov edx,OFFSET error
    call WriteString
    call crlf
    call WaitMsg
    jmp readinput

GetInt ENDP

;-------------------------------------------------------------------------------- -
;// Proc name: FindPrimes
;// Description:
;// Receives:none
;// Requires: eax 
;// Returns: 
;-------------------------------------------------------------------------------- -

FindPrimes PROC

.data

;dword that means everything is by 4 
numArray dword 10000 dup(?)
primes dword 10000 dup(?)

.code
;save the input number
push eax

;this is the count
mov ecx,eax
dec ecx ;this is a bug fix n-1 if input is 5 i should get 5 not 6
mov eax,2
mov edi,offset numArray
push ecx

;cld means move foward
cld
;ok so this should store edi pointer location to what ever eax is then add 1 and do again 
L1:
    stosd
    inc eax
    loop L1

;now we need an array to look through that array
mov esi,offset primes 
pop ecx 
mov edi,offset numArray;look at number or 0 not a prime
l2:
    mov eax,[edi];eax equal number we are looking at 
    
    cmp eax, 0; is it a 0 its not a prime
    jne prime ; if it is not a 0 it is prime 
    
    mov [esi], eax; save the prime in the primes array

    next:
    add edi,4 
    loop L2
    
    prime:
        push edi; save the pointer to this number
        push ecx;save where we are at
        
        mov ebx, eax ; when i div eax is dividend
        elim:;we just want the ones infront
            mov eax,[edi];this is the next value we will check 
            ;eax/ebx = eax(quotient) and edx(remainder)
            div ebx

            cmp edx,0; if remainder is 0 this cant be a prime
            je makeZero;
            jmp nextnum;

            makeZero:
                mov [edi],0

            nextnum:
                add edi,4
        loop elim

        pop ecx; return the where we are at loop wise
        pop edi; return the pointer
        jmp next ;return to next loop

;return the input number
pop eax 
ret
FindPrimes ENDP


;-------------------------------------------------------------------------------- -
;// Proc name: PrintResults 
;// Description:
;// Receives:none
;// Requires: 
;// Returns: 
;-------------------------------------------------------------------------------- -

PrintResults PROC

.data
.code


ret
PrintResults ENDP
END main
