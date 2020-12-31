'''
this is a python based programme that help you keep track 
of your passcodes for several accounts
To do :
- need to store key-value pair permanently
'''
print ("\n\tpassword(s) recaller".upper())                                              # displays PASSWORD(S)_RECALLER.
passwords_dict = {}                                                                     # declares an empty dictionary (passwords_dict).
def start():                                                                            # declares the beginning of start() function.
    message_one = ("\nwould you like to recall a password")                             # message for asking user to either add or recall
    message_one += ("\nor add a new one to the dictionary ? ")                          # a password.
    user_input_one = input (message_one + "\n[recall / add] - ")                        # stores user`s choice in a variable

    if (user_input_one == "recall") :                                                   # prints the passwords_dict if the conditions match.
        print ("\n\trecalling password protocol".upper())
        print ("----"*8)
        print (passwords_dict)
        print ("----"*8)

        rerun = input("\n=would you like to rerun the programme ? [y/n] ")               # asks user for a rerun.
        if (rerun.lower() == "y") :
            start()
        elif (rerun.lower() == "n"):
            pass

    elif (user_input_one == "add") :                                                    # adds key-value pair to the password_dict .
        print ("\n\tadd new password protocol".upper())
        def add():
            key = input ("\n-enter username \n(with service name in brackets) : ")
            value = input ("-enter password : ")
            passwords_dict.update({key:value})
            print ("key-value pair updated succesfully as :\n")
            print (passwords_dict)

            message_two = ("\n=would you like to rerun the programme")
            message_two += ("\nor add an another key-value pair [y/n/add] ")
            rerun = input(message_two)                                                  # asks user for a rerun.
            if (rerun.lower() == "y") :
                start()
            elif (rerun.lower() == "add") :
                add()
            elif (rerun.lower() == "n"):
                pass
        add()                                                                           # call add() function

    else :                                                                              # prints SOMETHING WENT WRONG 
        print ("\n\tsomething went wrong".upper())                                      # in case of unexpected inputs.
        
        rerun = input("=would you like to rerun the programme ? [y/n]")                  # asks user for a rerun.
        if (rerun.lower() == "y") :
            start()
        elif (rerun.lower() == "n"):
            pass
start()