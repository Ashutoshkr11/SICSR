"""
Q2)
Accept the user’s nationality (country). If the user enters “India”, ask the
them to enter their state. If the user enters “Pune”, display “You are on
the waitlist for hostel accommodation”. Otherwise, display “You are
eligible for hostel accommodation”. If the user enters a country other than
India, display “Please visit the International Office.”.

"""


country = input("Enter your nationality: ")

if country.lower() == "india":
    state = input("Enter your state: ")
    if state.lower() == "pune":
        print("You are on the waitlist for hostel accomodation.")
    else:
        print("You are eligible for hostel accomodation.")
else:
    print("PLease visit the international Office.")



