
from QA import answer_Q
from name_management import name_change
from name_management import check_name_change
from name_management import name_response
from small_talk import talk_response 
from spell_check import correct
from small_talk import time_response

# Function to book a single flight
def book_single_flight(origin, destination, date, email):
    return f"Single flight booked! From {origin} to {destination} on {date}. Confirmation sent to {email}."

# Function to book a return flight
def book_return_flight(origin, destination, departure_date, return_date, email):
    return f"Return flight booked! From {origin} to {destination} on {departure_date} and return on {return_date}. Confirmation sent to {email}."

if __name__ == "__main__":

    booking_confirmation = "" # Initialize variable for booking confirmation

    un = '(User)'

    flag = True
    print("- Skynet: Hi, I'm Skynet. I here help you book a flight ")
    print("          Please Enter 'bye' if you want to say good bye.")
    print("          If you need assistance enter 'help'")
    print("          May I have ur name? <(￣︶￣)>" )
    print('- %s: ' %un, end=" ")


    ui = input()
    if ui == 'bye':
        flag = False
    else:
        un = name_change(ui)
        if un.lower() == 'skynet':
            print("- Skynet: Oh, cool!! we have the same name  ( ˶ˆᗜˆ˵ ).... this might get confusing (´･ω･`)" )
        else:
            print("- Skynet: Hi, %s, glad to meet u! how can I help you" %(un))
        #ui= user input
    while(flag == True):
        print('- %s: '%un, end=" ")
        ui = input()
        ui = [correct(i) for i in ui.split(' ')]
        ui = (' ').join(ui)
        if(ui != 'bye'):

            # name management
            response = name_response(ui, threshold = 0.9)
            if response != 'NOT FOUND':
                print("- Skynet: You're %s, I have a great memory ┑(￣u ￣)┍ " %(un))
                continue

            if check_name_change(ui):
                un = name_change(ui)
                print("- Skynet: Hi, %s" %(un))
                continue

       



            if ui == 'help':
                print("- Skynet: My purpose is to help you book a flight. Try asking me to book you a flight from your origin to destination ")
                print("          For example: 'I would like to book a flight' ")
                print("          If your're looking edit flight details type 'edit flight' ")
                continue


           # Check if the user wants to book a flight
            if 'book' in ui and 'flight' in ui:
                print("- Skynet: Sure, please provide the details for the flight.")
                print("-         From where do you want to depart?")
                origin = input("- %s: " % un)
                print("- Skynet: Where is your destination?")
                destination = input("- %s: " % un)
                print("- Skynet: When do you want to fly?")
                departure_date = input("- %s: " % un)
                print("- Skynet: Is it a single or return flight?")
                flight_type = input("- %s: " % un)
                if 'single' in flight_type.lower():
                    email = input("- Skynet: Please provide your email for confirmation: ")
                    booking_confirmation = book_single_flight(origin, destination, departure_date, email)

                elif 'return' in flight_type.lower():
                    print("- Skynet: When do you want to return?")
                    return_date = input("- %s: " % un)
                    email = input("- Skynet: Please provide your email for confirmation: ")
                    booking_confirmation = book_return_flight(origin, destination, departure_date, return_date, email)

                else:
                    print("- Skynet: I'm sorry, I didn't get that. Please specify if it's a single or return flight.")
                    continue

                print("- Skynet:", booking_confirmation)
                continue

            if 'flight details' in ui:
                print("- Skynet: Here are your flight details: ", booking_confirmation)
                continue

            




            # Allow users to modify flight details
            if 'edit' in ui and 'flight' in ui:
                print("- Skynet: What would you like to change?")
                print("-         Choose from: origin, destination, departure_date or email")
                change_input = input("- %s: " % un)
                
                if 'origin' in change_input:
                    origin = input("- Skynet: What's the new origin? ")
                elif 'destination' in change_input:
                    destination = input("- Skynet: What's the new destination? ")
                elif 'departure' in change_input:
                    departure_date = input("- Skynet: What's the new departure date? ")
                elif 'return' in change_input:
                    return_date = input("- Skynet: What's the new return date? ")
                elif 'email' in change_input:
                    email = input("- Skynet: What's the new email? ")
                
                if 'single' in flight_type.lower():
                    booking_confirmation = book_single_flight(origin, destination, departure_date, email)
                elif 'return' in flight_type.lower():
                    booking_confirmation = book_return_flight(origin, destination, departure_date, return_date, email)

                else:
                    print("- Skynet: I'm sorry, I couldn't understand the change request.")

                print("- Skynet: Flight details updated!")
                continue
            
    
    

            # time and data -- a part of the small talk
            if 'time' in ui:
                time_response('time')
                continue

            if  'today' in ui:
                time_response('today')
                continue

            # small talk
            response = talk_response(ui, threshold = 0.9)
            if response != 'NOT FOUND':
                print("- Skynet: " + response + ' ')
                continue

            # Question Answering (QA)
            response = answer_Q(ui, threshold = 0.1)
            if response != 'NOT FOUND':
                print("- Skynet: " + response + ' ')
            else:
                print("- Skynet: I'm sorry ˙◠˙ I don't quite understand. Try asking me to book you a flight from your origin to destination ")
                print("          For example: 'I would like to book a flight' ")
                print("          If your're looking edit flight details type 'edit flight' ")

        else:
            flag = False

    print("- Skynet: Bye!")
