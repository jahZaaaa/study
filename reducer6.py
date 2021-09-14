
from operator import itemgetter
import sys
var = sys.stdout

tow2={}
current_key = None
sums = 0
for line in sys.stdin:

    line = line.strip()
    row = line.split("\t")
	
    (key,value) = row
    
        
    try:
        value = int(value)
    except ValueError:
        vv=0
        continue

	
    if current_key == key:
        sums = sums + value
        tow2[key]=sums
    else:
        bb=0
        if current_key:
            
            
            tow2[key]=sums
        current_key = key
        sums = value
	

if current_key == key:
    tow2[key]=sums    
    
f.close()




######################
#FIND TOP 3
t1=-100
t2=-100
t3=-100
k1=''
k2=''
k3=''
for i in tow2:
    if tow2[i]>t1:
        t1=tow2[i]
        k1=i
    elif tow2[i]>t2:
        t2=tow2[i]
        k2=i
    elif tow2[i]>t3:
        t3=tow2[i]
        k3=i
    
    



var.write('{}\t{}'.format(k1,tow2[k1]))
var.write('\n')

var.write('{}\t{}'.format(k2,tow2[k2]))
var.write('\n')

var.write('{}\t{}'.format(k3,tow2[k3]))
var.write('\n')



                
    
