#!/usr/bin/env python


def convert(s, numRows):
        if len(s) is 0:
            return ""
        if numRows == 0 or numRows == 1 or len(s)<=numRows:
            return s
        result = ""
        bottomIndexes = getBottomIndexes(s, numRows)    
        for row in range(0, numRows):
            if row is numRows-1 or row is 0:                
                result = result + ''.join([s[i] for i in range(row, len(s), 2*numRows-2)])
            else:
                for i in bottomIndexes:            
                    result = result + ''.join((s[i-numRows+row+1] if i-numRows+row+1<len(s) else '') + (s[i+numRows-row-1] if i+numRows-row-1<len(s) else ''))                    
        return result[:len(s)]

def getBottomIndexes(s, rows):
    return [i for i in range(rows-1, len(s)+rows, 2*rows-2)]

    
n = 503
s = "hjouvsuyoypayulyeimuotehzriicfskpggkbbipzzrzucxamludfykgruowzgiooobppleqlwphapjnadqhdcnvwdtxjbmyppphauxnspusgdhiixqmbfjxjcvudjsuyibyebmwsiqyoygyxymzevypzvjegebeocfuftsxdixtigsieehkchzdflilrjqfnxztqrsvbspkyhsenbppkqtpddbuotbbqcwivrfxjujjddntgeiqvdgaijvwcyaubwewpjvygehljxepbpiwuqzdzubdubzvafspqpqwuzifwovyddwyvvburczmgyjgfdxvtnunneslsplwuiupfxlzbknhkwppanltcfirjcddsozoyvegurfwcsfmoxeqmrjowrghwlkobmeahkgccnaehhsveymqpxhlrnunyfdzrhbasjeuygafoubutpnimuwfjqsjxvkqdorxxvrwctdsneogvbpkxlpgdirbfcriqifpgynkrrefx"
print(getBottomIndexes(s, 503))


c = convert(s, n)
#print("{} ({}) => {}".format(s, n, c))
expect = "hjouvsuyoypayulyeimuotehzriicfskpggkbbipzzrzucxamludfykgruowzgiooobppleqlwphapjnadqhdcnvwdtxjbmyppphauxnspusgdhiixqmbfjxjcvudjsuyibyebmwsiqyoygyxymzevypzvjegebeocfuftsxdixtigsieehkchzdflilrjqfnxztqrsvbspkyhsenbppkqtpddbuotbbqcwivrfxjujjddntgeiqvdgaijvwcyaubwewpjvygehljxepbpiwuqzdzubdubzvafspqpqwuzifwovyddwyvvburczmgyjgfdxvtnunneslsplwuiupfxlzbknhkwppanltcfirjcddsozoyvegurfwcsfmoxeqmrjowrghwlkobmeahkgccnaehhsveymqpxhlrnunyfdzrhbasjeuygafoubutpnimuwfjqsjxvkqdorxxvrwctdsneogvbpkxlpgdirbfcriqifpgynkrxrfe"

zzz=""
for i in range(len(c)):
    if i>=len(expect):
        print('{} {} {}'.format(None, c[i], i))
    elif expect[i] != c[i]:
        print('{} {} {}'.format(expect[i], c[i], i))

print( len(s), len(c))


assert(len(s) == len(c))
assert(convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
assert(convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
assert(convert("ABCDEF", 3) == "AEBDFC")

#3
#3
#P   A
#A P L                    PAHNAPLSIIGYIR
#Y   I

#4
#P     I      N
#A   L S   I  G          PINALSIGYAHRPI
#Y A   H R    
#P     I

