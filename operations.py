import read
import write

def addFurniture():
    status = True
    while status == True:
        employeeName = input("Enter your name (Employee Name)")
        furnitureValue = input("Is this piece of furniture already in the inventory? (yes/no) \n")
        if furnitureValue.lower() == "yes":
            checkId = input("Input the ID of the furniture \n")
            for line in range(len(read.inventory)):
                item = read.inventory[line]
                if checkId in item:
                    newCheckId = int(checkId) - 1
                    newQuantity = int(input("Enter the amount of new inventory \n"))
                    addedValue = int(read.inventory[newCheckId][checkId][2]) + newQuantity
                    read.inventory[newCheckId][checkId][2] = addedValue  
                    
                    write.newCheckId = newCheckId
                    write.newQuantity = newQuantity
                    
                    write.idAndQuantity.append([checkId,newQuantity])
                    
                        
        elif furnitureValue.lower() == "no":
            furnitureManufacturer = input("Enter Manufacturer Name: ")
            furnitureType = input("Enter Furniture Type: ")
            furnitureQuantity = int(input("Enter Quantity: "))
            furniturePrice = input("Enter Price per Unit: ")
            
            lastId = int(read.recentId) + 1
            
            read.inventory.append(
                {
                    str(lastId): [furnitureManufacturer, furnitureType, furnitureQuantity, furniturePrice]
                }
            )
        else:
            print("Error try again")
        
        checkStatus = input("Do you want to continue? (yes/no) \n")
        if checkStatus == "no":
            status = False