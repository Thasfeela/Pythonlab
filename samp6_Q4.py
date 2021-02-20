def capital(file1,file2):
    a=open(file1,'r')
    b=open(file2,'w')
    line=a.readline()
    while line:
        print(line.title())
        b.write("\n"+line) 
        line=a.readline()
    a.close()
    b.close()  

capital('samplein.txt','upper.txt')




