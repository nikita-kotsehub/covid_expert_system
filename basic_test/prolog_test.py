from dotenv import load_dotenv

load_dotenv()

from pyswip import Prolog
prolog = Prolog()
#prolog.assertz("father(michael,john)")
#prolog.assertz("father(michael,gina)")
prolog.consult('kbt.pl')
list(prolog.query("father(michael,X)")) == [{'X': 'john'}, {'X': 'gina'}]
for soln in prolog.query("father(X,Y)"):
    print(soln["X"], "is the father of", soln["Y"])
# michael is the father of john
# michael is the father of gina