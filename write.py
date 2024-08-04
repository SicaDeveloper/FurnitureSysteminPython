import datetime

time = datetime.datetime.now()
receipt = None
timeString = str(time).split()[0] + " " + str(time).split()[1].replace(":","-") + " Receipt"
def writeReceipt():
    fileName = timeString + ".txt"
    receiptFile = open(fileName, "w")
    for item in receipt:
        receiptFile.write(str(item))
    receiptFile.close()
