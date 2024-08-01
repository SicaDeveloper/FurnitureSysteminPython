import datetime

time = datetime.datetime.now()
receipt = None
timeString = str(time).replace() + " Receipt"
def writeReceipt():
    fileName = timeString + ".txt"
    receiptFile = open(fileName, "w")
    receiptFile.write(receipt)
    receiptFile.close()
