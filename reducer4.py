#!/usr/bin/env python

from operator import itemgetter
import sys
var = sys.stdout
tow=[]
tow2={}
current_key = None
sums = 0
#with open('out.txt') as f:
for line in sys.stdin:
    #lines = f.readlines()
# input comes from STDIN
#for line in lines:
    # remove leading and trailing whitespace
    line = line.strip()
    row = line.split("\t")
	
    (key,value) = row
    
        
    try:
        value = int(value)
    except ValueError:
        vv=0
        continue

	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reducer
    if current_key == key:
        sums = sums + value
        tow2[key]=sums
    else:
        bb=0
        if current_key:
            # write result to STDOUT
            #print('{}\t{}'.format(current_key,sums))
            tow.append('{}\t{}'.format(current_key,sums))
            tow2[key]=sums
        current_key = key
        sums = value
	
#Last key
if current_key == key:
    tow2[key]=sums
    #print('{}\t{}'.format(current_key,sums))
    tow.append('{}\t{}'.format(current_key,sums))
#f.close()



######################
c=0
tow2=dict(sorted(tow2.items(), key=lambda item: item[1]))
#print(tow2)
for hh in tow2:
    if c<3:
        var.write('{}\t{}'.format(hh,tow2[hh]))
        var.write('\n')
    c=c+1

                
    
