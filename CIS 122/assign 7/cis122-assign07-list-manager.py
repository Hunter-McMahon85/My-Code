# CIS 122 spring 2021 lab 7 word checkassign 07
# Author: Hunter McMahon
# Partner: completed solo 
# Description: are you on the list?

#pad functions from assign 6
def pad_string(string, padsize, side = True, charecter = ' '):
    """
    takes multiple inputs to add padding to a string
        uses booleans and string/integer inputs to add padding to a string
    Args
    string (str): the string were adding pading to
    padsize: (int): how many charecters of padding we want
    side (boolean) deafaulted to true: determines the side of padding (true = left, false = right)
    charecter (str) defualted to ' ': the charecter of the padding
    Returns:
    output_string = the padded string
    """
    output_string = ''
    if side == True:
        output_string = charecter*(padsize-len(string)) + string
    else:
        output_string = string + (charecter*(padsize-len(string))) 
    return output_string

def pad_left(string, size, charecter = ' '):
    """
    takes a string and ads a padding charecter to the left size times
        uses pad_string to add padding to the left side of a stirng
    Args
    string (str): the string were adding pading to
    padsize: (int): how many charecters of padding we want
    charecter (str) defualted to ' ': the charecter of the padding
    Returns:
    Padding = the padded string
    """
    padding = pad_string(str(string), size,  True, charecter)
    return padding

def pad_right(string, size, charecter = ' '):
    """
    takes a string and ads a padding charecter to the right by size times
        uses pad_string to add padding to the right side of a stirng
    Args
    string (str): the string were adding pading to
    padsize: (int): how many charecters of padding we want
    charecter (str) defualted to ' ': the charecter of the padding
    Returns:
    Padding = the padded string
    """
    padding = pad_string(str(string), size, False, charecter)
    return padding
#initialize an empty list 2 a variable
bunch_o_things = []
#required functions
#1
def cmd_help():
    """
    prints out the full list of commands for editing the list
        uses a loop and list to display to the user the full list of availible commands and a  short description of what they do 
    Args
    none 
    Returns:
    none: void function
    """
    commands = ['Add', 'Delete', 'List', 'Clear']
    discription = ['Add to list', 'Delete information', 'List information', 'Clear list']
    i = 0
    max_cmd_pad = get_max_list_item_size(commands)
    print('*** Available commands ***')
    for i in range(len(discription)):
        print(pad_right(commands[i], max_cmd_pad+5)+discription[i])
    print('Empty to Exit')
#2   
def cmd_add(t):
    """
    continuosly adds items to the list based on what the user enters
        uses loops and booleans see if the user entered something to add to the list, if so it adds the entry to the list and if the input is blank then the function is exited 
    Args
    t (list): the list we wish to add values to
    Returns:
    none: void function
    """
    add_terms = True
    item_count = 0
    while add_terms == True:
        new_term = input('Enter information (empty to stop): ')
        if len(new_term) > 0:
            t.append(new_term)
            item_count = len(t)
            print('Added, item count =', item_count)
        else:
            add_terms = False
            print('List contains', item_count, 'item(s)')
            i = 0
            for i in range(len(t)):
                print(t[i])
            break
#3    
def cmd_delete(t):
    """
    prompts the user for an index value and then deletes that index from the list unil it is empty or the user enters nothing
        uses loops and booleans to ask for an index to delete, verify its existance, and then act accordingly to delete an item or return an error message if input is invalid
    Args
    t(list): the list we are deleting items from
    Returns:
    none: void function
    """
    delete_terms = True
    for i in range(len(t)):
                print(pad_right(i, 2),t[i])
    #item_count = len(t)
    while delete_terms == True:
        remove_term = str(input('Enter number to delete (empty to stop): '))
        digits = remove_term.isdigit()
        remove_term = remove_term.strip()
        i = 0
        if len(t) > 0:
            if digits == True:
                if len(remove_term) > 0:
                    remove_term = int(remove_term)
                    if 0 <= remove_term < len(t):
                        t.remove(t[remove_term])
                    else:
                        print('Please enter a valid index number')
                elif len(remove_term) == 0:
                    delete_items = False
                    break
            elif digits == False:
                print('Please enter only digits')
        if len(t) == 0:
            print('All items deleted')
            delete_terms = False
            break
        elif len(t) > 0:
            for i in range(len(t)):
                print(pad_right(i, 2),t[i])             
#4    
def cmd_list(t):
    """
    prints the list out
        uses a loop to iterate through a list and print the list out 
    Args
    t (list): the list thats being printed 
    Returns:
    none: void function
    """
    print('List contains', len(t), 'item(s)')
    i = 0
    for i in range(len(t)):
        print(t[i])
#5    
def cmd_clear(t):
    """
    deletes every item from the list
        Theres not much else to say 
    Args
    t (list): the list thats being "cleaned" or "cleared" 
    Returns:
    none: void function
    """
    initial_length = len(t)
    del t[0:initial_length]
    print(initial_length, 'item(s) removed, list empty')
#6    
def get_max_list_item_size(t):
    """
    takes a list and finds the length of the longest valie
        uses a loop to iterate through a list and find the index number of the value with the longest charecter length
    Args:
    t (list): the list we want to find the longest entry of 
    Returns:
    Max_index (int): the index vaue of the longest string/set of charecters of the list
    """
    max_index = 0
    for i in range(len(t)):
        if len(t[i]) > max_index:
            max_index = len(t[i])
    return max_index
#request the user for a command and call the appropriate command
def handle_list():
    """
    handles our string based on user input
        Takes a user "commmand" and calls a function that edits a list based on whats been inputed
    Args
    none 
    Returns:
    none: void function
    """
    orders_sir = True
    while orders_sir == True:
        orders = str(input("Enter a command (? for help): "))
        orders = orders.strip().lower()
        if len(orders) == 0:
            orders_sir = False
            print('Goodbye!')
        else:
            if orders == '?':
                cmd_help()
            elif orders == 'add':
                cmd_add(bunch_o_things)
            elif orders == 'delete' or 'del':
                cmd_delete(bunch_o_things)
            elif orders == 'list':
                cmd_list(bunch_o_things)
            elif orders == 'clear':
                cmd_clear(bunch_o_things)
            else:
                print('Please enter a valid command (input ? for help)')
handle_list()
