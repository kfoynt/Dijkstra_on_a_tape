# Dijkstra on a Tape

A very inefficient implementation of Dijkstra's algorithm for the shortest path problem using a modified version of Turing's computational model. This project was done out of curiosity, the implementation is quite messy and it can be improved in terms of efficiency and programming. 

The implementation is based on the turing_machine implementation of Philipp Engelmann. Philipp's implementation can be found here: https://github.com/phillikus/turing_machine. 

My implementation can be found in the following notebook: 

## Comments about the implementation and my experience.

All numbers are stored in binary. Arithmetic is done in binary. This allowed me to have an implementation where the number of states does not depend on the data. I allocate certain number of bits to store binary numbers. This limits the type of data that this implementation can work with. But, one can always increase the number of bits if they have enough memory. 

I started this implementation with one tape only. This became quite hectic somewhere at 3/4 of the implementation. That's where I introduced two additional tapes for storing the previous node of a node and also for storing temporary numbers. 

I utilize Phillip's implementation of a Turing machine to build some core states (functions) such as printing and finding symbols on a tape. However, because Phillip's implementation did not allow easy composition of turing machines I used python to control the flow of the program on top of core functionality offered in Phillip's implementation. However, I only allow reading, printing and moving left and right on a tape. I utilize a couple of Python variables to control the flow of the program. This goes beyond Turing's original model. The variables store one symbol each and they have one cell. Therefore, these variables could trivially be simulated by having an additional tape for each variable.

Interestingly, my implementation of Dijkstra using Turing's model is close to 3000 lines of code. This excludes Phillip's core functionality. That's way more than an implementation of Dijkstra on standard computational models that conventional hardware implements. My implementation can certainly be improved, but that's going to be version 2.

I have tested my implementation but not extensively. It should be working on connected and directed graphs with integer weights for the edges. It is working for the small number of tests that I made so I will consider this as "fine" since I would prefer to move on to a more efficient implementation before I do extensive testing. 
