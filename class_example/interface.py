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

# Create a temporary file with the KB in it
#(FD, name) = tempfile.mkstemp(suffix='.pl', text = "True")
#with os.fdopen(FD, "w") as text_file:
#    text_file.write(KB)
prolog.consult('knowledge_base.pl')  
#prolog.consult(name) # open the KB for consulting
#os.unlink(name) # Remove the temporary file

call(retractall(known))
problem = [s for s in prolog.query("problem(X).", maxresult=1)]
print("Your problem is " + (problem[0]['X'] + "." if problem else "unknown."))