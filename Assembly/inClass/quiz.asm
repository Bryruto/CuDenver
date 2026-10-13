
TITLE pa3pt1.asm
INCLUDE Irvine32.inc

.data
    prompt1 byte "Enter a string of unsigned integers: ", 0
    prompt2 byte "Print a decimal in location: ", 0
    prompt3 byte "continue? Y/N: ", 0
    
    usernum byte 26 dup(0);one more for null
    userdec sdword ?;this will go in ecx
    userlength dword ?

.code

main PROC

    mainLoop:
        ;ask for input
        mov edx, OFFSET prompt1
        call WriteString

        ;save input
        mov edx, OFFSET usernum
        mov ecx, 25 
        call ReadString ; eax is holding the length
        mov userlength,eax

        
        ;ask for . location
        mov edx, OFFSET prompt2
        call WriteString

        ;save the output as sword
        call Readint; ecx will have userdec
        mov userdec,eax
        mov esi, OFFSET usernum
        mov ecx, userlength

        ;call print function
        call print
        call Crlf ; new line

        ;ask if they want to go again
        mov edx, OFFSET prompt3
        call WriteString
        call ReadChar
        
        cmp al, 'Y'
            je mainLoop
        cmp al, 'y'
            je mainLoop
    exit
main ENDP

print PROC USES ecx eax edx
    ;if input is negitive add 0.
    cmp eax, 0
    jl negitive
    je is0

    ;same size
    cmp eax, ecx
    je is0

    jmp positive

    is0:
        mov edx, esi
        call WriteString
    ret

    negitive:
        mov al, '0'
        call WriteChar
        
        mov al, '.'
        call WriteChar

        ;convert userdec to positive
        mov ecx, userdec
        neg ecx

        ;loop till ecx 0
        nLoop:
            mov al, '0'
            call WriteChar 
        loop nLoop

        ;then add the usernum
        mov edx, OFFSET usernum
        call WriteString
    ret

    ;if input is positive
    positive:
        ;take the number of elements in userlength
        ;save in ecx 
        mov ecx, userlength
        
        ;pointer to use index
        mov esi, OFFSET usernum
        mov ebx, 0

        ;loop till ecx is 0
        ploop:
            ;add 1 byte of usernum if you can if not add 0
            cmp ebx, userdec
            je printdot
            
            ;no more to add
            cmp ebx, ecx
            jge printzero
            

            mov al, [esi]
            call WriteChar

            inc esi
            inc ebx
            jmp ploop

        ;add 0
        printzero:
            mov al, '0'
            call WriteChar

            inc ebx
            jmp ploop
        ret

        ;add .
        printdot:
            mov al, '.'
            call WriteChar
            
            cmp ebx,ecx
            jge done

            mov edx, esi
            call WriteString
        ret

        done:
            mov al,'0'
            call WriteChar
        ret
    ret 
print ENDP

END main
