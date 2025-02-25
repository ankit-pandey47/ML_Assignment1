import pywhatkit as kit
phone = input("ENTER THE USERS PHONE NUMBER with coiuntry code")
msg = input("ENTER THE MSG U WANT TO SEND")
hour = int(input("Enter the hour to send the message (24-hour format, e.g., 15 for 3 PM): "))
minute = int(input("Enter the minute to send the message: "))


try:
    kit.sendwhatmsg(phone , msg , hour , minute)
    print("SUCCESFULL")
except Exception as er:
    print("ERROR")

print("ANkit")

