#import all the modules you need, below this line


#write any functions you need, below this line

def Sessions(total: int) -> str:
    if total > 9:
        return "High"
    elif total >= 5:
        return "Moderate"
    else:
        return "Low"
    
therapy_types = [
    "IndividualTherapy",
    "GroupTherapy",
    "FamilyTherapy",
    "CoupleTherapy",
    "OnlineTherapy"
]

clients = ["first", "second", "third"]

questions = [
    {"text": f"How many {t.replace('Therapy', ' Therapy')} sessions per week do you have with the {c} client?", "therapy": t}
    for c in clients
    for t in therapy_types
]

def ask(question):
    while True:
        try:
            x = int(input(question + " "))
            if 0 <= x <= 7:
                return x
            print("Number must be between 0 and 7!")
        except ValueError:
            print("Please enter a valid number!")
#use the main() function for your program, define all other functions above main
def main ():
    #use print statements such as this one, to mark important points in the application, to help you with debugging
    print("Starting application...")

    totals = {t: 0 for t in therapy_types}

    for q in questions:
        totals[q["therapy"]] += ask(q["text"])

    print("\n Weekly therapy sessions: \n")
    for t, total in totals.items():
        print(f"{t}: {total} session/week -> {Sessions(total)}")


#please do not change the lines below, they are needed for your tests to work properly
#write all your code in the current file, and all your tests in the tests.py file
if __name__ == "__main__":
    main()
