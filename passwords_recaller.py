'''
this is a python based program that help you keep track 
of your passcodes for several accounts/services.
Note :
- there must be a blank text (.txt) file in the same folder/directory named as 'pass_codes_file.txt'
- in case of deleting any pair of username-passwords, erase it from the same file 
'''
print ("\n\tpassword(s) recaller".upper())                                               # displays PASSWORD(S)_RECALLER.

def start():                                                                             # declares the beginning of start() function.
    message_one = ("\nwould you like to recall a password")                              # message for asking user to either add or recall
    message_one += ("\nor add a new one to the database ? ")                             # a password.
    user_input_one = input (message_one + "\n[recall / add] - ")                         # stores user`s choice in a variable

    if (user_input_one == "recall") :                                                    # prints the pass_codes_file if the conditions match.
        print ("\n\trecalling password protocol".upper())
        print ("----"*8)
        f = open('pass_codes_file.txt','r')                                              # change 'pass_codes_file.txt' in case of 
        print (f.read())                                                                 # a different file name.
        f.close()                                                                        # add file path if pass_codes_file is in 
        print ("----"*8)                                                                 # different folder/directory.           

        rerun = input("\n=would you like to rerun the program ? [y/n] ")                 # asks user for a rerun.
        if (rerun.lower() == "y") :
            start()
        elif (rerun.lower() == "n"):
            exit()

    elif (user_input_one == "add") :                                                     # adds key-value pair to the password_dict .
        print ("\n\tadd new password protocol".upper())
        def add():
            username = input ("\n-enter username \n(with service name in brackets) : ")
            password = input ("-enter password : ")
            f = open('pass_codes_file.txt','a')                                          # change 'pass_codes_file.txt' in case of 
            f.write("\n" + username + ' : ' + password)                                  # a different file name.
            f.close()
            print ("username-password updated successfully")

            message_two = ("\n=would you like to rerun the program")
            message_two += ("\nor add an another pair of username-password [y/n/add] ")
            rerun = input(message_two)                                                   # asks user for a rerun.
            if (rerun.lower() == "y") :
                start()
            elif (rerun.lower() == "add") :
                add()
            elif (rerun.lower() == "n"):
                exit()
        add()                                                                            # calls add() function

    else :                                                                               # prints SOMETHING WENT WRONG 
        print ("\n\tsomething went wrong".upper())                                       # in case of unexpected inputs.
        
        rerun = input("=would you like to rerun the program ? [y/n] ")                   # asks user for a rerun.
        if (rerun.lower() == "y") :
            start()
        elif (rerun.lower() == "n"):
            exit()
start()