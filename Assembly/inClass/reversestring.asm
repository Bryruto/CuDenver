.data
aName byte "Abraham Lincoln",0
nameSize = ($-aName)-1

.code 
main proc

mov ecx,nameSize 
mov esi,0

L1: movzx ezx,aName[esi]
push eax 
inc esi
loop L1

mov ecx, nameSize
moc esi,0

L2:pop eax 
mov aName[esi],al
inc esi
