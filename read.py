inventory = {}

inventoryFile = open("text.txt",'r')

for line in inventoryFile:
    segment = line.split(',')
    inventory.update({segment[0]:[segment[1],segment[2],segment[3],segment[4]]})
recentId = int(segment[0])
def readInventory():
    for line in inventory:
        print(inventory[line])
    