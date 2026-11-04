Comment @/*
Brycen Anderson
11/03/2026
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
call ClearRegisters;all register are 00 00 00 00


menustart:
call clrscr;clear the screen
mov edx, offset menuPrompt
call WriteString
call GetInt;what they want to do
mov userSelection, al;store in variable
mov edx, offset theString;edx is where the user will store the information
mov ecx, lengthof theString

opt1 :
cmp userSelection, 1;if the user entered a 1
jne opt2;jump not equal opt2
call clrscr;clear the screen
call GetString
mov theStringLen, al
jmp menustart


opt2 :
cmp userSelection, 2;if the user entered a 2
jne opt3; if not check opt3
call ToLower
jmp menustart


opt3 :
cmp userSelection, 3;if the user entered a 3
jne opt4;if not check opt4
call RemoveNonAlpha 
jmp menustart


opt4 :
cmp userSelection, 4;if the user entered a 4
jne opt5
call isPalindrome
Call crlf 
Call WaitMsg
jmp menustart


opt5 :
cmp userSelection, 5
jne opt6
call PrintString
jmp menustart


opt6 :
cmp userSelection, 6
jne printError
jmp quit


printError :
push edx
mov edx, offset errormessage
call writestring
call waitmsg
pop edx
jmp menustart


quit :
exit
main ENDP


;// Procedures
;-------------------------------------------------------------------------------- -
;// ClearRegisters
;// Description:
;// Requires: nothing
;// Returns: Nothing. Registers are now cleared.
;-------------------------------------------------------------------------------- -


ClearRegisters PROC
cleareax
clearebx
clearecx
clearedx
clearesi
clearedi
ret
ClearRegisters ENDP


;-------------------------------------------------------------------------------- -
;// GetInt
;// Description: Prompts the user for an unsigned integer and stores it in EAX
;// Receives: Nothing
;// Returns: user input integer in EAX
;// Requires: Nothing
;-------------------------------------------------------------------------------- -


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



;-------------------------------------------------------------------------------- -
;// GetString
;// Description: Prompts user to input a string
;// Receives: Offset of storage location for string in edx, maximum storage size in ecx
;// Returns: variable updated with string, stringlength in eax
;// Requires: Nothing
;-------------------------------------------------------------------------------- -


GetString PROC uses edx ecx


.data
promptStr BYTE "Enter a string(50 or fewer characters): ", 0ah, 0dh, 0h

.code

start :
push edx;why if you already do that with uses ?
mov edx, OFFSET promptStr
call WriteString
pop edx
call clearstring
call ReadString
cmp eax, 0
je start

ret
GetString endp


;-------------------------------------------------------------------------------- -
;// ClearString
;// Description: Clears the entire string so a new string does not containexisting values
;// Receives: string offset in edx, maxlength(global var)
;// Requires: Maxlength, string offset
;// Returns: String is now cleared.
;-------------------------------------------------------------------------------- -


ClearString PROC uses ebx ecx esi
mov ecx, maxlength
clearesi
clearebx

L1 :
mov Byte Ptr [edx + esi], 0
inc esi
loop L1

ret
ClearString ENDP



;-------------------------------------------------------------------------------- -
;// PrintString
;// Description: Prints the current user-input string to console
;// Receives: string offset in edx
;// Requires: Valid string offset in edx
;// Returns: String printed to console
;-------------------------------------------------------------------------------- -


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


;-------------------------------------------------------------------------------- -
;// ToLower
;// Description: Converts all alphabetic characters in a string to lower case.
;// Hint: You will need a loop, ASCII comparisons, a bitwise OR for the conversion, and ESI for indexing.
;// Receives: edx as pointer to the string, and the length from when the string was read i had to go add that btw
;// Requires: string to look through
;// Returns: String is now converted to lowercase.
;-------------------------------------------------------------------------------- -
;// YOUR CODE HERE


ToLower proc uses ecx esi eax 
.data
    Atoa = 32;differernce A-a

.code
    movzx ecx, theStringLen
    mov esi, offset theString

    ;this is if it is empty
    mov al, [esi]
    cmp al, 0
    je return3
    
    Lowerloop :

    mov al, [esi];//looks a char al = char

    ;//change to lower
    cmp al, 'a'
    jge already;//skip if larger than a

    cmp al, 'A'
    jl already;//skip if not a letter at all

    add al, Atoa

    cmp al, 'z';//becuase[] \^ _ ` i need to check this
    jle already

    sub al, Atoa

    already :
    mov [esi], al
    add esi, TYPE theString;//update esi

    loop Lowerloop

    return3:
    ret
ToLower endp

;-------------------------------------------------------------------------------- -
;// RemoveNonAlpha
;// Description: Removes all non-alphabetic characters from a string
;// Hint: You can compare a character to 'A' or 'z'(or 'a' and 'Z'), and use jaeand jbe jumps as needed.
;// You will also need to come up with a strategy to shift/update the remaining characters in the string.
;// Don't forget to update the string length variable as well.
;// Receives: a string and the length of that string
;// Requires: a string to look through
;// Returns: String now contains only a-z or A-Z
;-------------------------------------------------------------------------------- -
;// YOUR CODE HERE

RemoveNonAlpha proc uses esi ecx eax

.data
    newWord byte maxLength dup(0)
.code
    
    ;//edx will hold the count of shifts we will need
	mov esi, offset theString
	movzx ecx, theStringLen

	call ToLower ;//skip the hard part about doing this
    mov ebx, 0
    
    ;//this is if it is empty
    mov al, [esi]
    cmp al, 0
    je return2

	charbychar: 
   
        mov al, [esi] ;//al = char
        cmp al, 'a'
        jb remove ;// if char < a remove

        cmp al, 'z'
        ja remove ;// if char > a remove

        push esi

        mov esi, offset newWord ;//look at new word
        add esi,ebx ;//add esi with ebx , ebx is my counter for what byte im on
        mov [esi],al ;//esi will be on the next Available char

        inc ebx; //add 1 for next time 
        pop esi; //go back to theString

        remove:
            add esi, TYPE theString ;//esi + 1 for every char
        
    loop charbychar 
    
    Call ClearString;

    ;//copy the new -> old 
    mov newWord[ebx],0;//add null terminator
    mov theStringLen,bl
    inc ebx;// make sure it reads null
    mov ecx, ebx;// get the number of loop


    mov esi, offset newWord ; //get address of newWord 1st char
    mov edi, offset theString; //get address of theString 1st char

    copy:

        mov al, [esi];//get first byte of newWord
        mov [edi],al ;//add newWord char to theString
        add esi, TYPE newWord;
        add edi, TYPE theString
            
    loop copy

    return2:
    ret

RemoveNonAlpha endp


;-------------------------------------------------------------------------------- -
;// IsPalindrome
;// Description: Determines if a string is a palindrome and prints the result.
;// Hint: Start with ecx set to the string length, and use it as anindex([edx+ecx-1]).
;// This will allow you to iterate backwards through the string.
;// Use another register to also iterate forward during this same loop([edx+esi]).
;// With these two iterators you can compare characters of the string.
;// You will need to use a register as cmp cannot do memory-to-memory.
;// Receives: theString and the length of the string
;// Requires: a string to check and a working stack
;// Returns: Palindrome result printed to console.
;-------------------------------------------------------------------------------- -
;// YOUR CODE HERE
IsPalindrome proc uses esi ecx eax
.data
    word0 byte "False",0
    word1 byte "True",0

.code
    
    ;//get the string pointer and length
    mov esi, offset theString
    movzx ecx, theStringLen
    
    mov al,[esi]
    cmp al,0
    je return

    ;//push to stack String length times 
    addtostack:

        mov al,[esi]
        push eax;
        inc esi

    loop addtostack
    
    ;//get the string pointer and length again
    mov esi,offset theString
    movzx ecx, theStringLen

    ;//compare using pops from stack
    compare:
        pop eax
        cmp al,[esi]
        jne notequal 

        inc esi
    loop compare
    jmp equal
    
    ;//dec 1 more time then loop
    notequal:
        dec ecx
        jz donePopping
    
    ;//pop the rest
    cleanup:
        pop eax
    loop cleanup
    
    donePopping:

    ;//print false then return
    mov edx,offset word0
    call WriteString
    
    ret
    
    ;//print true
    equal:
        mov edx,offset word1 
        call WriteString
    
    return:
    ret
    

IsPalindrome endp


END main


