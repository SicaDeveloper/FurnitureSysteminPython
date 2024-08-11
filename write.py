import datetime
import read
question = None

time = datetime.datetime.now()
receipt = []
timeString = str(time).split()[0] + " " + str(time).split()[1].replace(":","-") + " Receipt"
def writeReceipt():
    if question == '2': 
        fileName = timeString + " Purchase" + ".txt"
    elif question == '3':
        fileName = timeString + " Sales" + ".txt"
    else:
        fileName = timeString + ".txt"
    receiptFile = open(fileName, "w")
    for item in receipt:
        receiptFile.write(str(item))
    receiptFile.close()
    
def updateInventory():
    updateInventoryFile = open("text.txt", 'w')
    for line in read.inventory:
            updateInventoryFile.write(str(line[0]) + "," + str(read.inventory[line][0]) + "," + str(read.inventory[line][1]) + "," + str(read.inventory[line][2]) + "," + str(read.inventory[line][3] + "\n"))
