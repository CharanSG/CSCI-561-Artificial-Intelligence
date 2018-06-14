import sys;
import re
inputFile = open(sys.argv[2],'r');
file = open("output.txt","w");

line = inputFile.readline();
day = line.rstrip()# to remove the \n charachter at the end of line
print(day)

line = inputFile.readline();
player = line.rstrip();
print(player)

line = inputFile.readline();
myList = re.findall('\w+', line)
#myList = line.split(',','(',')')
#myList.split('(')
#print(myList)
b = dict(zip(myList[::2], myList[1::2]))
detailNode = {k:int(v) for k,v in b.items()}
#print(b)
print(detailNode)
del myList

initMat = []
for i in range(len(detailNode)):
    line = inputFile.readline();
    line = line.rstrip();
    line = re.findall('\w+',line)
    line = [int(k) for k in line]
    initMat.append(line);

print(initMat,len(initMat))

line = inputFile.readline();
myList = re.findall('\w+', line)
print(myList)

line = inputFile.read();
line = line.rstrip();
depth = int(line);
print(depth)
newDetailNode={};
if(day == 'Yesterday'):
    print("its yesterday, so need diff heuristics")
    for key, value in detailNode.items():
        newDetailNode[key] =((sum(detailNode.values())/(len(detailNode)))+value)/2
else:
    newDetailNode = detailNode;
print(newDetailNode)

