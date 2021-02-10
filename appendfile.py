try:
    inf=open('samplein.txt','a')
    line=input("Enter the text :")
    while line:
        inf.write("\n"+line) 
        line=input("Enter the text :")
    inf.close()
    inf=False
    inf=open('samplein.txt')
    line=inf.read()
    print(line)
except IOError as io:
     print(io)

