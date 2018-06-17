from collections import defaultdict
import copy

validMap = {}
class Graph:
	V = 0;
	
	def __init__(self,vertices):
		self.V = vertices;
		self.graph = defaultdict(list)
		self.map = {};
		self.availNbr = {};
		self.sump1 = 0;
		self.sump2 = 0;
		self.sell = {};
		self.chosen = '\0';

	def addEdge(self,u,v):
		self.graph[u].append(v)

def remove_visited(a,b,val): 
	print("remove_visited");
#	print(a,b,val);
	for k,v in b.items():
#		print(k,v)
		if(v==val and k in a):
			a.remove(k);
#			print(k);
#	print(a)		
	return(sorted(a))	


def remove_duplicates(l):
#	print(l)
	return list(set(l));



priceDict={'A':10,'B':8,'C':10,'D':7}
initDepth = 1
first=0;	
#sel={}
p1Sel = {};
p2Sel = {};

def recursiveCall(p1,p2,validMap,isP1,depth,DEPTH):
	global p1Sel;
	global p1Final;
	global p1FinalValues;
	global p2Sel;
	global p2Final;
	global p2FinalValues;
	print("\n RECURSIVE CALL "+str(isP1)+" "+str(depth))

	print(p1.availNbr,p2.availNbr,validMap)
	storeMap = copy.deepcopy(validMap);
	storep1 = copy.deepcopy(p1.availNbr);
	storep2 = copy.deepcopy(p2.availNbr);
	sump1 = copy.deepcopy(p1.sump1);
	sump2 = copy.deepcopy(p2.sump2);
	print("storedmap"+str(storeMap));
	isValChosenAtDepth = 0;
	global first;	
	
	first+=1;
		
	if(isP1):
		if(first==1):
			for k in p1.availNbr:
				print("imhere");
				recursiveCall.sel[k]=0;				
		print("player 1 plays now"+" "+str(depth));
#		for k,v in p1.graph.items(): # p1.map see this 
		p1max = 0;
		for k in p1.availNbr:
			print("player 1 plays noww"+" "+str(depth));
#			print(hex(id(recursiveCall.sel['B'])))
			validMap = copy.deepcopy(storeMap);
			print(recursiveCall.sel)
			print("p1sel="+str(p1Sel));
			p1.availNbr = storep1;
			p2.availNbr = storep2;
			p1.sump1 = sump1;
			p2.sump2 = sump2;
			print(p1.availNbr,p2.availNbr,validMap)
			if( (validMap[k]==1)  and (k in p1.availNbr)  ):
				if(depth==initDepth):
					#print(actualGraph.chosen,sel[actualGraph.chosen]);
					actualGraph.chosen = k;
					print(actualGraph.chosen,recursiveCall.sel[actualGraph.chosen]);
				print(k,p1.graph[k]) # prints k,v
#				print(actualGraph.chosen,recursiveCall.sel[actualGraph.chosen]);
				p1.map[k] = 2;
				validMap[k] = 0;				
				#p1.availNbr.append(actualGraph.graph[k]);
				p1.availNbr = p1.availNbr+actualGraph.graph[k];
#				print(type(p1.availNbr));
				#t = set(p1.availNbr);
				#print(t)
				p1.sump1 += priceDict[k];			
				print("sump1 ="+str(p1.sump1)+" "+str(priceDict[k]));
#				print(p1.availNbr)
				p1.availNbr = remove_duplicates(p1.availNbr);
#				print(p1.availNbr)
				p1.availNbr = remove_visited(p1.availNbr,validMap,0);
				isValChosenAtDepth = 1;
				if(depth==DEPTH):
					print("final sump1 "+str(p1.sump1)+" "+k);
					p1Final.append(k);

#					print("final sump2"+str(sump2)+" "+k2);
					print("\n D returning recursive call p1"+str(isP1)+" "+str(depth));
					print("currentmaxp1="+str(p1max));
					print("maxp1="+str(p1max)+" "+str(p1.sump2));
					#p1max=max(p1max,p1.sump1);
					print(hex(id(recursiveCall.sel[actualGraph.chosen])))
					print("chosen="+str(actualGraph.chosen)+" "+str(recursiveCall.sel[actualGraph.chosen]));
					temp = (max(recursiveCall.sel[actualGraph.chosen],p1.sump1))
					recursiveCall.sel[actualGraph.chosen] = temp;
#					print(recursiveCall.sel['B'])
					print(hex(id(recursiveCall.sel)))	
#					print(hex(id(recursiveCall.sel['B'])))						
					p1Sel[actualGraph.chosen] = temp;
					p1FinalValues.append(temp);

				else:
#					print("currentmax p1="+str(p1max));
					recursiveCall(copy.deepcopy(p1),copy.deepcopy(p2),copy.deepcopy(validMap),False,depth+1,DEPTH) # next plyr is p2
				if(depth==initDepth):
					recursiveCall.sel[k]=p1max;
	else:
		if(first==1):
			for k2 in p2.availNbr:
				recursiveCall.sel[k2]=0;
		print("player 2 plays noww"+" "+str(depth));
#		print(p2.graph.items())
#		for k,v in p2.graph.items():
		print(p2.availNbr,len(p2.availNbr))
		p2max = 0;
		for k2 in p2.availNbr:
			print(p2Final)
			print(p2FinalValues)
			print(p2Sel)
			print("im in neew loop="+str(k2))
			if(depth==initDepth):
				actualGraph.chosen = k2;
				print("im here");

			print("player 2 plays nowwwww"+" "+str(depth));
			print(actualGraph.chosen)
			validMap = copy.deepcopy(storeMap);
			p1.availNbr = storep1;
			p2.availNbr = storep2;
			p1.sump1 = sump1;
			p2.sump2 = sump2;
			print(p1.availNbr,p2.availNbr,validMap,k2)
			print(validMap[k2])
			if( (validMap[k2]==1) and (k2 in p2.availNbr) ):
				#print(k,v)
				print(k2,p2.graph[k2]) # prints k,v
				p2.map[k2] = 3;
				validMap[k2] = 0;
				p2.sump2 += priceDict[k2];
				print("sum= "+str(p2.sump2)+" "+str(priceDict[k2]));
				p2.availNbr = p2.availNbr + actualGraph.graph[k2];
				p2.availNbr = remove_duplicates(p2.availNbr);
				p2.availNbr = remove_visited(p2.availNbr,validMap,0);
				isValChosenAtDepth = 1;
				if(depth==DEPTH):
#					print("final sump1 "+str(sump1)+" "+k);
					print("final sump2 "+str(p2.sump2)+" "+k2);
					print("\n D returning recursive call p2"+str(isP1)+" "+str(depth));
					print("maxp2="+str(p2max)+" "+str(p2.sump2));
#					p2max=max(p2max,p2.sump2);
					
					temp = (max(recursiveCall.sel[actualGraph.chosen],p2.sump2))
					p2Final.append(k2)
					p2Sel[actualGraph.chosen] = temp;
					p2FinalValues.append(temp);
				else:
					recursiveCall(copy.deepcopy(p1),copy.deepcopy(p2),copy.deepcopy(validMap),True,depth+1,DEPTH) # next plyr i
				if(depth==initDepth):
					recursiveCall.sel[k2]=p2max;
					print("k2 sel"+str(k2))
	if(isValChosenAtDepth==0):
		print("final PASS");
		if(isP1):
			print(p1.sump1);
			p1Final.append('PASS');
			temp = ((p1.sump1))
			p1FinalValues.append(temp)
		else:
			print(p2.sump2);
			p2Final.append('PASS');
			temp = ((p2.sump2))
			p2FinalValues.append(temp)
	print("\n returning recursive call "+str(isP1)+" "+str(depth));
	if(isP1):
		print(p1max);
		return(p1max);
	else:
		print(p2max)
		return(p2max);




#p1 = copy.deepcopy(actualGraph)
#p2 = copy.deepcopy(actualGraph)
		 
numNodes = 4;		
p1 = Graph(numNodes)
p2 = Graph(numNodes)

actualGraph = Graph(numNodes)
actualGraph.addEdge('A','B')
actualGraph.addEdge('A','C')
actualGraph.addEdge('B','A')
actualGraph.addEdge('B','D')
actualGraph.addEdge('C','A')
actualGraph.addEdge('C','D')
actualGraph.addEdge('D','B')
actualGraph.addEdge('D','C')

from string import ascii_uppercase

for c in ascii_uppercase[:numNodes]:# and i in range(5):
	validMap[c] = 1;
	p1Sel[c] = 0;
	p2Sel[c] = 0;

print(validMap);
#print(type(p1.graph))

#for k,v in (actualGraph.graph).items():
#	print(k,v)


p1 = copy.deepcopy(actualGraph)
p2 = copy.deepcopy(actualGraph)
p1.map = copy.deepcopy(validMap)
p2.map = copy.deepcopy(validMap)

#print(p1.map,p2.map)

p1.map['A'] = 2;
#print(actualGraph.graph['D'])
p1.availNbr = actualGraph.graph['A'];
#p2.map['C'] = 3;
#p2.availNbr = actualGraph.graph['C'];
p2.availNbr = ['B','C','D'];  # charan TBD put everything else as no new selection 
validMap['A'] = 0;
#validMap['C'] = 0;
DEPTH = 3; # 0 TO 4
p1.sump1 = 10
#p2.sump2 = 10
first = 0;
p1Final = [];
p2Final = [];
p1FinalValues = [];
p2FinalValues = [];
recursiveCall.sel = {}

recursiveCall(p1,p2,validMap,False,1,DEPTH) # PASS INITIAL DEPTH AS 2 IF 0 AND 1 DEPTH ARE ALREADY MENTIONED

print(p1.sump1,p2.sump2);
print(recursiveCall.sel)
#print(hex(id(recursiveCall.sel['B'])))
print(p1Sel)	
print(p1Final)
nextMove = list(p1Sel.values());
nextMoveKeys = list(p1Sel.keys());
print(nextMove)
print(nextMove.index(max(nextMove)))
print(nextMoveKeys[nextMove.index(max(nextMove))])
print(p1FinalValues);

print("result for p2");

print(p2Sel)	
print(p2Final)
nextMove = list(p2Sel.values());
nextMoveKeys = list(p2Sel.keys());
print(nextMove)
print(nextMove.index(max(nextMove)))
print(nextMoveKeys[nextMove.index(max(nextMove))])
print(p2FinalValues);
