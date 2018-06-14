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

	def addEdge(self,u,v):
		self.graph[u].append(v)

def remove_visited(a,b,val): 
	print("remove_visited");
	print(a,b,val);
	for k,v in b.items():
		print(k,v)
		if(v==val and k in a):
			a.remove(k);
			print(k);
	print(a)		
	return(a)	


def remove_duplicates(l):
#	print(l)
	return list(set(l));
	
def recursiveCall(p1,p2,validMap,isP1,depth):

	print("\n RECURSIVE CALL "+str(isP1)+" "+str(depth))

	print(p1.availNbr,p2.availNbr,validMap)

	storeMap = copy.deepcopy(validMap);
	storep1 = copy.deepcopy(p1.availNbr);
	storep2 = copy.deepcopy(p2.availNbr);
	print("storedmap"+str(storeMap));

	if(isP1):
		print("player 1 plays now"+" "+str(depth));
#		for k,v in p1.graph.items(): # p1.map see this 
		for k in p1.availNbr:
			validMap = copy.deepcopy(storeMap);
			p1.availNbr = storep1;
			p2.availNbr = storep2;
			print(p1.availNbr,p2.availNbr,validMap)
			if( (validMap[k]==1)  and (k in p1.availNbr)  ):
				print(k,p1.graph[k]) # prints k,v
				p1.map[k] = 2;
				validMap[k] = 0;				
				#p1.availNbr.append(actualGraph.graph[k]);
				p1.availNbr = p1.availNbr+actualGraph.graph[k];
#				print(type(p1.availNbr));
				#t = set(p1.availNbr);
				#print(t)
				p1.availNbr = remove_duplicates(p1.availNbr);
				p1.availNbr = remove_visited(p1.availNbr,validMap,0);
				recursiveCall(copy.deepcopy(p1),copy.deepcopy(p2),copy.deepcopy(validMap),False,depth+1) # next plyr is p2
	else:
		print("player 2 plays noww"+" "+str(depth));
#		print(p2.graph.items())
#		for k,v in p2.graph.items():
		print(p2.availNbr,len(p2.availNbr))
		for k2 in p2.availNbr:
			validMap = copy.deepcopy(storeMap);
			p1.availNbr = storep1;
			p2.availNbr = storep2;
			print(p1.availNbr,p2.availNbr,validMap,k2)
			print(validMap[k2])
			if( (validMap[k2]==1) and (k2 in p2.availNbr) ):
				#print(k,v)
				print(k2,p2.graph[k2]) # prints k,v
				p2.map[k2] = 3;
				validMap[k2] = 0;
				p2.availNbr = p2.availNbr + actualGraph.graph[k2];
				p2.availNbr = remove_duplicates(p2.availNbr);
				p2.availNbr = remove_visited(p2.availNbr,validMap,0);
				recursiveCall(copy.deepcopy(p1),copy.deepcopy(p2),copy.deepcopy(validMap),True,depth+1) # next plyr i
	print("\n returning recursive call "+str(isP1)+" "+str(depth));


#p1 = copy.deepcopy(actualGraph)
#p2 = copy.deepcopy(actualGraph)
		 
		
p1 = Graph(5)
p2 = Graph(5)

actualGraph = Graph(5)
actualGraph.addEdge('A','B')
actualGraph.addEdge('A','C')
actualGraph.addEdge('B','A')
actualGraph.addEdge('B','C')
actualGraph.addEdge('B','D')
actualGraph.addEdge('B','E')
actualGraph.addEdge('C','A')
actualGraph.addEdge('C','B')
actualGraph.addEdge('C','E')
actualGraph.addEdge('D','B')
actualGraph.addEdge('D','E')
actualGraph.addEdge('E','B')
actualGraph.addEdge('E','C')
actualGraph.addEdge('E','D')

from string import ascii_uppercase

for c in ascii_uppercase[:5]:# and i in range(5):
	validMap[c] = 1;

print(validMap);
print(type(p1.graph))

for k,v in (actualGraph.graph).items():
	print(k,v)


p1 = copy.deepcopy(actualGraph)
p2 = copy.deepcopy(actualGraph)
p1.map = copy.deepcopy(validMap)
p2.map = copy.deepcopy(validMap)

print(p1.map,p2.map)

p1.map['D'] = 2;
#print(actualGraph.graph['D'])
p1.availNbr = actualGraph.graph['D'];
p2.map['C'] = 3;
p2.availNbr = actualGraph.graph['C'];
validMap['D'] = 0;
validMap['C'] = 0;

recursiveCall(p1,p2,validMap,True,3)

	
