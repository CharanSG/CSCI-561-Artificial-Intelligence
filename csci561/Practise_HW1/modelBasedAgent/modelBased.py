import sys
print(sys.argv[2])

inputFile = open(sys.argv[2],'r');
file = open("output.txt","w");

model = {'A':None,'B':None}

for line in inputFile:    
    
    line = line.rstrip()# to remove the \n charachter at the end of line
    myList = line.split(',')
    print(myList)
    
    if( myList[1] == 'Dirty' ):        
        print("Suck");
        file.write("Suck\n");
        model[myList[0]] = 'Clean';
        
    elif( (myList[0]=='A') ):
        model['A'] = 'Clean';
        if(model['B'] != 'Clean'): 
            print('Right');
            file.write("Right\n");
        else:
            print('NoOp');
            file.write("NoOp\n");
        
    elif( myList[0]=='B'):
        model['B'] = 'Clean';
        if(model['A'] != 'Clean'):
            print('Left');
            file.write("Left\n")            
        else:           
            print('NoOp');
            file.write("NoOp\n");
    
    elif( (model['A'] == 'Clean')and (model['B'] == 'Clean') ):
        print('NoOp');
        file.write("NoOp\n");
    
file.close()
inputFile.close()
