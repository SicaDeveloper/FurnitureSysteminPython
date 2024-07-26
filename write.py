import datetime
import read

vat = 0.13
time = datetime.datetime.now()

newCheckId = None
newQuantity = None

idAndQuantity = []
receipt = []

def writeReceipt():
    receiptList = [
        print("="*50,"\nReceipt\n"),
        print(idAndQuantity),
        print("="*50)
        ]