import datetime
import read
import write

vat = 0.13  
time = datetime.datetime.now()


recentId = 0

def addFurniture():
    """
    Adds a piece of furniture to the inventory.

    Asks the user for the employee name and whether the piece of furniture is already in the inventory.
    
    Checks if the piece of furniture is already in the inventory and calls the addOldFurniture function if it is. 
    Otherwise it calls the function addNewFurniture.
    """
    while True:
        employeeName = input("Enter your name (Employee Name) \n")
        if type(employeeName) == str:
            break
        else:
            print("Please Enter a valid name \n")
    while True:
                furnitureCheckValue = input("Is this piece of furniture already in the inventory? (yes/no) \n")
                if furnitureCheckValue.lower() == "yes" or furnitureCheckValue.lower() == "no":
                    break
                else:
                    print("Invalid Input,Try again \n")
    if furnitureCheckValue.lower() == "yes":
        addOldFurniture(employeeName)
    elif furnitureCheckValue.lower() == "no":
        addNewFurniture()
    else:
        print("Invalid Input,Try again \n")
def addOldFurniture(employeeName):
    Total = 0
    status = True
    furnitureListString = ""
    furnitureList = []
    while status == True:
        while True:
            checkId = input("Input the ID of the furniture \n")
            if checkId in read.inventory.keys():
                break
            else:
                print("Item not found / doesn't Exist")
        for key in read.inventory:
            if checkId in key:
                while True:
                    try:
                        newQuantity = int(input("Enter the amount of new inventory \n"))
                        break
                    except:
                        print("Invalid Input \n")
                        
                if newQuantity > 0:
                    addedValue = int(read.inventory[checkId][2]) + newQuantity
                    read.inventory[checkId][2] = addedValue  
                    productName = read.inventory[checkId][1]
                    
                else:
                    print("Negative Number not allowed \n")
                    
                Total += vat * (newQuantity * int(read.inventory[checkId][3].replace("\n","").replace("$","")))        
                
                spaceForItems = 50 - len(productName) - len(str(newQuantity))
                spaceForTotal = 50 - len("Total") - len(str(Total))
                
        furnitureList.append([productName + spaceForItems * " " + str(newQuantity)])    
        while True:
                try:
                    checkStatus = input("Do you want to continue? (yes/no) \n")
                    break
                except:
                    print("Invalid Input, Enter yes or no \n")
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
        
    write.writeReceipt()
    
    furnitureListString = ""
    write.receipt = []
    furnitureList = []
        
def addNewFurniture():
    """
    Adds a new piece of furniture to the inventory.
    Asks the user for the manufacturer name, furniture type, quantity, and price per unit.
    Checks if the values are entered correctly and calls the updateInventory function if they are.
    
    """
    while True:
        try:
            furnitureManufacturer = input("Enter Manufacturer Name: \n ")
            furnitureType = input("Enter Furniture Type: \n ")
            furnitureQuantity = int(input("Enter Quantity: \n "))
            furniturePrice = input("Enter Price per Unit: \n ")
        except:
            print("Invalid Input \n")
        
        if type(furnitureManufacturer) == str and type(furnitureType) == str and type(furnitureQuantity) == int and type(furniturePrice) == str:
            break
        else:
            print("Invalid input found, Try again \n ")         
            
        lastId = int(recentId) + 1
        read.inventory.update({str(lastId): [furnitureManufacturer, furnitureType, furnitureQuantity, furniturePrice]})
        print("New Item added to Inventory \n")
        
def sellFurniture():
    """
    Sells furniture from the inventory.

    Asks the customer for their name and the ID of the furniture to be sold.
    Checks if the furniture exists in the inventory and if the quantity to be sold is valid and available in the inventory.
    Updates the inventory and prints the receipt.
    Prints the receipt and writes it to a file.
    
    """
    Total = 0
    shippingPrice = 0
    status = True
    furnitureListString = ""
    furnitureList = []
    while True:
        try:
            customerName = input("Enter your name (Customer Name) \n")
            if type(customerName) == str:
                break
            else:
                print("Please Enter a valid name \n")
        except:
            print("Invalid Input \n")
    while status == True:
        while True:
            try:
                checkId = input("Input the ID of the furniture \n")
                if checkId in read.inventory.keys():
                    break
                else:
                    print("Item not found / doesn't Exist \n")
            except:
                print("Invalid Input , Enter a numerical value \n")

        while True:
            try:
                newQuantity = int(input("Enter the amount to be sold \n"))
                break
            except:
                print("Invalid Input, Enter a number \n")
                
            if newQuantity > int(read.inventory[checkId][2]):
                print("Not enough inventory \n")
            elif newQuantity < 0:
                print("Negative Number not allowed \n")
            elif newQuantity == 0:
                print("Zero not allowed \n")
            elif subtractedValue < 0:
                print("Not enough inventory \n")
            
        subtractedValue = int(read.inventory[checkId][2]) - newQuantity
        read.inventory[checkId][2] = subtractedValue  
        
        Total += vat * (newQuantity * int(read.inventory[checkId][3].replace("\n","").replace("$",""))) + shippingPrice
        
        productName = read.inventory[checkId][1]
        
        spaceForItems = 49 - len(productName) - len(str(newQuantity))
        spaceForTotal = 49 - len("Total") - len(str(Total))
        furnitureList.append([productName + spaceForItems * " " + str(newQuantity)])
        productName = read.inventory[checkId][1]
            
        checkStatus = input("Do you want to continue? (yes/no) \n")
        if checkStatus == "no":
            status = False
    while True:    
        shippingCheck = input("Do you need shipping? (yes/no) \n")  
                       
        if shippingCheck == "yes":
            shippingLocation = input("Enter shipping location \n 1.Inside Valley \n 2.Outside Valley \n Enter the Corresponding Number \n")
        else:
            break
        
        if shippingLocation == "1":
            shippingPrice = 0
            break
        elif shippingLocation == "2":
            shippingPrice = 1500
            break
        else:
            print("Invalid Input , Enter a number (Shipping) \n")
    
    spaceForShipping = 49 - len("Shipping Price") - len(str(shippingPrice))
            
    furnitureListString += "".join(str(furnitureList).replace("[","").replace("]","").replace("'","")).replace(", ","\n")
    write.receipt = [
    "="*50, "\n",
    21 * " " +  "Receipt" +  20 * " " +  "\n",
    " " * 20 + str(time).split()[0] + " " * 20,"\n",
    "Customer Name: " + customerName, "\n",
    "Name of the furniture" + " " * 20 + "Quantity","\n",
    furnitureListString,"\n",
    "Shipping Price" + spaceForShipping * " " + "$" + str(shippingPrice),"\n",
    "VAT" + 44 * " " +"13% \n"
    "Total" + spaceForTotal * " " + "$" + str(Total),"\n",
    "\n",
    "=" * 50 
    ]
    for item in write.receipt:
            print(item)
    write.writeReceipt()
    furnitureListString = ""
    furnitureList = []
    write.receipt = []