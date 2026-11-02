Comment @/*
Your Name
03/25/24
PA5
Description: Menu-based program that accepts user input and performs the following
functions:
1. Enter a string
2. Convert the string to lower case.
3. Remove all non-alphabetic characters from the string.
4. Is the string a palindrome?
5. Print the string.
6. Exit
*/@


Include Irvine32.inc
    ClearEAX textequ <mov eax, 0>
    ClearEBX textequ <mov ebx, 0>
    ClearECX textequ <mov ecx, 0>
    ClearEDX textequ <mov edx, 0>
    ClearESI textequ <mov esi, 0>
    ClearEDI textequ <mov edi, 0>
    maxLength = 51d

.data
   
   menuPrompt byte 'MAIN MENU', 0Ah, 0Dh,
    '--------------', 0Ah, 0Dh,
    '1. Enter a String:', 0Ah, 0Dh,
    '2. Convert all elements to lower case: ', 0Ah, 0Dh,
    '3. Remove all non-alphabetic characters: ', 0Ah, 0Dh,
    '4. Determine if the string is a palindrome: ', 0Ah, 0Dh,
    '5. Print the string: ', 0Ah, 0Dh,
    '6. Exit: ', 0Ah, 0Dh, 0h

    errormessage byte 'Invalid menu selection. Please try again.', 0Ah, 0Dh, 0h
    userSelection byte 0h
    theString byte maxLength dup(0)
    theStringLen byte 0
    
.code
    
    main PROC
    call ClearRegisters ;all register are 00 00 00 00 
    

    menustart:
        call clrscr;clear the screen
        mov edx, offset menuPrompt 
        call WriteString
        call GetInt;what they want to do
        mov userSelection, al;store in variable
        mov edx, offset theString ;edx is where the user will store the information
        mov ecx, lengthof theString ;this is very bad 

    opt1:
        cmp userSelection, 1;if the user entered a 1 
        jne opt2;jump not equal opt2
        call clrscr;clear the string
        call GetString
        mov theStringLen,al
        jmp menustart
    

    opt2:
        cmp userSelection, 2;if the user entered a 2
        jne opt3; if not check opt3

        call ToLower
        call waitMsg

        jmp menustart
    

    opt3:
        cmp userSelection, 3;if the user entered a 3
        jne opt4 ;if not check opt4
        
        
        jmp menustart
    

    opt4:
        cmp userSelection, 4;if the user entered a 4 
        jne opt5;if not 
        jmp menustart
    

    opt5:
        cmp userSelection, 5
        jne opt6
        call PrintString
        jmp menustart
    

    opt6:
        cmp userSelection, 6
        jne printError
        jmp quit
    

    printError:
        push edx
        mov edx, offset errormessage
        call writestring
        call waitmsg
        pop edx
        jmp menustart
        

        quit:
            exit
main ENDP


;// Procedures
;---------------------------------------------------------------------------------
;// ClearRegisters
;// Description:
;// Requires: nothing
;// Returns: Nothing. Registers are now cleared.
;---------------------------------------------------------------------------------


ClearRegisters PROC
    cleareax
    clearebx
    clearecx
    clearedx
    clearesi
    clearedi
    ret
ClearRegisters ENDP


;---------------------------------------------------------------------------------
;// GetInt
;// Description: Prompts the user for an unsigned integer and stores it in EAX
;// Receives: Nothing
;// Returns: user input integer in EAX
;// Requires: Nothing
;---------------------------------------------------------------------------------


GetInt PROC USES edx
    

    .data
        promptInt BYTE "Menu selection: ", 0ah, 0dh, 0h
        promptInvalid BYTE "Invalid Input", 0ah, 0dh, 0h
    

    .code
        start :
            mov edx, OFFSET promptInt
            call WriteString
            call ReadInt;// Sets the overflow flag and resets eax to 0 if input is invalid
            jno validInput
            mov edx, OFFSET promptInvalid
            call WriteString
            jmp start
        
        validInput :
            ret
GetInt endp



;---------------------------------------------------------------------------------
;// GetString
;// Description: Prompts user to input a string
;// Receives: Offset of storage location for string in edx, maximum storage size in ecx
;// Returns: variable updated with string, stringlength in eax
;// Requires: Nothing
;---------------------------------------------------------------------------------


GetString PROC uses edx ecx


    .data
        promptStr BYTE "Enter a string(50 or fewer characters): ", 0ah, 0dh, 0h
    
    .code
        
        start:
            push edx;why if you already do that with uses? 
            mov edx, OFFSET promptStr
            call WriteString
            pop edx
            call clearstring
            call ReadString
            cmp eax, 0
        je start

        ret
GetString endp


;---------------------------------------------------------------------------------
;// ClearString
;// Description: Clears the entire string so a new string does not containexisting values
;// Receives: string offset in edx, maxlength(global var)
;// Requires: Maxlength, string offset
;// Returns: String is now cleared.
;---------------------------------------------------------------------------------


ClearString PROC uses ebx ecx esi
    mov ecx, maxlength
    clearesi
    clearebx
    
    L1:
        mov [edx+esi], ebx
        inc esi
    loop L1
    
    ret
ClearString ENDP



;---------------------------------------------------------------------------------
;// PrintString
;// Description: Prints the current user-input string to console
;// Receives: string offset in edx
;// Requires: Valid string offset in edx
;// Returns: String printed to console
;---------------------------------------------------------------------------------


PrintString proc uses edx

    .data
        option5prompt byte 'The current string is: ', 0h
    
    .code
        call clrscr
        push edx
        mov edx, offset option5prompt
        call writestring
        pop edx
        call writestring
        call crlf;// added a crlf for readability
        call waitmsg
        ret

PrintString endp


;---------------------------------------------------------------------------------
;// ToLower
;// Description: Converts all alphabetic characters in a string to lower case.
;// Hint: You will need a loop, ASCII comparisons, a bitwise OR for the conversion, and ESI for indexing.
;// Receives: edx as pointer to the string, and the length from when the string was read i had to go add that btw
;// Requires: ?
;// Returns: String is now converted to lowercase.
;---------------------------------------------------------------------------------
;// YOUR CODE HERE


ToLower proc uses esi ecx edx
    .data
        Atoa=32
    .code
        mov esi, offset theString
        mov cl, theStringLen
        

        Lowerloop:

            mov al, [esi];looks a char al = char

            ;change to lower
            cmp al,'a'
            jge already;skip if larger than a 
            
            cmp al,'A'
            jl already;skip if not a letter at all

            add al,Atoa

            cmp al,'z';becuase [] \ ^ _ ` i need to check this 
            jle already

            sub al,Atoa
            
            already:
            add esi, Type theString ;update esi

        loop Lowerloop

        ret
ToLower endp

;---------------------------------------------------------------------------------
;// RemoveNonAlpha
;// Description: Removes all non-alphabetic characters from a string
;// Hint: You can compare a character to 'A' or 'z'(or 'a' and 'Z'), and use jaeand jbe jumps as needed.
;// You will also need to come up with a strategy to shift/update the remaining characters in the string.
;// Don't forget to update the string length variable as well.
;// Receives: ?
;// Requires: ?
;// Returns: String now contains only a-z or A-Z
;---------------------------------------------------------------------------------
;// YOUR CODE HERE
RemoveNonAlpha proc uses eax ecx edx 
    .data
        blank=' '
    .code
        ;edx will hold the count of shifts we will need
        mov esi, offset theString
        mov ecx, theStringLen

        remove:
            
            cmp [esi],'a'
            jl inbetween;i need to do inbetween Z-a
            
            inbetween:
                cmp [esi],'Z'
                jg removeNonLetter


            cmp [esi],'A'
            jge ;and also inbetween A-z 
            
            check2:
                cmp [esi],'z'
                jle 
            
            
            removeNonLetter:
                
            ;this is where we remove
            

            mov [esi],?

            skip:
        loop remove

RemoveNonAlpha endp


;---------------------------------------------------------------------------------
;// IsPalindrome
;// Description: Determines if a string is a palindrome and prints the result.
;// Hint: Start with ecx set to the string length, and use it as anindex([edx+ecx-1]).
;// This will allow you to iterate backwards through the string.
;// Use another register to also iterate forward during this same loop([edx+esi]).
;// With these two iterators you can compare characters of the string.
;// You will need to use a register as cmp cannot do memory-to-memory.
;// Receives: ?
;// Requires: ?
;// Returns: Palindrome result printed to console.
;---------------------------------------------------------------------------------
;// YOUR CODE HERE
IsPalindrome proc
    .data

    .code

IsPalindrome endp


END main


