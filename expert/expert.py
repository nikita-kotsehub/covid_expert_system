# The code here will ask the user for input based on the askables. 
# It will only ask the user where necessary.
# Import necessary packages and load environmental variables
from dotenv import load_dotenv
load_dotenv()

import tempfile
from pyswip import Prolog
from pyswip.easy import *

# Global handle to interpreter
prolog = Prolog() 

retractall = Functor("retractall")
known = Functor("known",3)

# Define foreign functions for getting user input and writing to the screen
def write_py(X):
    print(str(X))
    sys.stdout.flush()
    return True

def read_py(A,V,Y):
    if isinstance(Y, Variable):
        if str(A) == "body_temperature":
            print("Please measure your body temperature. Choose the option that most closely describes it:")
            print("a. High \nb. Regular")
            answer = input("Your body temperature is: ")
            if answer == "a":
                response="yes"
            else:
                response="no"
            
        elif str(A) == "chest":
            print("Is your chest in pain?")
            print("a. yes, it is \nb. no, it's not")
            answer = input("Choose a or b to describe your chest condition: ")
            if answer == "a":
                response="yes"
            else:
                response="no"

        elif str(A) == "breathing":
            print(f"Is {str(A)} {str(V)} for you?")
            print("a. yes, it is \nb. no, it's not")
            answer = input("Choose your breathing condition: ")
            if answer == "a":
                response="yes"
            else:
                response="no"

        elif str(A) == "cough":
            print(f"If coughing, how would you describe your {str(A)}?")
            print("a. Strong \nb. Medium \nc. Not too bad")
            answer = input("Choose your coughing condition: ")
            if answer == "a":
                response="yes"
            else:
                response="no"

        elif str(A) == "speech":
            print(f"Do you experience difficulties with {str(A)}?")
            print("a. Yes, I do :( \nb. No, all good")
            answer = input(f"Choose your {str(A)} condition: ")
            if answer == "a":
                response="yes"
            else:
                response="no"

        elif str(A) == "taste":
            print(f"Can you {str(A)}?")
            print("a. Yes, I can ^-^ \nb. No, not at all :(")
            answer = input(f"Choose your {str(A)} condition: ")
            if answer == "a":
                response="yes"
            else:
                response="no"

        elif str(A) == "smell":
            print(f"Can you {str(A)}?")
            print("a. Yes, I can ^-^ \nb. No, not at all :(")
            answer = input(f"Choose your {str(A)} condition: ")
            if answer == "a":
                response="yes"
            else:
                response="no"

        elif str(A) == "throat":
            print(f"Is your {str(A)} {str(V)}?")
            print("a. Yes, it is \nb. Nope")
            answer = input(f"Choose your {str(A)} condition: ")
            if answer == "a":
                response="yes"
            else:
                response="no"

        else:
            response = input(str(A) + " is " + str(V) + "? ")

        Y.unify(Atom(response))
        return True
    else:
        return False

write_py.arity = 1
read_py.arity = 3

registerForeign(read_py)
registerForeign(write_py)

prolog.consult('kb.pl')  

call(retractall(known))
disease = [s for s in prolog.query("disease(X).", maxresult=1)]
contact = [s for s in prolog.query("contact(X).")]
test = [s for s in prolog.query("test(X).")]

print("Your disease is " + (disease[0]['X'] + "." if disease else "unknown."))
if contact:
    contacts = set(c['X'] for c in contact)
    print("You need to urgently contact " + str(' and '.join(contacts)))
    if 'minerva' in contacts:
        print('\t You can reach Minerva at +49 151 24039851 or at bwalder@minerva.edu')
    if 'hospital' in contacts:
        print('\t The nearest hospital to Berlin res can be contacted at 030 23110')
print(("You also need to do an " + test[0]['X'] + " test" if test else "No testing is needed"))
