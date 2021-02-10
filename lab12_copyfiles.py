try:
    inf=open('samplein.txt')
    outf=open('sampleout.txt','w')
    line=inf.readline()
    while line:
        outf.write(line) 
        line = inf.readline()
    inf.close()
    outf.close()
    inf=False
    inf=open('sampleout.txt')
    line=inf.read()
    print(line)
except IOError as io:
     print(io)

