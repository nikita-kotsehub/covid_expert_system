from dotenv import load_dotenv

load_dotenv()

from pyswip import Prolog
from pyswip.easy import *

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
        response = input(str(A) + " is " + str(V) + "? ")
        Y.unify(Atom(response))
        return True
    else:
        return False

write_py.arity = 1
read_py.arity = 3

registerForeign(read_py)
registerForeign(write_py)

prolog.consult('kba.pl')

call(retractall(known))
problem = [s for s in prolog.query("problem(X).", maxresult=1)]
print("Your problem is " + (problem[0]['X'] + "." if problem else "unknown."))