try:
    a=open('samplein.txt','r')
    c,b,d=[],0,""
    line=a.readline()
    while line:
        l=line.split(" ")
        for i in l:
            if len(i)>b:
                d=i
                b=len(i)
        line=a.readline()
    print("Longest word is ",d)
    a.close()
except IOError as io:
     print(io)