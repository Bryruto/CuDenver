def compress(msg) -> str:
    result = ""
    last = msg[0]
    count = 0
    for char in msg: 
        if last == char: 
            count +=1
        else:
            result += str(count) + last
            last = char
            count = 1
    return result + str(count) + last     

def decompress(msg) -> str:
    result = ""
    for i in range(1,len(msg),2):
        result += msg[i] * int(msg[i-1])
    return result

print("given AAAABBBCCAAB")
print( "compress: " + compress("AAAABBBCCAAB"))
print( "decompress: " + decompress("4A3B2C2A1B"))
