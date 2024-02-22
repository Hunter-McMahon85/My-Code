# CIS 122 spring 2021 assign 8
# Author: Hunter McMahon
# Partner: completed solo
# Description: listing some stuff...

#default group
groups = {}

#required functions
def create_group(d):
    #ask for a group name
    print('** Create new Group **')
    getgroupname = True
    while getgroupname == True:
        new_group = input('\nEnter Group name (empty to cancel):')
        #checks to see if the group is a duplicate
        if len(new_group) > 0:
            duplicate = False
            for key in d:
                if key == new_group:
                    duplicate = True
            #action if the group name is original
            if duplicate == False:
                groups[new_group] = {}
                group_keys = []
                add_fields = True
                #prompts the user to add fields to the group, they are stored as a list in the subgroup
                while add_fields == True:
                    new_field = input('Enter field name (empty to stop):')
                    if len(new_field) > 0:
                        #adds the field to the group if one is inputed
                        group_keys.append(new_field)
                    else:
                        add_fields = False
                groups[new_group]['_keys_'] = group_keys
                d[new_group]['_data_'] = []
            #action if group name is duplicate
            elif duplicate == True:
                print('Group name cant be a duplicate')
        else:
            getgroupname = False
            
#list out our groups
def list_groups(d):
    print('** list of Groups **')
    if len(d) > 0:
        #iterates through the groups and prints them out
        for key in d:
            seperation = ', '
            list_string = seperation.join(d[key]['_keys_'])
            print(key, ':', len(d[key]['_keys_']), 'properties', '(' + list_string + ')')
    else:
        print('There are no groups, enter C to add a group, ? for help, x or nothing to exit\n')
     
#put some data in our groups
def add_group_data(d):
    print('** Add group data **')
    list_groups(d)
    add_data = True
    if len(d) > 0:
        while add_data == True:
            group_2_add = input('\nEnter group (empty to cancel):')
            if len(group_2_add) > 0:
                #checks to see if the group exist
                for key in d:
                    #ask for data if the group exist
                    if key == group_2_add:
                        entries = {}
                        for key in d[group_2_add]['_keys_']:
                            new_entry = input('Enter '+ str(key) +':')
                            entries[key] = new_entry
                        d[group_2_add]['_data_'].append(entries)      
                    else:
                        #ask for a valid group name
                        print('Please enter a valid group name (entry does not exist)')
                        break
            else:
                add_data = False
                break
    else:
        #exits if nothing is entered into d
        pass

#display the data in our groups
def list_group_data(d):
    print('** list group data **')
    list_groups(d)
    ask_to_list = True
    if len(d) > 0:
        while ask_to_list == True:
            group_2_list = input('\nEnter group name(empty to cancel):')
            if len(group_2_list) > 0:
                #checks to see if the group exist
                for key in d:
                    #list whats in the group if the group exist
                    if key == group_2_list:
                        length_of_data = len(d[group_2_list]['_data_'])
                        for i in range(length_of_data):
                            data_2_print = d[group_2_list]['_data_'][i]
                            pair = '' 
                            for key, value in data_2_print.items():
                                pair += str(i)
                                pair += str(key)+'='+str(value)
                                if i < length_of_data:
                                    pair += ','
                            print(pair)  
                    else:
                        #ask for a valid group name if the given one is invalid
                        print('Please enter a valid group name (entry does not exist)')
                        break
            else:
                ask_to_list = False
                break
    else:
        #exits if nothing is entered into d
        pass

#take input and handle it 
def take_and_handle_orders():
    #greeting message
    print('>> Welcome to Group Manager <<\nThis program creates groups with dynamic properties')
    #input loop
    orders_sir = True
    while orders_sir == True:
        order = input('\nCommand (empty or X to quit, ? for help):')
        order = order.strip()
        order = order.upper()
        #determins if we have input and calls the according function
        if len(order) > 0:
            if order == '?':
                print('?: list commands\nC: Create a new group\nA: Add data to a group\nG: List groups\nL:list data for a group\nX: Exit')
                print('Enter r for a suprise ;)')
            elif order == 'C':
                create_group(groups)
            elif order == 'A':
                add_group_data(groups)
            elif order == 'G':
                list_groups(groups)
            elif order == 'L':
                list_group_data(groups)
            elif order == 'X':
                orders_sir = False
                print('Adios!')
                break
            elif order == 'R':
                # a little easter egg
                print('Were no strangers to love \nYou know the rules and so do I \nA full commitments what Im thinking of\nYou wouldnt get this from any other guy\n\nI just wanna tell you how Im feeling\nGotta make you understand\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\nWeve known each other for so long\nYour hearts been aching, but youre too shy to say it\nInside, we both know whats been going on\nWe know the game, and were gonna play it\nAnd if you ask me how Im feeling\nDont tell me youre too blind to see\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\nOoh (Give you up)\nOoh-ooh (Give you up)\nOoh-ooh\nNever gonna give, never gonna give (Give you up)\nOoh-ooh\nNever gonna give, never gonna give (Give you up)\n\nWeve known each other for so long\nYour hearts been aching, but youre too shy to say it\nInside, we both know whats been going on\nWe know the game, and were gonna play it\n\nI just wanna tell you how Im feeling\nGotta make you understand\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you')
            else:
                print('Please enter a valid input (input ? for help, input X or leave blank to quit')
        else:
            orders_sir = False
            print('Adios!')
            break
#call our function and let the show begin
take_and_handle_orders()
