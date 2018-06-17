from collections import defaultdict
import copy
import sys
import re

class Graph:
	V = 0;
	
	def __init__(self,vertices):
		self.V = vertices;
		self.graph = defaultdict(list)
		self.map = {};
		self.availNbr = [];
		self.sump1 = 0;
		self.sump2 = 0;
		self.sell = {};
		self.chosen = '\0';

	def addEdge(self,u,v):
		self.graph[u].append(v)

def remove_visited(a,b,val): 
	#print("remove_visited");
#	#print(a,b,val);
	for k,v in b.items():
#		#print(k,v)
		if(v==val and k in a):
			a.remove(k);
#			#print(k);
#	#print(a)		
	return(sorted(a))	


def remove_duplicates(l):
#	#print(l)
	return list(set(l));

def recursiveCall(p1,p2,validMap,isP1,depth,DEPTH):
	global p1Sel;
	global p1Final;
	global p1FinalValues;
	global p2Sel;
	global p2Final;
	global p2FinalValues;
	#print("\n RECURSIVE CALL "+str(isP1)+" "+str(depth))

	#print(p1.availNbr,p2.availNbr,validMap)
	storeMap = copy.deepcopy(validMap);
	storep1 = copy.deepcopy(p1.availNbr);
	storep2 = copy.deepcopy(p2.availNbr);
	sump1 = copy.deepcopy(p1.sump1);
	sump2 = copy.deepcopy(p2.sump2);
	#print("storedmap"+str(storeMap));
	isValChosenAtDepth = 0;
	global first;	
	
	first+=1;
		
	if(isP1):
		if(first==1):
			for k in p1.availNbr:
				#print("imhere");
				recursiveCall.sel[k]=0;				
		#print("player 1 plays now"+" "+str(depth));
#		for k,v in p1.graph.items(): # p1.map see this 
		p1max = 0;
		for k in p1.availNbr:
			#print("player 1 plays noww"+" "+str(depth));
#			#print(hex(id(recursiveCall.sel['B'])))
			validMap = copy.deepcopy(storeMap);
			#print(recursiveCall.sel)
			#print("p1sel="+str(p1Sel));
			p1.availNbr = storep1;
			p2.availNbr = storep2;
			p1.sump1 = sump1;
			p2.sump2 = sump2;
			#print(p1.availNbr,p2.availNbr,validMap)
			if( (validMap[k]==1)  and (k in p1.availNbr)  ):
				if(depth==initDepth):
					##print(actualGraph.chosen,sel[actualGraph.chosen]);
					actualGraph.chosen = k;
					#print(actualGraph.chosen,recursiveCall.sel[actualGraph.chosen]);
				#print(k,p1.graph[k]) # prints k,v
#				#print(actualGraph.chosen,recursiveCall.sel[actualGraph.chosen]);
				p1.map[k] = 2;
				validMap[k] = 0;				
				#p1.availNbr.append(actualGraph.graph[k]);
				p1.availNbr = p1.availNbr+actualGraph.graph[k];
#				#print(type(p1.availNbr));
				#t = set(p1.availNbr);
				##print(t)
				p1.sump1 += priceDict[k];			
				#print("sump1 ="+str(p1.sump1)+" "+str(priceDict[k]));
#				#print(p1.availNbr)
				p1.availNbr = remove_duplicates(p1.availNbr);
#				#print(p1.availNbr)
				p1.availNbr = remove_visited(p1.availNbr,validMap,0);
				isValChosenAtDepth = 1;
				if(depth==DEPTH):
					#print("final sump1 "+str(p1.sump1)+" "+k);
					p1Final.append(k);

#					#print("final sump2"+str(sump2)+" "+k2);
					#print("\n D returning recursive call p1"+str(isP1)+" "+str(depth));
					#print("currentmaxp1="+str(p1max));
					#print("maxp1="+str(p1max)+" "+str(p1.sump2));
					#p1max=max(p1max,p1.sump1);
					#print(hex(id(recursiveCall.sel[actualGraph.chosen])))
					#print("chosen="+str(actualGraph.chosen)+" "+str(recursiveCall.sel[actualGraph.chosen]));
					temp = (max(recursiveCall.sel[actualGraph.chosen],p1.sump1))
					recursiveCall.sel[actualGraph.chosen] = temp;
#					#print(recursiveCall.sel['B'])
					#print(hex(id(recursiveCall.sel)))	
#					#print(hex(id(recursiveCall.sel['B'])))						
					p1Sel[actualGraph.chosen] = temp;
					p1FinalValues.append(temp);

				else:
#					#print("currentmax p1="+str(p1max));
					recursiveCall(copy.deepcopy(p1),copy.deepcopy(p2),copy.deepcopy(validMap),False,depth+1,DEPTH) # next plyr is p2
				if(depth==initDepth):
					recursiveCall.sel[k]=p1max;
	else:
		if(first==1):
			for k2 in p2.availNbr:
				recursiveCall.sel[k2]=0;
		#print("player 2 plays noww"+" "+str(depth));
#		#print(p2.graph.items())
#		for k,v in p2.graph.items():
		#print(p2.availNbr,len(p2.availNbr))
		p2max = 0;
		for k2 in p2.availNbr:
			#print(p2Final)
			#print(p2FinalValues)
			#print(p2Sel)
			#print("im in neew loop="+str(k2))
			if(depth==initDepth):
				actualGraph.chosen = k2;
				#print("im here");

			#print("player 2 plays nowwwww"+" "+str(depth));
			#print(actualGraph.chosen)
			validMap = copy.deepcopy(storeMap);
			p1.availNbr = storep1;
			p2.availNbr = storep2;
			p1.sump1 = sump1;
			p2.sump2 = sump2;
			#print(p1.availNbr,p2.availNbr,validMap,k2)
			#print(validMap[k2])
			if( (validMap[k2]==1) and (k2 in p2.availNbr) ):
				##print(k,v)
				#print(k2,p2.graph[k2]) # prints k,v
				p2.map[k2] = 3;
				validMap[k2] = 0;
				p2.sump2 += priceDict[k2];
				#print("sum= "+str(p2.sump2)+" "+str(priceDict[k2]));
				p2.availNbr = p2.availNbr + actualGraph.graph[k2];
				p2.availNbr = remove_duplicates(p2.availNbr);
				p2.availNbr = remove_visited(p2.availNbr,validMap,0);
				isValChosenAtDepth = 1;
				if(depth==DEPTH):
#					#print("final sump1 "+str(sump1)+" "+k);
					#print("final sump2 "+str(p2.sump2)+" "+k2);
					#print("\n D returning recursive call p2"+str(isP1)+" "+str(depth));
					#print("maxp2="+str(p2max)+" "+str(p2.sump2));
#					p2max=max(p2max,p2.sump2);
					
					temp = (max(recursiveCall.sel[actualGraph.chosen],p2.sump2))
					p2Final.append(k2)
					p2Sel[actualGraph.chosen] = temp;
					p2FinalValues.append(temp);
				else:
					recursiveCall(copy.deepcopy(p1),copy.deepcopy(p2),copy.deepcopy(validMap),True,depth+1,DEPTH) # next plyr i
				if(depth==initDepth):
					recursiveCall.sel[k2]=p2max;
					#print("k2 sel"+str(k2))
	if(isValChosenAtDepth==0):
		#print("final PASS");
		if(isP1):
			#print(p1.sump1);
			p1Final.append('PASS');
			temp = ((p1.sump1))
			p1FinalValues.append(temp)
		else:
			#print(p2.sump2);
			p2Final.append('PASS');
			temp = ((p2.sump2))
			p2FinalValues.append(temp)
	#print("\n returning recursive call "+str(isP1)+" "+str(depth));
	if(isP1):
		#print(p1max);
		return(p1max);
	else:
		#print(p2max)
		return(p2max);




## main code starts here

inputFile = open(sys.argv[2],'r');
fileOut = open("output.txt","w");

line = inputFile.readline();
day = line.rstrip()# to remove the \n charachter at the end of line
##print(day)

line = inputFile.readline();
player = line.rstrip();
##print(player)

if(player=='R2'):
	isP1 = False;
else:
	isP1 = True;

line = inputFile.readline();
myList = re.findall('\w+', line)

b = dict(zip(myList[::2], myList[1::2]))
detailNode = {k:int(v) for k,v in b.items()}
##print(detailNode)
keyList = list(detailNode.keys());
valuesList = list(detailNode.values());

initMat = []
for i in range(len(detailNode)):
    line = inputFile.readline();
    line = line.rstrip();
    line = re.findall('\w+',line)
    line = [int(k) for k in line]
    initMat.append(line);

##print(initMat,len(initMat))

line = inputFile.readline();
##print(line)
##print(line=='*\n')
completedList = [];
if(line=='*\n'):
	completedList.append('*');
else:
	completedList = re.findall('\w+', line)
#print(completedList)


numNodes = len(detailNode)
p1 = Graph(numNodes)
p2 = Graph(numNodes)
isEmpty = False;

from string import ascii_uppercase

validMap = {}

p1Sel = {};
p2Sel = {};

numTOalpha = {};
k=0;
for c in ascii_uppercase[:numNodes]:# and i in range(5):
	validMap[c] = 1;
	p1Sel[c] = 0;
	p2Sel[c] = 0;
	numTOalpha[k] = c;
	k+=1;

##print(numTOalpha)	

actualGraph = Graph(numNodes)
for i in range(numNodes):
	for j in range(numNodes):
		if(i!=j and initMat[i][j]==1):
			actualGraph.addEdge(numTOalpha[i],numTOalpha[j]);


#for k,v in (actualGraph.graph).items():
#	#print(k,v)

initDepth = 0;

newDetailNode={};
if(day == 'Yesterday'):
 #   #print("its yesterday, so need diff heuristics")
    for key, value in detailNode.items():
        newDetailNode[key] =((sum(detailNode.values())/(len(detailNode)))+value)/2
else:
    newDetailNode = detailNode;
##print(newDetailNode)

priceDict = newDetailNode;

if( completedList[0] != '*' ):
  
	initDepth = len(completedList);

	if(len(completedList)%2 == 0):
		for i in range(len(completedList)):
			if(isP1 == True):
				if((i%2)==0):
					p1.sump1 += priceDict[completedList[i]]
					p1.availNbr += actualGraph.graph[completedList[i]];
					validMap[completedList[i]]=0;
					#print(completedList[i],p1.availNbr)
				else:
					p2.sump2 += priceDict[completedList[i]];
					p2.availNbr += actualGraph.graph[completedList[i]];
					validMap[completedList[i]]=0;
					#print(completedList[i],p2.availNbr);
			else:
				if((i%2)==0):
					p2.sump2 += priceDict[completedList[i]];
					p2.availNbr += actualGraph.graph[completedList[i]];
					validMap[completedList[i]]=0;
				else:
					p1.sump1 += priceDict[completedList[i]];
					p1.availNbr += actualGraph.graph[completedList[i]];
					validMap[completedList[i]]=0;
	else:
		for i in range(len(completedList)):
			
			if(isP1 == True):
				if((i%2)==0):
					p2.sump2 += priceDict[completedList[i]];
					p2.availNbr = p2.availNbr + actualGraph.graph[completedList[i]];
					validMap[completedList[i]]=0;
					if(len(completedList)==1):
						p1.availNbr = copy.deepcopy(keyList);
				else:
					p1.sump1 += priceDict[completedList[i]];
					p1.availNbr += actualGraph.graph[completedList[i]];
					validMap[completedList[i]]=0;
			else:
				if((i%2)==0):
					p1.sump1 += priceDict[completedList[i]];
					p1.availNbr += list(actualGraph.graph[completedList[i]]);
					validMap[completedList[i]]=0;
					if(len(completedList)==1):
						p2.availNbr = copy.deepcopy(keyList);
				else:
					p2.sump2 += priceDict[completedList[i]];
					p2.availNbr += actualGraph.graph[completedList[i]];
					validMap[completedList[i]]=0;
else:
	p1.availNbr = copy.deepcopy(keyList);
	p2.availNbr = copy.deepcopy(keyList);
	p1.sump1 = 0;
	p2.sump2 = 0;
	initDepth = 0;
			
#print(p2.availNbr)	
p2.availNbr = remove_duplicates(p2.availNbr);
#print(p2.availNbr)	
p2.availNbr = remove_visited(p2.availNbr,validMap,0);
#print(p2.availNbr)	
p1.availNbr = remove_duplicates(p1.availNbr);
p1.availNbr = remove_visited(p1.availNbr,validMap,0);

line = inputFile.read();
line = line.rstrip();
depth = int(line);
##print(depth)
DEPTH = depth



first = 0; # simple counter to help check whether we are in first recursion or not.
p1Final = []; # list of alphabets at the depth specified if p1 has to play
p2Final = [];
p1FinalValues = []; # list of final utility values at the depth specified if p1 has to play, SECOND LINE OF THE OUTPUT
p2FinalValues = [];
recursiveCall.sel = {}; # function attribute for collecting the value


recursiveCall(p1,p2,validMap,isP1,initDepth,DEPTH) # PASS INITIAL DEPTH AS 2 IF 0 AND 1 DEPTH ARE ALREADY MENTIONED

if(isP1):# #print results for p1 player

	nextMove = list(p1Sel.values());
	nextMoveKeys = list(p1Sel.keys());
	#print(nextMoveKeys[nextMove.index(max(nextMove))])
	fileOut.write(nextMoveKeys[nextMove.index(max(nextMove))]+"\n");
	fileOut.write(str(p1FinalValues)[1:-1])
	#print(p1FinalValues);

else:
	nextMove = list(p2Sel.values());
	nextMoveKeys = list(p2Sel.keys());
	#print(nextMoveKeys[nextMove.index(max(nextMove))])
	#print(p2FinalValues);
	fileOut.write(nextMoveKeys[nextMove.index(max(nextMove))]+"\n");
	fileOut.write(str(p2FinalValues)[1:-1])











'''
#print(p1.sump1,p2.sump2);
#print(recursiveCall.sel)
##print(hex(id(recursiveCall.sel['B'])))
#print(p1Sel)	
#print(p1Final)
nextMove = list(p1Sel.values());
nextMoveKeys = list(p1Sel.keys());
#print(nextMove)
#print(nextMove.index(max(nextMove)))
#print(nextMoveKeys[nextMove.index(max(nextMove))])
#print(p1FinalValues);

#print("result for p2");

#print(p2Sel)	
#print(p2Final)
nextMove = list(p2Sel.values());
nextMoveKeys = list(p2Sel.keys());
#print(nextMove)
#print(nextMove.index(max(nextMove)))
#print(nextMoveKeys[nextMove.index(max(nextMove))])
#print(p2FinalValues);
'''
