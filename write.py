import datetime

time = datetime.datetime.now()
receipt = None

def writeReceipt():
    fileName = str(time)
    with open(fileName,"w") as receiptFile:
        receiptFile.write(receipt)