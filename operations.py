import datetime
import read
import write

vat = 0.13  
time = datetime.datetime.now()

def addFurniture():
    status = True
    employeeName = input("Enter your name (Employee Name)")
    while status == True:
        furnitureValue = input("Is this piece of furniture already in the inventory? (yes/no) \n")
        if furnitureValue.lower() == "yes":
            checkId = input("Input the ID of the furniture \n")
            for key in read.inventory:
                if checkId in key:
                    newQuantity = int(input("Enter the amount of new inventory \n"))
                    addedValue = int(read.inventory[checkId][2]) + newQuantity
                    read.inventory[checkId][2] = addedValue  
                    
                    productName = read.inventory[checkId][1]
                    
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
            
    write.receipt = [
        "="*50, "\nReceipt\n",
            time.year,time.month,time.day,"\n",
            employeeName,"\n"
            FurnitureList,"\n"
            addedValue,"\n"
            "\n",
            "="*50
    ]