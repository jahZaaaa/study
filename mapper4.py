
import sys
lines = []
var = sys.stdout

count = 0
for line in sys.stdin:

    line = line.strip()
    rows = line.split(",")
    (name1,phone1,name2,phone2,timestamp_ms,timestamp_str,duration_m) = tuple(rows)
    

    
    try:
        
        var.write('{}\t{}'.format(name1, int(duration_m)))
        var.write('\n')
        vv=0 
        
    except ValueError as e:
                      
        print('')
        continue








	
