# The code here will ask the user for input based on the askables. 
# It will only ask the user where necessary.
# Import necessary packages
from dotenv import load_dotenv

load_dotenv()

import tempfile
from pyswip import Prolog
from pyswip.easy import *
#from prolog_logic.pl import KB

prolog = Prolog() # Global handle to interpreter

retractall = Functor("retractall")
known = Functor("known",3)

# Define foreign functions for getting user input and writing to the screen
def write_py(X):
    print(str(X))
    sys.stdout.flush()
    return True

def read_py(A,V,Y):
    if isinstance(Y, Variable):
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
print("You need to urgently contact " + str(set(c['X'] for c in contact)) if contact else "You don't need to contact anyone")
print(("You also need to do an " + test[0]['X'] + " test" if test else "No testing is needed"))
