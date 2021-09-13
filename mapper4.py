import sys
lines = []
var = sys.stdout
tow=[]
#with open('note.txt') as f:
    #lines = f.readlines()


count = 0
for line in sys.stdin:
#for line in lines:
    line = line.strip()
    rows = line.split(",")
    (name1,phone1,name2,phone2,timestamp_ms,timestamp_str,duration_m) = tuple(rows)
    #print(rows)
    
    
    #for i in rows:
    #    var.write(i)
    
    #tow.append('{}\t{}'.format(name1, int(duration_m)))
    
	#(name1,phone1,name2,phone2,timestamp_ms,timestamp_str,duration_m) = tuple(rows)

	# write the results to STDOUT (standard output);
	# what we output here will be the input for the
	# Reduce step, i.e. the input for reducer.py

    
    try:
        print('{}\t{}'.format(name1, int(duration_m)))
        var.write('{}\t{}'.format(name1, int(duration_m)))
        var.write('\n')
        vv=0 
        
    except ValueError as e:
                      
        print('')
        continue

#f.close()
###############






	
