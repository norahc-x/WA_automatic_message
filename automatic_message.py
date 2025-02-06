import pywhatkit as kit 

def automatic_message(number, message, hour, minute):
    try:
        kit.sendwhatmsg(number, message, hour, minute)
        print("Message sent")
    except Exception as e:
        print(f"Error: {e}")
        
number = ""  # Recipient's phone number with country code
message = ""  # Your message
hour = 12  # Message time (24-hour format)
minute = 30  # Message minute

automatic_message(number, message, hour, minute)
