try:
    a=open('samplein.txt','r')
    b=open('sample6.txt','w')
    line=a.readline()
    while line:
        if not(line.startswith('#')):
             print(line)
             b.write("\n"+line) 
        line=a.readline()
    a.close()
    b.close()  
except IOError as io:
     print(io)