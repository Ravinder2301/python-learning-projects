import pywhatkit

def send_message(phone_number, message, time_hour=0, time_minute=0):
    pywhatkit.sendwhatmsg(phone_number, message, time_hour, time_minute)  # Sends the message at the specified time

send_message("+918860386096", "Hello! This is an automated message.", 1, 9)  # Example usage
