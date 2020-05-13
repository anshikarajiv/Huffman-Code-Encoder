#Language - Python (v3.7)

import textwrap 
import sys

inputfile = sys.argv[1]
with open(inputfile) as file:
    filecontents = file.read()

cfreq = {} #Variable storing frequency of chars
for i in filecontents:
    if i not in cfreq:
        cfreq[i] = 1
    else:
        cfreq[i] = cfreq[i] + 1

tpx = sorted(cfreq.items(), key = lambda x: (x[1], x[0])) #Sorting

#Codes storage
codearr = {}
for ch in tpx:
    codearr[ ch[0] ] = ''  

while (len(tpx) > 1):
    
    tpx = sorted( tpx, key = lambda x: (x[1], x[0]) ) #Sorting
    
    tree1 = tpx.pop(0)
    tree2 = tpx.pop(0)
    tree = [tree1, tree2]
    sortedtree = sorted(tree)
    lefttree = sortedtree.pop(0)
    righttree = sortedtree.pop(0)

    for c1 in lefttree[0]:
        codearr[c1] = '0' + codearr[c1]
    for c2 in righttree[0]:
        codearr[c2] = '1' + codearr[c2]
        
    tpx.append((lefttree[0] + righttree[0], lefttree[1] + righttree[1])) #New Node is appended

messageencoded = ''
for ch in filecontents:
    messageencoded = messageencoded + codearr[ch]

codearr = sorted( codearr.items(), key = lambda x: x[0] )
sumofFr = lensumofFr = 0
with open("code.txt", "w") as f: 
    for j in range(len(codearr)):
        if codearr[j][0] == ' ':
            print("Space: " + codearr[j][1], file=f)
            a = cfreq.get(codearr[j][0])
            sumofFr = sumofFr + a 
            prod = len(codearr[j][1]) * a
            lensumofFr = lensumofFr + prod
        else:
            print(codearr[j][0] + ": " + codearr[j][1], file=f)
            a = cfreq.get(codearr[j][0]) 
            sumofFr = sumofFr + a 
            prod = len(codearr[j][1]) * a
            lensumofFr = lensumofFr + prod
    #Printing average
    print("Ave = " + str(round( (lensumofFr/sumofFr), 2)) + " bits per symbol", end='', file=f)
    
#Text Wrapping
rowcharwrap = textwrap.TextWrapper(width=80)
lineswp = rowcharwrap.wrap(text=messageencoded)
with open("encodemsg.txt", "w") as f: 
    for i in range(len(lineswp)):
        if ( i != len(lineswp) - 1):
            print(lineswp[i], file=f)
        else:
            print(lineswp[i], end='', file=f)
