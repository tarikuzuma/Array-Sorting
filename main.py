def end():
    while True:
        print("")
        terminate = str(input('Continue [Y/y: N/n]?: '))
        terminate = terminate.lower()
        if terminate == 'n':
            print(" \n -TERMINATE- \n")
            quit()
        elif terminate == 'y':
            print("\n -Continue- \n")
            return
        else: 
            print ("invalid input")
            continue

def op1(list):
    print("\nEnter any programming languages:")
    print(*list, sep = "\n")
    user_inp = str(input("\nEnter Language to add: "))
    list.append(user_inp)
    print ("")
    print(*list, sep = "\n")
    
def op2(list):
    print("\nEnter any programming languages:")
    print(*list, sep = "\n")
    user_inp = str(input("\nClear Now [Y/y]: "))
    
    if user_inp.lower() == 'y':
        list.clear()
        print(f"Value: {list}")
    
    else:
        print ('\nInvalid Input \n')
        print(*list, sep = "\n")
    
def op3(list):
    print("\nEnter any programming languages:")
    print(*list, sep = "\n")

    x = list.copy()
    print("\nDuplicate Copy: \n")
    print(*x, sep = "\n")


#CREDITS TO ETRALOOM THE MAANAGS FOR THE LOGIC IN THE FOR LOOP!
def op4(list):
    try: 
        print("\nEnter any programming languages:")
        print(*list, sep = "\n")
        duplicate = 0
        
        for item in list:
            if list.count(item) > 1:
                duplicate += 1
            else:
                pass
        print (f"\nNumber of duplicated value/s: {duplicate}")
        
    except:
        return

def op5(list):
    print("\nEnter any programming languages:")
    print(*list, sep = "\n")
    print("\nEnter additional valeus for Programming languages (Max of 5 indexes): ")
    
    index0 = str(input("Index [0]: "))
    index1 = str(input("Index [1]: "))
    index2 = str(input("Index [2]: "))
    index3 = str(input("Index [3]: "))
    index4 = str(input("Index [4]: "))
    
    list2 = [index0, index1, index2, index3, index4]

    list.extend(list2)

    print ("")
    print(*list, sep = "\n")

def op6(list):
    try:
        print("\nEnter any programming languages:")
        print(*list, sep = "\n")
        user_inp = str(input("\nChoose from your inputted Programming Language: "))
        x = list.index(user_inp)

        print (f'Index: {x}')
    
    except:
        print("\nElement or list does not exist, therefore index cannot be given.")

def op7(list):
    print("\nEnter any programming languages:")
    print(*list, sep = "\n")

    number = int(input("\nEnter element number: "))
    user_input = str(input("Enter Programming Language to be inserted: "))

    try:
        list.insert(number, user_input)

    except:
        print("Parameter Error: Either index is too high or non-existent")

    print(*list, sep = "\n")

def op8(list):
    try: 
        print("\nEnter any programming languages:")
        print(*list, sep = "\n")

        number = int(input("\nEnter element number: "))

            
        list.pop(number)
        print ("")
        print(*list, sep = "\n")
        print ("")

    except:
        print("Args. Error: Either index is too high or non-existent")

def op9(list):
    try: 
        print ("\nEnter any programming languages: ")
        print(*list, sep = "\n")
        user_input = str(input("\nEnter Programming Language you want to remove: "))
        list.remove(user_input)
        print ("")
        print(*list, sep = "\n")
    except:
        print("Args. Error: Element is non-existent")

def op10(list):
    print ("\nEnter any programming languages: ")
    print(*list, sep = "\n")
    list.reverse()
    print("")
    print(*list, sep = "\n")

def op11(list):
    print ("\nEnter any programming languages: ")
    print(*list, sep = "\n")
    list.sort()
    print("")
    print(*list, sep = "\n")

    

def main():
    list = ['Kotlin', 'Swift', 'Python', 'Assembly', 'Ruby']
    while True:
        print ("          Menu:")
        print ("[1] Append      [6] Index")
        print ("[2] Clear       [7] Insert")
        print ("[3] Copy        [8] Pop")
        print ("[4] Count       [9] Remove")
        print ("[5] Extend      [10] Reverse ")
        print ("        [11] Sort")
        choice = str(input('Enter your choice: '))

        match choice:
            case "1":
                op1(list)
                end()
            case "2":
                op2(list)
                end()
            case "3":
                op3(list)
                end()
            case "4":
                op4(list)
                end()
            case "5":
                op5(list)
                end()
            case "6":
                op6(list)
                end()
            case "7":
                op7(list)
                end()
            case "8":
                op8(list)
                end()
            case "9":
                op9(list)
                end()
            case "10":
                op10(list)
                end()
            case "11":
                op11(list)
                end()
            case _:
                print("-Invalid Input-")
                continue

main()