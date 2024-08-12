import operations
inventory = {}
try:
    inventoryFile = open("text.txt",'r')
    for line in inventoryFile:
        segment = line.split(',')
        inventory.update({segment[0]:[segment[1],segment[2],segment[3],segment[4]]})
    #setting the final id in the text file
    operations.recentId = int(segment[0])
except:
    print("File not found,please create the required file [text.txt]")
    
"""
Reads the contents of the inventory file 'text.txt' and prints each line.

No parameters are taken, and no value is returned.
"""
def readInventory():
    try:
        inventoryFile = open("text.txt",'r')
    except:
        print("File not found,please create the required file [text.txt]")
    for line in inventoryFile:
        print(line)