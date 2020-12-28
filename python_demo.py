'''
This is a python based programme that remembers the your password(s).
'''

print ("\n\tpassword(s) recaller".upper())                              # declares the name of the programme in capital letters.

ask_message = ("do you want me to recall a password for you")           # asking message for user
ask_message += ("\nor learn a new one ?")
user_order = input (ask_message.title())                                # displays the ask_message

if (user_order.lower() = "recall" or "recall a password") then :
    print ("recalling password protocol ...")
elif (user_order.lower() = "learn" or "learn a new password") then :
    print ("learn new password protocol ...")