import datetime
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
