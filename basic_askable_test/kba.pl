:- dynamic known/3, multivalued/1.

problem(out_of_gas) :- gas_gauge(empty).

gas_gauge(X) :- ask(gas_gauge, X).

ask(A, V):-
known(yes, A, V), 
!.

ask(A, V):-
known(_, A, V),
!, fail.

ask(A, V):-
\+multivalued(A),
known(yes, A, V2),
V \== V2,
!, fail.

ask(A, V):-
read_py(A,V,Y),
assertz(known(Y, A, V)), 
Y == yes.