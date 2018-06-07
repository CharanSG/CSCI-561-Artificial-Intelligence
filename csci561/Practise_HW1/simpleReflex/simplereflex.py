import sys

#inputFile=open(sys.argv[2],'r')
# /home/ccc_v1_s81247__50528/asn29297_10/asn29298_1/asnlib.0/test1.txt 
# ccc_v1_w_NjNiZ_87225@runweb8:~$ echo $ASNLIB                                                                                            #/home/ccc_v1_s81247__50528/asn29297_10/asn29298_1/asnlib.0 

#print(sys.argv[2])

inputFile = open(sys.argv[2],'r');
file = open("output.txt","w");
#num_lines = sum(1 for line in open(sys.argv[2]))
#print(num_lines)
for line in inputFile:    
    #print(line)
    line = line.rstrip()# to remove the \n charachter at the end of line
    myList = line.split(',')
    print(myList)
    if(myList[1] == 'Dirty'):
        print("Suck");
        file.write("Suck\n")
    elif(myList[0]=='A'):
        print('Right');
        file.write("Right\n")
    elif(myList[0]=='B'):
        print('Left');
        file.write("Left\n")
    
file.close()
inputFile.close()
