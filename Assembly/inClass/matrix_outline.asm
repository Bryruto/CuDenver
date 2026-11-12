;// Quiz 5 - Outline code
;// This is the starting point for Quiz 5.
;// You are to read through and fully comment the FillMatrix, ResetMatrix, and PrintMatrix procedures.
;// Then you will implement the CheckRow, CheckCols, and CheckDiag procedures.
;// Your completed program should print out all "words" found in the matrix.
;// (A "word" is a string of 5 characters with exactly 2 vowels).
;// Submit your finished program on Canvas.

Include Irvine32.inc


FillMatrix PROTO m : PTR BYTE, mLen : BYTE
ResetMatrix PROTO m : PTR BYTE, mLen : BYTE
PrintMatrix PROTO m : PTR BYTE

CheckRow PROTO m : PTR BYTE
CheckCols PROTO m : PTR BYTE
CheckDiag PROTO  m : PTR BYTE

.data
matrix BYTE 25 dup(? )
matrixLength BYTE 0
noWords BYTE 'No words in matrix.', 0ah, 0dh, 0h
continuePrompt BYTE 'Check another matrix? (Y/N)', 0h

.code
main proc

mov matrixLength, lengthof matrix

Start :
mov edx, 0
;// clear and reset the matrix on each iteration
INVOKE ResetMatrix, ADDR matrix, matrixLength
INVOKE FillMatrix, ADDR matrix, matrixLength
INVOKE PrintMatrix, ADDR matrix
;// check and print words horizontally, vertically, and diagonally
INVOKE CheckRow, ADDR matrix
INVOKE CheckCols, ADDR matrix
INVOKE CheckDiag, ADDR matrix
call crlf

;// if no words found,  print message
cmp edi, 0
jne cont
mov edx, OFFSET noWords
call WriteString


cont :
;// get loop input
mov edx, OFFSET continuePrompt
call WriteString
call readChar
cmp al, 'n'
je quit
cmp al, 'N'
je quit
call crlf
jmp Start

quit :

exit
main endp


;//-------------------------------------------------------------------------------------
;// FillMatrix
;// Description: Fills the matrix with letters, half of which will be vowels. 
;// Receives: an address to the matrix and the number of elements in that matrix
;// Returns:  The matrix filled with letters, with a 50/50 chance between vowels and consonants
FillMatrix PROC m : PTR BYTE, mlen : BYTE

.data
;// the two arrays to choose from
Con BYTE "BCDFGHJKLMNPQRSTVWXYZ", 0h
Vow BYTE "AEIOU", 0h

.code

call Randomize ;calling a function Randomize

movzx ecx, mlen ; move extended ecx to value at mlen 
mov edi, m ;store m value in edi

L1:;loop 1 
call Random32; call function random32

Test al, 1;check if al is odd or even
je cons;if al equals 1 jmp to cons

vowel:;loop for vowel
mov edx, 0;set edx to 0 ; this is for indexing 
mov ebx, 5; set ebx to 5
div ebx ;eax/ebx = eax r=edx
mov esi, OFFSET vow;esi to look at vowel array
mov al, [esi + edx];set to pointer location of esi + edx at the start that is A
mov [edi + ecx - 1], al;store what is in al in location of edi + ecx - 1
loop L1;do all over again till ecx is 0
jmp full;jump to full when done

cons:
mov edx, 0 ; set edx to 0
mov ebx, 21 ; set ebx to 21
div ebx ; eax/ebx = eax r = edx
mov esi, OFFSET con ; esi is looing at consonants
mov al, [esi + edx]; al will store value at esi + edx
mov [edi + ecx - 1], al; edi + ecx -1 location will store al value
loop L1 ; loop and get next fill

full :
ret;array is filled

FillMatrix endp
;//-------------------------------------------------------------------------------------

;//-------------------------------------------------------------------------------------
;// ResetMatrix
;// Receives: address of the matrix and it's length
;// Returns:  the matrix reset to all 0's
ResetMatrix PROC m : PTR BYTE, mLen : BYTE

movzx ecx, mLen;ecx gets the matrix length
mov esi, m ; esi will point to matrix
mov al, 0 ;set al to 0

clear :;set every element to 0 going backward through the loop
	mov[esi + ecx - 1], al
	loop clear

	ret;return the array of 0's

	ResetMatrix endp
	;//-------------------------------------------------------------------------------------

;//-------------------------------------------------------------------------------------
;// printMatrix
;// Description: Prints the matrix in 5x5 format
;// Receives: address of the matrix
;// Returns:  matrix printed to console in 5x5 format
PrintMatrix PROC m : PTR BYTE

.data
rowInd BYTE 0;set the row index to 0

.code
mov ecx, 5 ;set ecx to 5
mov edi, m ; edi will look at location of matrix
rowSz = 5 ;rowsize is 5 there will be 5 elements per row 
line:
mov esi, 0;set esi to 0
push ecx; push ecx to the stack
mov ecx, 5 ; set ecx to 5 
index:
mov al, [edi + esi] ;store edi + esi to al
call writeChar; write the char in al
;print a space between every print 
mov al, ' ' 
call writeChar
;go to the next letter with by adding 1 to esi
inc esi
loop index;go back to index flag 

pop ecx; pop ecx now stack is empty
add edi, rowSz;edi is looking at the next row 
call crlf ; get a new line 
loop line;go to line flag and do all again

ret

PrintMatrix endp
;//-------------------------------------------------------------------------------------

;//-------------------------------------------------------------------------------------
;// CheckRow
;// Description: Checks matrix for horizontal words and prints them
;// Receives: address of the matrix
;// Returns:  all horizontal words printed to console
;// Hint: lodsb might be useful. 

CheckRow PROC m : PTR BYTE
.data

wordSpacer BYTE ', ', 0h
wordsFound Dword 0 

.code

;// YOUR CODE HERE
mov wordsFound, 0
mov edi,m;this is the location of the matrix

start:
mov ecx,5;number of elements per row 
mov ebx,0; this will be my count of vowels

checkRowL1:
mov al, [edi];this will give each char in the row
push ecx;save loop count on stack

mov ecx, lengthof vow - 1;the length of vow 5
mov esi,offset vow;position of vow

isVow:

mov dl, [esi]
add esi,type vow; move it to look at the next location
;i had to move it because of the loopne
            
cmp al,dl; if the al == dl dl will be a char then al is a char
loopne isVow; i love this so much 
        
jne notVowel
inc ebx ;add one to the vow count

notVowel:
pop ecx;restore loop count
inc edi;move to the next char
loop checkRowL1

cmp ebx,2; if equal print it off
jne nextRow;go to the next row edi will aready be there 

inc wordsFound
mov esi,edi; set esi to the row edi is at
sub esi, 5 ;go back to start of row
mov ecx, 5 ;print all 5 chars 

printstring:

mov al,[esi];char set to al
add esi,type vow;i can also do inc of add esi,1 but this is better and safer most of the time i think 
call WriteChar;print to the screen what is in al
loop printstring

mov edx,offset wordSpacer; set edx to wordspacer after word is printed
Call writeString;print to screen what is in edx till it hits 0

nextRow:
mov eax,m;set eax to the end to check if edi is over
add eax, 25;5X5 is 25
cmp edi, eax; if edi > end here if lower keep going
jb start

mov edi, wordsFound
ret 

CheckRow endp
;//-------------------------------------------------------------------------------------

;//-------------------------------------------------------------------------------------
;// CheckCols
;// Description: Checks matrix for vertical words and prints them.
;// Receives:	address of the matrix 
;// Returns:	vertical words printed to screen
;a e i o u 
CheckCols PROC m : PTR BYTE

.data
wordSpace BYTE ', ', 0h
colInd DWORD 0
colWords DWORD 0

.code
mov colWords, edi ;save the words already found
mov colInd, 0 ;start at the first column

startCol:
mov edi, m ;location of matrix
add edi, colInd ;move to the start of this column
mov ecx, 5 ;number of elements per column
mov ebx, 0 ;this will be my count of vowels

checkColL1:
mov al, [edi] ;get each char in the column
push ecx ;save loop count on stack

mov ecx, LENGTHOF vow - 1 ;the length of vowels is 5
mov esi, OFFSET vow ;position of vow

isVowCol:
mov dl, [esi] ;get vowel to compare
add esi, TYPE vow ;move to the next vowel
cmp al, dl ;check if the char is a vowel
loopne isVowCol

jne notVowelCol ;skip count if no vowel matched
inc ebx ;add one to the vowel count

notVowelCol:
pop ecx ;restore loop count
add edi, 5 ;move down one row in the same column
loop checkColL1

cmp ebx, 2 ;if exactly 2 vowels print the column
jne nextCol

inc colWords ;add one to the words found
mov esi, m ;go back to the matrix
add esi, colInd ;go to the start of this column
mov ecx, 5 ;print all 5 chars

printstringCol:
mov al, [esi] ;set al to the char
add esi, 5 ;move down to the next char
call WriteChar ;print the char in al
loop printstringCol

mov edx, OFFSET wordSpace ;space between words
call WriteString

nextCol:
inc colInd ;move to the next column
cmp colInd, 5 ;check if all 5 columns are done
jb startCol

mov edi, colWords ;return total words found
ret

CheckCols endp
;//-------------------------------------------------------------------------------------

;//-------------------------------------------------------------------------------------
;// CheckDiag
;// Description: Checks matrix for diagonal words and prints them.
;// Receives:	 address of matrix
;// Returns:	 diagonal words printed to console
CheckDiag PROC m : PTR BYTE

.data
wordsp BYTE ', ', 0h
diagStep DWORD 6
diagWords DWORD 0

.code
mov diagWords, edi ;save the words already found
mov diagStep, 6 ;move 6 bytes for top left to bottom right
mov edi, m ;start at the first char in the matrix

startDiag:
mov ecx, 5 ;number of elements per diagonal
mov ebx, 0 ;this will be my count of vowels

checkDiagL1:
mov al, [edi] ;get each char in the diagonal
push ecx ;save loop count on stack

mov ecx, LENGTHOF vow - 1 ;the length of vowels is 5
mov esi, OFFSET vow ;position of vow

isVowDiag:
mov dl, [esi] ;get vowel to compare
add esi, TYPE vow ;move to the next vowel
cmp al, dl ;check if the char is a vowel
loopne isVowDiag

jne notVowelDiag ;skip count if no vowel matched
inc ebx ;add one to the vowel count

notVowelDiag:
pop ecx ;restore loop count
add edi, diagStep ;move to the next diagonal char
loop checkDiagL1

cmp ebx, 2 ;if exactly 2 vowels print the diagonal
jne nextDiag

inc diagWords ;add one to the words found
mov esi, m ;go back to the start of the matrix

cmp diagStep, 6 ;check which diagonal we are printing
je setupPrintDiag
add esi, 4 ;second diagonal starts at the top right

setupPrintDiag:
mov ecx, 5 ;print all 5 chars

printstringDiag:
mov al, [esi] ;set al to the char
add esi, diagStep ;move to the next diagonal char
call WriteChar ;print the char in al
loop printstringDiag

mov edx, OFFSET wordsp ;space between words
call WriteString

nextDiag:
cmp diagStep, 4 ;check if the second diagonal is done
je done

mov diagStep, 4 ;move 4 bytes for top right to bottom left
mov edi, m ;go back to the start of the matrix
add edi, 4 ;move to the top right char
jmp startDiag ;check the second diagonal

done:
mov edi, diagWords ;return total words found
ret

CheckDiag endp

END main
