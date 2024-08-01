import datetime

time = datetime.datetime.now()
receipt = None
timeString = str(time)
def writeReceipt():
    fileName = timeString + ".txt"
    with open(fileName,"w") as receiptFile:
        receiptFile.write(receipt)
