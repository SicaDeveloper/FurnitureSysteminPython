import read
import operations
import write

status = True

while status == True:
    try:
        while True:
            question = input('\n Nepal Furnishings Pvt Ltd \n Press 1 for Inventory \n Press 2 to purchase from Manufacturer \n Press 3 to process sales \n Press 4 to Exit \n')
            if type(question) == int or float:
                break
        write.question = question
    except:
        print("Invalid Input")
    if question == '1':
        read.readInventory()
    elif question == '2':
        operations.addFurniture()
        write.updateInventory()
    elif question == '3':
        operations.sellFurniture()
        write.updateInventory()
    elif question == '4':       
        break
    else:
        print('Invalid Input')
    
