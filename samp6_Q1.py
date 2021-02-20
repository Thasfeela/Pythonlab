try:
    a=open('samplein.txt','r')
    b=open('samp6.txt','w')
    w=input("Enter the word :")
    c=0
    line=a.readline()
    while line:
        l=line.split(" ")
        if w not in l:
            print(line)
            b.write("\n"+line) 
        line=a.readline()
    a.close()
    b.close()  
except IOError as io:
     print(io)