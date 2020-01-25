stuff = {'rope': 1, 'torches': 6, 'gold coins': 42, 'dagger':1, 'arrows': 12}

def displayInventory(inventory):
    print('Inventory:')
    for item, qty in inventory.items():
        print('%d %s' % (qty, item))
    total = sum(inventory.values())
    print('\nTotal number of items: %d' % total)
    
   
    

displayInventory(stuff)
