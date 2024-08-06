import read
import operations
import write

status = True

while status == True:
    try:
        question = input('Nepal Furnishings Pvt Ltd \n Press 1 for Inventory \n Press 2 to purchase from Manufacturer \n Press 3 to process sales \n Press 4 to Exit \n')
    except ValueError:
        print("Invalid Input")
    if question == '1':
        read.readInventory()
    elif question == '2':
        operations.addFurniture()
        operations.updateInventory()
        write.writeReceipt()
    elif question == '3':
        operations.sellFurniture()
        operations.updateInventory()
        write.writeReceipt()
    elif question == '4':       
        status = False
    else:
        print('Invalid Input')
    write.question = question
    