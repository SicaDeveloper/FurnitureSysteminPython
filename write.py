import datetime
import read

time = datetime.datetime.now()
receipt = []
timeString = str(time).split()[0] + " " + str(time).split()[1].replace(":","-") + " Receipt"

"""
Writes the current receipt to a text file.

The file name is created based on the current time with the entire receipt in it.
"""
def writeReceipt():
    fileName = timeString + ".txt"
    receiptFile = open(fileName, "w")
    for item in receipt:
        receiptFile.write(str(item))
    receiptFile.close()
    
def updateInventory():
    """
    Updates the inventory file 'text.txt' with the current inventory by concatenating the new inventory.

    """
    updateInventoryFile = open("text.txt", 'w')
    for line in read.inventory:
            updateInventoryFile.write(str(line[0]) + "," + str(read.inventory[line][0]) + "," + str(read.inventory[line][1]) + "," + str(read.inventory[line][2]) + "," + str(read.inventory[line][3]))
