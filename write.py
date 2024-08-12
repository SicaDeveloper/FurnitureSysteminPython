import datetime
import read

time = datetime.datetime.now()
receipt = []
timeString = str(time).split()[0] + " " + str(time).split()[1].replace(":","-") + " Receipt"

"""
Writes the current receipt to a text file.

The file name is generated based on the current time and has a .txt extension.
The receipt is written to the file line by line, with each item in the receipt
being written as a string.
"""
def writeReceipt():
    fileName = timeString + ".txt"
    receiptFile = open(fileName, "w")
    for item in receipt:
        receiptFile.write(str(item))
    receiptFile.close()

"""
Updates the inventory file 'text.txt' by rewriting all items in the current inventory.

Iterates over each item in the inventory, writing its details to the file in a comma-separated format.
The details include the item's ID, name, type, quantity, and price.

No parameters are taken, and no value is returned.
"""
def updateInventory():
    updateInventoryFile = open("text.txt", 'w')
    for line in read.inventory:
            updateInventoryFile.write(str(line[0]) + "," + str(read.inventory[line][0]) + "," + str(read.inventory[line][1]) + "," + str(read.inventory[line][2]) + "," + str(read.inventory[line][3] + "\n"))
