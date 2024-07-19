import datetime

id = 0
manufacturer = ""
productName = ""
availableQuantity = ""
pricePerUnit = ""
orderStatus = True
inventory = {}
inventoryList = []
inventoryFile = 'text.txt'
vat = 0.13
status = True
time = datetime.datetime.now()

with open(inventoryFile, 'r') as readFile:
    for line in readFile:
        segment = line.strip().split(',')
        inventoryList.append    ({
        'id': int(segment[0]),
        'manufacturer': segment[1],
        'product_name': segment[2],
        'quantity': int(segment[3]),
        'price': segment[4]
        })
last_id = int(segment[0])

def readInventory():
    for line in inventoryList:
        print(', '.join(str(x) for x in line.values()))

def updateInventory():
    new_id = last_id + 1
    inventory.update({'id': new_id})
    inventory.update({'manufacturer' : manufacturer})
    inventory.update({'productName' : productName})
    inventory.update({'quantity' : availableQuantity})
    inventory.update({'pricePerUnit' : pricePerUnit})
    writeInv = open(inventoryFile, 'a')
    writeValue =  f"{new_id},{manufacturer},{productName},{quantity},{pricePerUnit}"
    writeInv.write('\n' + writeValue)
    writeInv.close()
        
    
def purchaseManufacturer():  
    transaction = {}
    while orderStatus == True:
            try:
                id = int(input("Enter ID").strip())
                quantity = int(input("Enter Quantity").strip())
                
            except :
                print("Item not found / doesn't Exist")         
            
while status == True:
    question = input('Nepal Furnishings Pvt Ltd \n Press 1 for Inventory \n Press 2 to purchase from Manufacturer \n Press 3 to process sales \n Press 4 to update Inventory \n Press 5 to Exit \n')
    if question == '1':
        readInventory()
    elif question == '2':
       purchaseManufacturer()
    elif question == '3':
        pass
    elif question == '4':
        manufacturer = input("Enter Manufacturer Name")
        productName = input("Enter Product Name")
        quantity = int(input("Enter Quantity Bought"))
        pricePerUnit = input("Enter pricePerUnit")
        updateInventory()
    elif question == '5':
        status = False
    else:
        print('Invalid Input')
        