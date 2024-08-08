import datetime
import read
import write

vat = 0.13  
time = datetime.datetime.now()

furnitureList = []

recentId = 0

def addFurniture():
    Total = 0
    status = True
    furnitureListString = ""
    employeeName = input("Enter your name (Employee Name)")
    
    while status == True:
        try:
            while True:
                furnitureValue = input("Is this piece of furniture already in the inventory? (yes/no) \n")
                if furnitureValue.lower() == "yes" or furnitureValue.lower() == "no":
                    break
                else:
                    print("Invalid Input,Try again")
        except Exception as e:
            print(e)
        if furnitureValue.lower() == "yes":
                while True:
                    checkId = input("Input the ID of the furniture \n")
                    if checkId in read.inventory.keys():
                        break
                    else:
                        print("Item not found / doesn't Exist")
                for key in read.inventory:
                    if checkId in key:
                        newQuantity = int(input("Enter the amount of new inventory \n"))
                        
                        if newQuantity > 0:
                            addedValue = int(read.inventory[checkId][2]) + newQuantity
                            read.inventory[checkId][2] = addedValue  
                        
                            productName = read.inventory[checkId][1]
                            spaceForItems = 49 - len(productName) - len(str(newQuantity))
                            spaceForTotal = 50 - len("Total") - len(str(Total))
                        else:
                            print("Negative Number not allowed")
                            
                        Total += vat * (newQuantity * int(read.inventory[checkId][3].replace("\n","").replace("$","")))        
                        
                        furnitureList.append([productName + spaceForItems * " " + str(newQuantity)])
                        
        elif furnitureValue.lower() == "no":
            while True:
                try:
                    furnitureManufacturer = input("Enter Manufacturer Name: ")
                    furnitureType = input("Enter Furniture Type: ")
                    furnitureQuantity = int(input("Enter Quantity: "))
                    furniturePrice = input("Enter Price per Unit: ")
                    break
                except:
                    print("Invalid Input")
            lastId = int(read.recentId) + 1
            read.inventory.update({str(lastId): [furnitureManufacturer, furnitureType, furnitureQuantity, furniturePrice]})
        else:
            print("Error try again")
        while True:
            try:
                checkStatus = input("Do you want to continue? (yes/no) \n")
                break
            except:
                print("Invalid Input, Enter yes or no")
            
        if checkStatus == "no":
            status = False
            
    furnitureListString += "".join(str(furnitureList).replace("[","").replace("]","").replace("'","")).replace(", ","\n")
    
    write.receipt = [
                "="*50, "\n",
                21 * " " + "Receipt" + 20 * " ", "\n",
                " " * 20 + str(time).split()[0] + " " * 20,"\n",
                "Employee Name: " +  employeeName +  "\n",
                "Name of the furniture"  + " " * 20  +  "Quantity","\n",
                furnitureListString,"\n",
                "Total" + spaceForTotal * " " + "$" + str(Total),"\n",
                "\n",
                "="*50
                ]
    for item in write.receipt:
                print(item)    
                
    furnitureListString = ""

def sellFurniture():
    Total = 0
    shippingPrice = 0
    status = True
    furnitureListString = ""
    while True:
        try:
            customerName = input("Enter your name (Customer Name) \n")
            break
        except:
            print("Invalid Input")
    while status == True:
        while True:
            try:
                checkId = input("Input the ID of the furniture \n")
                if checkId in read.inventory.keys():
                    break
                else:
                    print("Item not found / doesn't Exist \n")
            except:
                print("Invalid Input")
        for key in read.inventory:
            if checkId in key:
                while True:
                    try:
                        while True:
                            try:
                                newQuantity = int(input("Enter the amount to be sold \n"))
                                
                                if newQuantity > int(read.inventory[checkId][2]):
                                    print("Not enough inventory")
                                elif newQuantity < 0:
                                    print("Negative Number not allowed")
                                elif newQuantity == 0:
                                    print("Zero not allowed")
                                else:
                                    break
                            except Exception as e:
                                print(e)
                        
                        if newQuantity > 0:
                            
                                shippingCheck = input("Do you need shipping? (yes/no) \n")
                                
                                if shippingCheck == "yes":
                                    shippingLocation = input("Enter shipping location \n 1 : Kathmandu \n 2 : Lalitpur \n 3 : Bhaktapur \n Enter the Corresponding Number")
                                else:
                                    break
                                
                                if shippingLocation == "1":
                                    shippingPrice = 150
                                    break
                                elif shippingLocation == "2":
                                    shippingPrice = 200
                                    break
                                elif shippingLocation == "3":
                                    shippingPrice = 250
                                    break
                                else:
                                    print("Invalid Input")

                    except:
                        print("Invalid Input")
                        
                subtractedValue = int(read.inventory[checkId][2]) - newQuantity
                
                if subtractedValue < 0:
                    print("Not enough inventory")
                    break
                read.inventory[checkId][2] = subtractedValue  
                
                Total += vat * (newQuantity * int(read.inventory[checkId][3].replace("\n","").replace("$",""))) + shippingPrice
                
                productName = read.inventory[checkId][1]
                
                spaceForItems = 49 - len(productName) - len(str(newQuantity))
                spaceForTotal = 49 - len("Total") - len(str(Total))
                
                productName = read.inventory[checkId][1]
                    
                checkStatus = input("Do you want to continue? (yes/no) \n")
                if checkStatus == "no":
                    status = False
             
    furnitureList.append([productName + spaceForItems * " " + str(newQuantity)])
    furnitureListString += "".join(str(furnitureList).replace("[","").replace("]","").replace("'","")).replace(", ","\n")
    write.receipt = [
    "="*50, "\n",
    21 * " " +  "Receipt" +  20 * " " +  "\n",
    " " * 20 + str(time).split()[0] + " " * 20,"\n",
    "Customer Name: " + customerName, "\n",
    "Name of the furniture" + " " * 20 + "Quantity","\n",
    furnitureListString,"\n",
    "Total" + spaceForTotal * " " + "$" + str(Total),"\n",
    "\n",
    "=" * 50 
    ]
    for item in write.receipt:
            print(item)
    furnitureListString = ""
                    
def updateInventory():
    updateInventoryFile = open("text.txt", 'w')
    for line in read.inventory:
            updateInventoryFile.write(str(line[0]) + ", " + str(read.inventory[line][0]) + ", " + str(read.inventory[line][1]) + ", " + str(read.inventory[line][2]) + ", " + str(read.inventory[line][3]))