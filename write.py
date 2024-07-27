import datetime
import read
import operations

vat = 0.13
now = datetime.now()
time = now.date()   

newCheckId = None
newQuantity = None

idAndQuantity = []

nameOfIdList = []
newQuantityList = []

receiptList = []

def writeReceipt():
    for item in idAndQuantity:
        nameOfIdList.append(read.inventory[int(item[0])-1][item[0]][0])
        newQuantityList.append(item[1])

    for items in range(len(nameOfIdList)):
        space = 50 - len(nameOfIdList[items]) + len(str(newQuantityList[items]))
        receiptList.append([nameOfIdList[items]," " * space,newQuantityList[items]])
        
    receipt = [
            "="*50, "\nReceipt\n",
            time,"\n",
            receiptList,"\n",
            "="*50
            ]
    
    for item in receipt:
        print(item)
    
    receipt.clear()
    nameOfIdList.clear()
    newQuantityList.clear()
    idAndQuantity.clear()
    receiptList.clear()