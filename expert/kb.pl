:- dynamic known/3, multivalued/1.

problem(battery) :- \+engine(turning_over), battery(bad).
problem(engine_oil_low) :- \+engine(turning_over), warning_light(oil).
battery(bad) :- lights(weak).
battery(bad) :- radio(weak).
problem(out_of_gas) :- engine(turning_over), gas_gauge(empty).
problem(engine_flooded) :- engine(turning_over), smell(gas).

gas_gauge(X) :- ask(gas_gauge, X).
engine(X) :- ask(engine, X).
lights(X) :- ask(lights, X).
radio(X) :- ask(radio, X).
smell(X) :- ask(smell, X).
warning_light(X) :- ask(warning_light,X).

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