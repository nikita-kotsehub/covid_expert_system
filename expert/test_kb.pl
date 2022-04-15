:- dynamic known/3, multivalued/1.

% define disease
disease(covid) :- chest(pain).
disease(covid) :- breathing(difficult).
disease(covid) :- body_temperature(high), cough(strong).
disease(covid) :- body_temperature(high), taste(abscent), smell(abscent).
disease(flu) :- \+body_temperature(high), \+cough(strong), throat(sore).

% ask about symptoms
chest(X) :- ask(chest, X).
breathing(X) :- ask(breathing, X).
speech(X) :- ask(speech, X).
body_temperature(X) :- ask(body_temperature, X).
cough(X) :- ask(cough, X).
taste(X) :- ask(taste, X).
smell(X) :- ask(smell, X).
throat(X) :- ask(throat, X).


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