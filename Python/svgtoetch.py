# By Vipul Vacharajani

image = open("testfile.txt")
rawlines = image.readlines()
path = ""
#Remove tabs:
lines = []

for line in rawlines:
    startstab = True
    newline = line
    while startstab:
        if newline[0] == " " or newline[0] == "\t":
            newline = newline[1:]
        else:
            startstab = False
    if line[-1]=="\n":
        newline=newline[:-1]
    lines.append(newline)
paths = []
print (lines)
line=""
for i in lines:
    line+=i
if line[0:2]== "d=":
    print("FOUND IT")
    firstindex = 0
    foundfirst = False
    done=False
    lastindex = 0
    for i in range(len(line)):
        if line[i] == "\"" and not done:
            if not foundfirst:
                print("found first \"")
                firstindex = i+1
                print(i+1)
                foundfirst = True
            elif foundfirst:
                lastindex = i
                done=True       
                print(i)
    path = line[firstindex: lastindex]
if len(path)!=0:
    paths.append(path)
print (paths)

rawpath = ""

for i in paths:
    rawpath+=i
#get rid of tabs
path=""
for i in rawpath:
    if i!="\t":
        path+=i
print(path)
#add spaces
i=0
while i <len(path):
    if path[i] in ["C","c","H",'h','Q','q','L','l','z','M','m','V','v','S','s','T','t']:
        path = path[:i]+" "+path[i]+" "+path[i+1:]
        i+=4
    elif path[i] in [","]:
        path = path[:i] + " " +path[i+1:]
        i+=2
    elif path[i] =="-":
        path = path[:i] + " " +path[i:]
        i+=2
    else:
        i+=1
arg = path.split(" ")
i=0
while i<len(arg):
    if arg[i]=="":
        arg.pop(i)
        
    else:
        i+=1
print (arg)
#print args

#Translate to the arduino

code = ""
i = 0
firstm = True
secondm = True
while i<len(arg):
    if arg[i] =="C":
        code+="svgC("+arg[i+1]+","+arg[i+2]+","+arg[i+3]+","+arg[i+4]+","+arg[i+5]+","+arg[i+6]+");\n"
        print(arg[i+1])
        print(arg[i+2])
        print(arg[i+3])
        i+=7
    elif arg[i] == "c":
        code+="svgc("+arg[i+1]+","+arg[i+2]+","+arg[i+3]+","+arg[i+4]+","+arg[i+5]+","+arg[i+6]+");\n"
        i+=7
    elif arg[i] == "Q":
        code+="svgQ("+arg[i+1]+","+arg[i+2]+","+arg[i+3]+","+arg[i+4]+");\n"
        print(arg[i+1])
        print(arg[i+2])
        i+=5
    elif arg[i] == "q":
        code+="svgq("+arg[i+1]+","+arg[i+2]+","+arg[i+3]+","+arg[i+4]+");\n"
        i+=5
    elif arg[i] == "L":
        code+="svgL("+arg[i+1]+","+arg[i+2]+");\n"
        print(arg[i+1])
        i+=3
    elif arg[i] == "l":
        code+="svgl("+arg[i+1]+","+arg[i+2]+");\n"
        i+=3
    elif arg[i] == "M":
        code+="svgL("+arg[i+1]+","+arg[i+2]+");\n"
        i+=3
    elif arg[i] == "V":
        code+="svgV("+arg[i+1]+");\n"
        i+=2
    elif arg[i] == "v":
        code+="svgv("+arg[i+1]+");\n"
        i+=2
    elif arg[i] == "H":
        code+="svgH("+arg[i+1]+");\n"
        i+=2
    elif arg[i] == "h":
        code+="svgh("+arg[i+1]+");\n"
        i+=2
    elif arg[i] == "S":
        code+="svgS("+arg[i+1]+","+arg[i+2]+","+arg[i+3]+","+arg[i+4]+");\n"
        i+=5
    elif arg[i] == "s":
        code+="svgs("+arg[i+1]+","+arg[i+2]+","+arg[i+3]+","+arg[i+4]+");\n"
        i+=5
    elif arg[i] == "T":
        code+="svgT("+arg[i+1]+","+arg[i+2]+");\n"
        i+=3
    elif arg[i] == "t":
        code+="svgt("+arg[i+1]+","+arg[i+2]+");\n"
        i+=3
    else:
        i+=1
outfile = open("Sierpinski.txt","w")
##print(code)
outfile.write(code)
outfile.close()
