TITLE cal.asm
INCLUDE Irvine32.inc
;ok so this is going to be a calculator app
.data
    Screen byte 30 dup("_"),0
.code

main PROC

    mov edx,offset screen
    call WriteString 
    
    exit
main ENDP
END main

