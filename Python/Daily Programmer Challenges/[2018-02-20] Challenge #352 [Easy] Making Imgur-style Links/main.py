'''Description

Short links have been all the rage for several years now, spurred in part by Twitter's character limits.Imgur - Reddit's
go-to image hosting site - uses a similar style for their links. Monotonically increasing IDs represented in Base62.

Your task today is to convert a number to its Base62 representation.
Input Description

You'll be given one number per line. Assume this is your alphabet:

0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

Example input:

15674
7026425611433322325

Output Description

Your program should emit the number represented in Base62 notation. Examples:

O44
bDcRfbr63n8

Challenge Input

187621
237860461
2187521
18752

Challenge Output

9OM
3n26g
B4b9
sS4

Note

Oops, I have the resulting strings backwards as noted in this thread. Solve it either way, but if you wish make a note
 as many are doing. Sorry about that.
'''
num = int(input("What number do you want to convert?"))

def toBase62(n):
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    basis = len(alphabet)
    ret = ''
    while (n > 0):
        tmp = n % basis
        ret += alphabet[tmp]
        n = (n//basis)
    return ret


anw = toBase62(num)
if anw == '':
    anw = '0'
print(anw)