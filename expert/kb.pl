:- dynamic known/3, multivalued/1.

% define disease
disease(covid) :- chest(pain).
disease(covid) :- breathing(difficult).
disease(covid) :- cough(strong).
disease(covid) :- body_temperature(high), speech(lost).
disease(covid) :- body_temperature(high), taste(abscent). 
disease(covid) :- body_temperature(high), smell(abscent).
disease(cold) :- \+body_temperature(high), \+cough(strong), throat(sore).

% contact details
contact(minerva) :- disease(covid).
contact(hospital) :- disease(covid).

% testing
test(antigen) :- disease(covid).

% ask about symptoms
chest(X) :- ask(chest, X).
breathing(X) :- ask(breathing, X).
speech(X) :- ask(speech, X).
body_temperature(X) :- ask(body_temperature, X).
cough(X) :- ask(cough, X).
taste(X) :- ask(taste, X).
smell(X) :- ask(smell, X).
throat(X) :- ask(throat, X).

% Asking clauses
ask(A, V):-
    known(yes, A, V), % succeed if true
    !.	

ask(A, V):-
    known(_, A, V), % fail if false 
    !, fail.

% If not multivalued, and already known to be something else, dont ask again for a different value.
ask(A, V):-
    \+multivalued(A),
    known(yes, A, V2),
    V \== V2,
    !, fail.

ask(A, V):-
    read_py(A,V,Y), % get the answer
    assertz(known(Y, A, V)),  % remember it
    Y == yes.	