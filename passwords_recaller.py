print ("\n\tpassword(s) recaller".upper())
def start():
    passwords_dict = {}

    message_one = ("\nWould you like to recall a password")
    message_one += ("\nor add a new one to the dictionary ? ")
    user_input_one = input (message_one + "\n[recall / add] - ")
    
    if (user_input_one == "recall") :
        print ("\n\trecalling password protocol".upper())
        print (passwords_dict)
        rerun = input("\nwould you like to rerun the programme ? [y/n] ")
        if (rerun.lower() == "y") :
            start()
        elif (rerun.lower() == "n"):
            pass

    elif (user_input_one == "add") :
        print ("\n\tadd new password protocol".upper())

        key = input ("enter username \n(with service name in brackets) : ")
        value = input ("enter password : ")
        passwords_dict.update({key:value})
        print ("key-value pair updated succesfully as :\n")
        print (passwords_dict)

        rerun = input("\nwould you like to rerun the programme ? [y/n]")
        if (rerun.lower() == "y") :
            start()
        elif (rerun.lower() == "n"):
            pass

    else :
        print ("\n\tsomething went wrong".upper())
        
        rerun = input("would you like to rerun the programme ? [y/n]")
        if (rerun.lower() == "y") :
            start()
        elif (rerun.lower() == "n"):
            pass
start()