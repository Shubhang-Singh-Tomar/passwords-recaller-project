'''
This is a python based programme that helps you to keep track
of you passwords and accounts usernames.
To do :
- complete the key medium
- complete the value medium
- random number generator and use the same for greeting statements and unexpected values
- add more greeting statements and unexpected inputs 
'''

greetings_statements = [                                               # these are greeting statements 
    'See you later',                                                   # that are to be displayed at the end.
    'Goodbye',
    'Hope to see you soon'
    ]   
unexpected_inputs = [                                                  # these statements are to be displayed in case of 
    'Sorry, i didn`t get that',                                        # unexpected inputs from user.
    'Invalid value or input'
    ]

pass_codes = {}                                                        # will store the key(account`s username) and values(passwords)                               

def recalling_password_protocol() :                                    # recalling_password_protocol()
    print ("recalling passwords ...".upper())
    
    recall_medium_input_statement = ("would you like to go with key-medium or value-medium :".title())
    recall_medium_input_statement += ("\n(use key-medium if you want to know a password for an username)")
    recall_medium_input_statement += ("\n(use value-medium if you want to know about the username for the password given)")
    user_choice = input (recall_medium_input_statement)      

    if (user_choice.lower() == "key-medium" or "i would like to go with the key-medium") :
        print ("key-medium".upper())
        username = input ("enter username : ".title())
         
        rerun = input ("would you like to go back ? ".title())             # provides user to go back and change his/her action.
        if (rerun.lower() == "yes" or "definitely" or "would love to") :
            rerun()
        elif (rerun.lower() == "no" or "no thanks") :
            print (greetings_statements[0])
        else :
            print (unexpected_inputs[0])
    elif (user_choice.lower() == "value-medium" or "i would like to go with the value-medium"):
        print ("value-medium".upper())
        password = input ("enter password : ".title())

        rerun = input ("would you like to go back ? ".title())             # provides user to go back and change his/her action.
        if (rerun.lower() == "yes" or "definitely" or "would love to") :
            rerun()
        elif (rerun.lower() == "no" or "no thanks") :
            print (greetings_statements[0])
        else :
            print (unexpected_inputs[0])
    else :
        print (unexpected_inputs[0])

def learn_new_password_protocol() :                                    # learn_new_password_protocol()       
    print ("learnng new passwords ...".upper())
    
    username = input (                                                 # asks user for acoount and password for the same.     
        "enter username :\n(with website or service name in brackets)"
        .title())
    password = input (
        "enter password :\n".title()
    )
    
    pass_codes.update({username:password})                             # stores the key and values to the dictionary.
    print ("password added to dictionary succesfully".title())

    rerun = input ("would you like to go back ? ".title())             # provides user to go back and change his/her action.
    if (rerun.lower() == "yes" or "definitely" or "would love to") :
        rerun()
    elif (rerun.lower() == "no" or "no thanks") :
        print (greetings_statements[0])
    else :
        print (unexpected_inputs[0])

print ("\n\tpassword(s) recaller".upper())                              # declares the name of the programme in capital letters.

def rerun() :
    ask_message = ("do you want me to recall a password for you")       # asks user for creating a new password to remeber 
    ask_message += ("\nor learn a new one ?")                           # or recall an old one.
    user_order = input (ask_message.title())                                

    if (user_order.lower() == "recall" or "recall a password"):         # initiates the recalling_password_protocol() if conditions match.
        recalling_password_protocol()
    elif (user_order.lower() == "learn" or "learn a new password"):     # initiates the learn_new_password_protocol() if conditions match.
        learn_new_password_protocol()
    else :                                                              # displays message in case of unexpected inputs.
        print (unexpected_inputs [0])
        rerun()
rerun()