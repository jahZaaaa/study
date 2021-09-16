#!/usr/bin/env python

from operator import itemgetter
import sys
var = sys.stdout
tow=[]
tow2={}
current_key = None
sums = 0
max_sum = -20000
max_key = ''
max_sum2 = -20000
max_key2 = ''
max_sum3 = -20000
max_key3 = ''

for line in sys.stdin:
    
    
    line = line.strip()
    row = line.split("\t")
    
    
    (key,value) = row
    
        
    try:
        
        value = int(value)
        
                
                    
    except ValueError:
        vv=0
        continue

    if key in tow2:
            
            tow2[key]=tow2[key]+value
            
            if tow2[key] > max_sum :
                max_sum2=max_sum
                max_key2=max_key
                max_sum=tow2[key]
                max_key=key
                
                
            elif tow2[key] > max_sum2 :                
                max_sum3=max_sum2
                max_key3=max_key2
                max_sum2=tow2[key]
                max_key2=key
                
                
            elif tow2[key] > max_sum3 :
                max_sum3=tow2[key]
                max_key3=key
                
            
                
            
                
        else:
           
            tow2[key]=value
            
            if tow2[key] > max_sum :
                max_sum2=max_sum
                max_key2=max_key
                max_sum=tow2[key]
                max_key=key
                
                
            elif tow2[key] > max_sum2 :
                max_sum3=max_sum2
                max_key3=max_key2
                max_sum2=tow2[key]
                max_key2=key
                
                
            elif tow2[key] > max_sum3 :
                max_sum3=tow2[key]
                max_key3=key
                
var.write('{}\t{}'.format(max_key,tow2[max_key])
var.write('{}\t{}'.format(max_key2,tow2[max_key2])
var.write('{}\t{}'.format(max_key3,tow2[max_key3])

	






                
    
