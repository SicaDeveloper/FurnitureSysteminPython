import read
import operations
import write

status = True

"""
This is a program to simulate real inventory management 

It allows the customers and employees to buy and sell available inventory.

The components of this program are,
1. The employee or customer can view the inventory
2. The employee or customer can sell an item or multiple items
3. The employee or customer can buy an item or multiple items available in the inventory or a new item
4. The employee or customer can exit the program

"""

while status == True:
    try:
        question = int(input('\n Nepal Furnishings Pvt Ltd \n Press 1 for Inventory \n Press 2 to purchase from Manufacturer \n Press 3 to process sales \n Press 4 to Exit \n'))
        write.question = question    
        if question == 1:
            read.readInventory()
        elif question == 2:
            operations.addFurniture()
            write.updateInventory()
        elif question == 3:
            operations.sellFurniture()
            write.updateInventory()
        elif question == 4:       
            break
        else:
            print('Number not in range')
    except:
            print("Invalid Input")    
