import datetime
import read
import write

vat = 0.13  
time = datetime.datetime.now()

furnitureList = []

def addFurniture():
    Total = 0
    status = True
    furnitureListString = ""
    try:
        employeeName = input("Enter your name (Employee Name)")
    except ValueError:
        print("Invalid Input")
    while status == True:
        furnitureValue = input("Is this piece of furniture already in the inventory? (yes/no) \n")
        if furnitureValue.lower() == "yes":
            try:
                checkId = input("Input the ID of the furniture \n")
            except ValueError:
                print("Invalid Input, Not a number")
            checkIdValue = False
            for key in read.inventory:
                if checkId in key:
                    newQuantity = int(input("Enter the amount of new inventory \n"))
                    addedValue = int(read.inventory[checkId][2]) + newQuantity
                    read.inventory[checkId][2] = addedValue  
                    
                    productName = read.inventory[checkId][1]
                    spaceForItems = 49 - len(productName) - len(str(newQuantity))
                    spaceForTotal = 50 - len("Total") - len(str(Total))

                    checkIdValue = True
                    
            Total += vat * (newQuantity * int(read.inventory[checkId][3].replace("\n","").replace("$","")))        
                
            furnitureList.append([productName + spaceForItems * " " + str(newQuantity)])

                       
            if checkIdValue == False:
                print("Item not found / doesn't Exist")
        elif furnitureValue.lower() == "no":
            try:
                furnitureManufacturer = input("Enter Manufacturer Name: ")
                furnitureType = input("Enter Furniture Type: ")
                furnitureQuantity = int(input("Enter Quantity: "))
                furniturePrice = input("Enter Price per Unit: ")
            except ValueError:
                print("Invalid Input")
            lastId = int(read.recentId) + 1
            read.inventory.update({str(lastId): [furnitureManufacturer, furnitureType, furnitureQuantity, furniturePrice]})
        else:
            print("Error try again")
        try:
            checkStatus = input("Do you want to continue? (yes/no) \n")
        except ValueError:
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
    try:
        customerName = input("Enter your name (Customer Name) \n")
    except ValueError:
        print("Invalid Input")
    while status == True:
        try:
            checkId = input("Input the ID of the furniture \n")
        except ValueError:
            print("Invalid Input")
            for key in read.inventory:
                if checkId in key:
                    try:
                        newQuantity = int(input("Enter the amount of sold \n"))
                        shippingCheck = input("Do you need shipping? (yes/no) \n")
                    except ValueError:
                        print("Invalid Input")
                    if shippingCheck == "yes":
                        shippingLocation = input("Enter shipping location \n 1 : Kathmandu \n 2 : Lalitpur \n 3 : Bhaktapur \n")
                        if shippingLocation.lower() == "kathmandu":
                            shippingPrice = 150
                        elif shippingLocation.lower() == "lalitpur":
                            shippingPrice = 200
                        elif shippingLocation.lower() == "bhaktapur":
                            shippingPrice = 250
                        else:
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