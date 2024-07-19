inventory = []

inventoryFile = open("text.txt",'r')

for line in inventoryFile:
    segment = line.split(',')
    inventory.append(
        {
            segment[0] : [segment[1],segment[2],int(segment[3]),segment[4].strip()]
        }
    )
recentId = int(segment[0])
def readInventory():
    for line in inventory:
        print(line)
    