import datetime
import read
import write

vat = 0.13  
time = datetime.datetime.now()

furnitureList = []

def addFurniture():
    Total = 0
    status = True
    employeeName = input("Enter your name (Employee Name)")
    while status == True:
        furnitureValue = input("Is this piece of furniture already in the inventory? (yes/no) \n")
        if furnitureValue.lower() == "yes":
            checkId = input("Input the ID of the furniture \n")
            for key in read.inventory:
                checkIdValue = False
                if checkId in key:
                    newQuantity = int(input("Enter the amount of new inventory \n"))
                    addedValue = int(read.inventory[checkId][2]) + newQuantity
                    read.inventory[checkId][2] = addedValue  
                    
                    productName = read.inventory[checkId][1]
                    space = 50 - len(productName) - len(str(newQuantity))
                    
                    furnitureList.append([productName,space * "",newQuantity,"\n"])
                    Total += newQuantity * int(read.inventory[checkId][3].replace("\n","").replace("$",""))
                    checkIdValue = True
                    
            if checkIdValue == False:
                print("Item not found / doesn't Exist")
            write.receipt = [
                "="*50, "\nReceipt\n",
                    str(time.year) + str(time.month) + str(time.day),"\n",
                    employeeName,"\n",
                    furnitureList,"\n",
                    Total,"\n",
                    "\n",
                    "="*50
                ]
                    
        elif furnitureValue.lower() == "no":
            furnitureManufacturer = input("Enter Manufacturer Name: ")
            furnitureType = input("Enter Furniture Type: ")
            furnitureQuantity = int(input("Enter Quantity: "))
            furniturePrice = input("Enter Price per Unit: ")
            
            lastId = int(read.recentId) + 1
            read.inventory.update({str(lastId): [furnitureManufacturer, furnitureType, furnitureQuantity, furniturePrice]})
        else:
            print("Error try again")
        checkStatus = input("Do you want to continue? (yes/no) \n")
        if checkStatus == "no":
            status = False
    for item in write.receipt:
                print(item)    

def sellFurniture():
    status = True
    customerName = input("Enter your name (Customer Name)")
    while status == True:
        furnitureValue = input("Is this piece of furniture already in the inventory? (yes/no) \n")
        if furnitureValue.lower() == "yes":
            checkId = input("Input the ID of the furniture \n")
            for key in read.inventory:
                if checkId in key:
                    newQuantity = int(input("Enter the amount of new inventory \n"))
                    subtractedValue = int(read.inventory[checkId][2]) - newQuantity
                    read.inventory[checkId][2] = subtractedValue  
                    
                    productName = read.inventory[checkId][1]
                    space = 50 - len(productName) - len(str(newQuantity))
                    
                    furnitureList.append([productName,space * "",newQuantity,"\n"])
                    
                    write.receipt = [
                        "="*50, "\nReceipt\n",
                            time.year,time.month,time.day,"\n",
                            customerName,"\n",
                            furnitureList,"\n",
                            "\n",
                            "\n",
                            "="*50
                     ]
                    