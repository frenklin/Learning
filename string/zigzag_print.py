#!/usr/bin/env python


def convert(s, numRows):
    if len(s) is 0:
        return ""
    if numRows == 0 or numRows == 1 or len(s)<=numRows:
        return s
    result = ""
    bottomIndexes = getBottomIndexes(s, numRows)
    for i in range(0, numRows):
        result = result + ''.join(getRow(i, s, numRows,bottomIndexes))
    return result[:len(s)]

def getRow(row, s, rows, bottomIndexes):
    if row is rows-1 or row is 0:
        return [s[i] for i in range(row, len(s), 2*rows-2)]
    else:
        result = ""
        for i in bottomIndexes:
            result = result + getPair(i, row, rows, s)
    return result

def getBottomIndexes(s, rows):
    return [i for i in range(rows-1, len(s)+rows-1, 2*rows-2)]


def getPair(i, row, rows, s):
    return (s[i-rows+row+1] if i-rows+row+1<len(s) else '') + (s[i+rows-row-1] if i+rows-row-1<len(s) else '')



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
assert(convert("hjouvsuyoypayulyeimuotehzriicfskpggkbbipzzrzucxamludfykgruowzgiooobppleqlwphapjnadqhdcnvwdtxjbmyppphauxnspusgdhiixqmbfjxjcvudjsuyibyebmwsiqyoygyxymzevypzvjegebeocfuftsxdixtigsieehkchzdflilrjqfnxztqrsvbspkyhsenbppkqtpddbuotbbqcwivrfxjujjddntgeiqvdgaijvwcyaubwewpjvygehljxepbpiwuqzdzubdubzvafspqpqwuzifwovyddwyvvburczmgyjgfdxvtnunneslsplwuiupfxlzbknhkwppanltcfirjcddsozoyvegurfwcsfmoxeqmrjowrghwlkobmeahkgccnaehhsveymqpxhlrnunyfdzrhbasjeuygafoubutpnimuwfjqsjxvkqdorxxvrwctdsneogvbpkxlpgdirbfcriqifpgynkrrefx", 503) == "hjouvsuyoypayulyeimuotehzriicfskpggkbbipzzrzucxamludfykgruowzgiooobppleqlwphapjnadqhdcnvwdtxjbmyppphauxnspusgdhiixqmbfjxjcvudjsuyibyebmwsiqyoygyxymzevypzvjegebeocfuftsxdixtigsieehkchzdflilrjqfnxztqrsvbspkyhsenbppkqtpddbuotbbqcwivrfxjujjddntgeiqvdgaijvwcyaubwewpjvygehljxepbpiwuqzdzubdubzvafspqpqwuzifwovyddwyvvburczmgyjgfdxvtnunneslsplwuiupfxlzbknhkwppanltcfirjcddsozoyvegurfwcsfmoxeqmrjowrghwlkobmeahkgccnaehhsveymqpxhlrnunyfdzrhbasjeuygafoubutpnimuwfjqsjxvkqdorxxvrwctdsneogvbpkxlpgdirbfcriqifpgynkrxrfe")

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


def convert2(s: str, numRows: int) -> str:
    line, delta = 0, 1
    result = [""] * numRows
    for i in range(len(s)):
        result[line] += s[i]
        if numRows > 1:
            line += delta
            if line == 0 or line == numRows -1:
                delta *= -1
    return ''.join(result)

