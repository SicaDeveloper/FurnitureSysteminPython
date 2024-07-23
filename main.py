import read
import operations
import write

status = True

while status == True:
    question = input('Nepal Furnishings Pvt Ltd \n Press 1 for Inventory \n Press 2 to purchase from Manufacturer \n Press 3 to process sales \n Press 4 to Exit \n')
    if question == '1':
        read.readInventory()
    elif question == '2':
        operations.addFurniture()
    elif question == '3':
        write.sellFurniture()
    elif question == '4':       
        status = False
    else:
        print('Invalid Input')
    