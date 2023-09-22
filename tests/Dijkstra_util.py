import sys
sys.path.insert(1, '/Users/kimonfountoulakis/Downloads/turing_machine-master/src')

from turing_machine import TuringMachine
from state import State, StateType
from transition import Transition
from direction import Direction
from tape import Tape

def print_symbol(tape, symbol, verbose=False):
    
    states = [
                State("s0", StateType.Start),
                State("sf", StateType.Final)
             ]

    transitions = [
                     Transition("s0", "*", "sf", symbol, Direction.Neutral)
                  ]
    
    return TuringMachine(states, transitions, tape, verbose)

def move(tape, direction, verbose=False):
    
    states = [
                State("s0", StateType.Start),
                State("sf", StateType.Final)
             ]

    transitions = [
                     Transition("s0", "*", "sf", "*", direction)
                  ]
    
    return TuringMachine(states, transitions, tape, verbose)


def find_symbol(tape, symbol, direction, verbose=False):
    
    states = [
                State("s0", StateType.Start),
                State("sf", StateType.Final)
             ]

    transitions = [        
                     Transition("s0", "*", "s0", "*", direction),
                     Transition("s0", "E", "sf", "*", Direction.Neutral),
                     Transition("s0", symbol, "sf", "*", Direction.Neutral)
                  ]
    
    return TuringMachine(states, transitions, tape, verbose)

def find_symbol_delete(tape, symbol, direction, verbose=False):
    
    tm = find_symbol(tape, symbol, direction, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, ' ', verbose=verbose)
    tm.process(verbose=verbose)
    
    return tm

def if_else_find_print(tape, check_symbol, symbol_find, symbol_print, direction, verbose=False):
    
    if tape.read() == check_symbol[0]:
        
        tm = find_symbol(tape, symbol_find, direction, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = print_symbol(tape, symbol_print[0], verbose=verbose)
        tm.process(verbose=verbose)
    else:
        tm = find_symbol(tape, symbol_find, direction, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = print_symbol(tape, symbol_print[1], verbose=verbose)
        tm.process(verbose=verbose)
        
    return tm

def copy_data_between_two_symbols(tape, symbol1, symbol2, symbol3, symbols_if, symbols_print, verbose=False):
    
    # symbol1: The symbol which determines the start of the data on the tape.
    # symbol2: The symbol which determines where to copy the data on the tape.
    # symbol3: The symbol which determines when to stop the copying process. 
    
    while True:
    
        if tape.read() != symbol3:
            tm = if_else_find_print(tape, symbols_if, symbol2, symbols_print, Direction.Right, verbose=verbose)

            tm = find_symbol_delete(tape, symbol1, Direction.Left, verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, symbol1, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
        else:
            tm = find_symbol_delete(tape, symbol1, Direction.Right, verbose=verbose)
            break
            
    return tm

def copy_between_two_symbols(tape, symbol1, symbol2, symbol3, symbols_if, symbols_print, verbose=False):
    
    # symbol1: The symbol which determines the start of the data on the tape.
    # symbol2: The symbol which determines where to copy the data on the tape.
    # symbol3: The symbol which determines when to stop the copying process. 
    
    while True:
            
        if tape.read() == symbols_if[0]:  
            tm = find_symbol(tape, symbol2, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, symbols_print[0], verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            if tape.read() == symbol3:
                break
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
                
            tm = print_symbol(tape, symbol2, verbose=verbose)
            tm.process(verbose=verbose)  
            
            tm = find_symbol(tape, symbol1, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape, symbol1, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

        else:
            tm = find_symbol(tape, symbol2, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, symbols_print[1], verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            if tape.read() == symbol3:
                break
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
                
            tm = print_symbol(tape, symbol2, verbose=verbose)
            tm.process(verbose=verbose)  
            
            tm = find_symbol(tape, symbol1, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape, symbol1, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
            
    return tm

def initialize_distance_for_seed_node(tape, symbol1, symbol2, symbol3, symbol4, symbol5, symbols_if, symbols_print, verbose=False):
    
    # symbol1: The symbol which determines the start of the data on the tape.
    # symbol2: The symbol which determines where to copy the data on the tape.
    # symbol3: The symbol which determines when to stop the copying process. 
    # symbol4: The symbol which distinguishes the node ID from the distance to the source node.
    # symbol5: The symbol which determines the start of the tape.
    
    tm = copy_data_between_two_symbols(tape, symbol1, symbol2, symbol3, symbols_if, symbols_print, verbose=verbose)

    tm = find_symbol(tape, symbol5, Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, symbol1, verbose=verbose)
    tm.process(verbose=verbose)

    tm = find_symbol(tape, symbol2, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, symbol4, verbose=verbose)
    tm.process(verbose=verbose)

    tm = find_symbol(tape, symbol1, Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)

    tm = copy_data_between_two_symbols(tape, symbol1, symbol2, symbol3, symbols_if, ['0', '0'], verbose=verbose)
    
    tm = find_symbol(tape, symbol5, Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)
    
    return tm

def if_else_find_check(tape, check_symbol, symbol_find, direction, verbose=False):
    
    if tape.read() == check_symbol[0]:
        
        tm = find_symbol(tape, symbol_find, direction, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)

        if tape.read() != check_symbol[0]:
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'X', verbose=verbose)
            tm.process(verbose=verbose)
        else:
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
    else:

        tm = find_symbol(tape, symbol_find, direction, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        if tape.read() != check_symbol[1]:
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'X', verbose=verbose)
            tm.process(verbose=verbose)

        else:
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
        
    return tm

def check_bits_between_two_symbols(tape, symbol1, symbol2, symbol3, symbols_if, direction1, direction2, verbose=False):
    
    # symbol1: The symbol which determines the start of the data on the tape.
    # symbol2: The symbol which determines where to copy the data on the tape.
    # symbol3: The symbol which determines when to stop the copying process. 
    
    while True:
        # This if statement is equivalent to a state where we check 
        # at the current position of the tape we observe symbol3.
        # If we do, then we terminate the machine.
        if tape.read() != symbol3 and tape.read() != 'M':
            tm = if_else_find_check(tape, symbols_if, symbol2, direction1, verbose=verbose)  
            
            # This if statement is equivalent to a state where we check 
            # at the current position of the tape we observe symbol3.
            # If we do, then we terminate the machine.
            if tape.read() == 'X':
                return tm
            else:
                
                tm = print_symbol(tape, ' ', verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
            
                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = print_symbol(tape, symbol2, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = find_symbol(tape, symbol1, direction2, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = print_symbol(tape, ' ', verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                if tape.read() == 'E':
                    tm = move(tape, Direction.Left, verbose=verbose)
                    tm.process(verbose=verbose)
                    
                    tm = print_symbol(tape, 'D', verbose=verbose)
                    tm.process(verbose=verbose)
                    
                    break
                
                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = print_symbol(tape, symbol1, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
        else:
            return tm
        
    return tm

def initialize_distance_of_node(tape, prev_termination_symbol, next_termination_symbol, verbose=False):

    tm = print_symbol(tape, '$', verbose=verbose)
    tm.process(verbose=verbose)

    tm = find_symbol(tape, 'A', Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, ' ', verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = find_symbol(tape, prev_termination_symbol, Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, 'A', verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)

    tm = copy_data_between_two_symbols(tape, 'A', 'E', next_termination_symbol, ['0', '1'], ['0', '1'], verbose=verbose)

    tm = find_symbol(tape, prev_termination_symbol, Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, 'A', verbose=verbose)
    tm.process(verbose=verbose)

    tm = find_symbol(tape, 'E', Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, '-', verbose=verbose)
    tm.process(verbose=verbose)

    tm = find_symbol(tape, 'A', Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)

    tm = copy_data_between_two_symbols(tape, 'A', 'E', next_termination_symbol, ['0', '1'], ['1', '1'], verbose=verbose)
    
    return tm

def check_which_termination(tape, termination_symbol, verbose=False):
    
    if tape.read() == 'X':
        
        tm = print_symbol(tape, ' ', verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = find_symbol(tape, '$', Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        if tape.read() == 'E':
            if termination_symbol == ':':
                tm = initialize_distance_of_node(tape, '-', ':', verbose=verbose)
                
                tm = find_symbol(tape, '#', Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                if tape.read() == 'E':
                    return termination_symbol
                
                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = print_symbol(tape, 'A', verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = find_symbol(tape, 'd', Direction.Right, verbose=verbose)
                tm.process(verbose=verbose);

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = print_symbol(tape, 'B', verbose=verbose)
                tm.process(verbose=verbose)

                tm = find_symbol(tape, 'A', Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
                
                termination_symbol = '-'
            else:
                tm = initialize_distance_of_node(tape, '#', '-', verbose=verbose)
                
                tm = find_symbol(tape, '-', Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = print_symbol(tape, 'A', verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = find_symbol(tape, 'd', Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = print_symbol(tape, 'B', verbose=verbose)
                tm.process(verbose=verbose)

                tm = find_symbol(tape, 'A', Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
                
                termination_symbol = ':'
                
            return termination_symbol

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = print_symbol(tape, 'B', verbose=verbose)
        tm.process(verbose=verbose)

        tm = find_symbol(tape, 'A', Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
            
        tm = print_symbol(tape, ' ', verbose=verbose)
        tm.process(verbose=verbose)
        
        if termination_symbol == '-':
            tm = find_symbol(tape, '#', Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
        else:
            tm = find_symbol(tape, '-', Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
            
        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = print_symbol(tape, 'A', verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
    elif tape.read() == '-':
        
        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = print_symbol(tape, ' ', verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = print_symbol(tape, 'A', verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = find_symbol(tape, 'B', Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = print_symbol(tape, ' ', verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = find_symbol(tape, 'd', Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = print_symbol(tape, 'B', verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = find_symbol(tape, 'A', Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        termination_symbol = ':'

    elif tape.read() == ':':

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = print_symbol(tape, ' ', verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = find_symbol(tape, '#', Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        if tape.read() == 'E':
            
            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = find_symbol(tape, 'B', Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = find_symbol(tape, '@', Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
            
            return termination_symbol

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = print_symbol(tape, 'A', verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = find_symbol(tape, 'B', Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = print_symbol(tape, ' ', verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = find_symbol(tape, 'd', Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = print_symbol(tape, 'B', verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = find_symbol(tape, 'A', Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        termination_symbol = ':'

    else:
        print("ERROR?")
        
    return termination_symbol

def initialize_distance_data(tape, verbose=False):
    
    # Initialize distance data
    tm = initialize_distance_for_seed_node(tape, 'A', 'E', '#', '-', '@', ['0', '1'], ['0', '1'], verbose=verbose)

    ## Initialize the distance for the rest of the nodes.

    ### Set marker A for the first bit of the node.
    tm = find_symbol(tape, '#', Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, 'A', verbose=verbose)
    tm.process(verbose=verbose)

    ### Set marker B for the first bit of the first node in the distance data.
    tm = find_symbol(tape, 'd', Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, 'B', verbose=verbose)
    tm.process(verbose=verbose)

    tm = find_symbol(tape, 'A', Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)

    ### Initialization loop.
    termination_symbol = '-'
    
    while tape.read() != '@':

        tm = check_bits_between_two_symbols(tape, 'A', 'B', termination_symbol, ['0', '1'], Direction.Right, Direction.Left, verbose=verbose)

        termination_symbol = check_which_termination(tape, termination_symbol, verbose=verbose)
        
    return tm

def initialize_tape(tape, verbose=False):

    # Some initialization steps.
    tm = find_symbol(tape, 'E', Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, 'd', verbose=verbose)
    tm.process(verbose=verbose)

    tm = find_symbol(tape, '@', Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, 'A', verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)
    
    return tm

def initialize_nodes_in_the_queue(tape, verbose=False):
    
    tm = find_symbol(tape, 'E', Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = print_symbol(tape, 'Q', verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = find_symbol(tape, 'd', Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, 'A', verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = move(tape, Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)
    
    while True:
    
        tm = copy_data_between_two_symbols(tape, 'A', 'E', '-', ['0', '1'], ['0', '1'], verbose=verbose)

        tm = find_symbol(tape, '$', Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        if tape.read() == 'E':
            break

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = print_symbol(tape, 'A', verbose=verbose)
        tm.process(verbose=verbose)

        tm = find_symbol(tape, 'E', Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = print_symbol(tape, '-', verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = find_symbol(tape, 'A', Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
    
    return tm

def initialize_minimum_distance(tape, verbose=False):
    
    tm = print_symbol(tape, 'M', verbose=verbose)
    tm.process(verbose=verbose)

    tm = find_symbol(tape, '@', Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, 'A', verbose=verbose)
    tm.process(verbose=verbose)

    tm = copy_data_between_two_symbols(tape, 'A', 'E', '#', ['0', '1'], ['1', '1'], verbose=verbose)

#     tm = move(tape, Direction.Left, verbose=verbose)
#     tm.process(verbose=verbose)

#     tm = find_symbol(tape, '@', Direction.Left, verbose=verbose)
#     tm.process(verbose=verbose)

    return tm

def initialize_minimum_distance_node(tape, verbose=False):
    
    tm = find_symbol(tape, 'E', Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = print_symbol(tape, 'U', verbose=verbose)
    tm.process(verbose=verbose)

    tm = find_symbol(tape, '@', Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, 'A', verbose=verbose)
    tm.process(verbose=verbose)

    tm = copy_data_between_two_symbols(tape, 'A', 'E', '#', ['0', '1'], ['0', '0'], verbose=verbose)

    tm = move(tape, Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)

    tm = find_symbol(tape, '@', Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)
    
    return tm

def compare_numbers(tape, verbose=False):
    
    if tape.read() == '0':
        
        tm = find_symbol(tape, 'C', Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        if tape.read() != '0':
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape, 'D', verbose=verbose)
            tm.process(verbose=verbose)
    else:
        tm = find_symbol(tape, 'C', Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        if tape.read() != '1':
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape, 'X', verbose=verbose)
            tm.process(verbose=verbose)
              
    return 0 # do nothing
    
def copy_number_to_min_memory(tape, verbose=False):
    
    while True:
    
        tm = compare_numbers(tape, verbose=verbose)
        
        if tape.read() == 'D' or tape.read() == 'X':
            break
        
        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        if tape.read() == 'U':
            break
        else:
            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = print_symbol(tape, ' ', verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = print_symbol(tape, 'C', verbose=verbose)
        tm.process(verbose=verbose)

        tm = find_symbol(tape, 'B', Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)

        tm = print_symbol(tape, ' ', verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = print_symbol(tape, 'B', verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
       
    if tape.read() == 'D':
        tm = print_symbol(tape, ' ', verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = find_symbol(tape, 'M', Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = print_symbol(tape, 'C', verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = find_symbol(tape, 'B', Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = print_symbol(tape, ' ', verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = find_symbol(tape, '-', Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = print_symbol(tape, 'B', verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = copy_between_two_symbols(tape, 'B', 'C', 'U', ['0', '1'], ['0', '1'], verbose=verbose)
        
        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = print_symbol(tape, 'D', verbose=verbose)
        tm.process(verbose=verbose)
    elif tape.read() == 'X':
        tm = print_symbol(tape, ' ', verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = find_symbol(tape, 'M', Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        if tape.read() != 'A':
            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)
    else:
        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = print_symbol(tape, ' ', verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = find_symbol(tape, 'M', Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        if tape.read() != 'A':
            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)
    
    return tm

def find_minimum(tape, verbose=False):
    
    tm = find_symbol(tape, 'Q', Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)
    
    previous_starting_symbol = 'Q'
    
    previous_starting_symbol = check_if_node_in_queue(tape, previous_starting_symbol, verbose=verbose)
    
    if tape.read() == 'E':
        return tm

    tm = print_symbol(tape, 'A', verbose=verbose)
    tm.process(verbose=verbose)

    tm = find_symbol(tape, 'd', Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, 'B', verbose=verbose)
    tm.process(verbose=verbose)

    tm = find_symbol(tape, 'A', Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)
    
    while True:

        # checks if the numbers between two symbols are the same
        tm = check_bits_between_two_symbols(tape, 'A', 'B', '-', ['0', '1'], Direction.Left, Direction.Right, verbose)
        
        if tape.read() == 'X':
            # Enter here if the numbers are different
            
            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, '$', Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'B', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, 'A', Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, previous_starting_symbol, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'A', verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

        else:  
            # Enter here if the numbers are the same 
            tm = find_symbol(tape, 'M', Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'C', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, 'B', Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'B', verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
            
            # copy the distance to memory if the distance is smaller than the minimum distance
            tm = copy_number_to_min_memory(tape, verbose=verbose)
            
            if tape.read() == 'D':
                tm = print_symbol(tape, ' ', verbose=verbose)
                tm.process(verbose=verbose) 
                
                tm = find_symbol(tape, 'U', Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = print_symbol(tape, 'C', verbose=verbose)
                tm.process(verbose=verbose) 
                
                tm = find_symbol(tape, 'A', Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = print_symbol(tape, ' ', verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = find_symbol(tape, previous_starting_symbol, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = print_symbol(tape, 'A', verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = copy_between_two_symbols(tape, 'A', 'C', 'E', ['0', '1'], ['0', '1'], verbose=verbose)
            
                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
            
                tm = find_symbol(tape, 'A', Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = print_symbol(tape, ' ', verbose=verbose)
                tm.process(verbose=verbose)
            
                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                previous_starting_symbol = check_if_node_in_queue(tape, previous_starting_symbol, verbose=verbose)
                
                if tape.read() == 'E': 
                    tm = move(tape, Direction.Left, verbose=verbose)
                    tm.process(verbose=verbose)

                    tm = find_symbol(tape, '@', Direction.Left, verbose=verbose)
                    tm.process(verbose=verbose)
                
                    break
                
                tm = print_symbol(tape, 'A', verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = find_symbol(tape, 'B', Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = print_symbol(tape, ' ', verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = find_symbol(tape, 'd', Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = print_symbol(tape, 'B', verbose=verbose)
                tm.process(verbose=verbose)

                tm = find_symbol(tape, 'A', Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
            else:
                
                if tape.read() == 'A':
                    tm = print_symbol(tape, ' ', verbose=verbose)
                    tm.process(verbose=verbose)
                    break
                    
                tm = print_symbol(tape, ' ', verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = find_symbol(tape, 'A', Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)

                tm = print_symbol(tape, ' ', verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                previous_starting_symbol = check_if_node_in_queue(tape, previous_starting_symbol, verbose=verbose)
                
                if tape.read() == 'E':                    
                    break

                tm = print_symbol(tape, 'A', verbose=verbose)
                tm.process(verbose=verbose)

                tm = find_symbol(tape, 'B', Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)

                tm = print_symbol(tape, ' ', verbose=verbose)
                tm.process(verbose=verbose)

                tm = find_symbol(tape, 'd', Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = print_symbol(tape, 'B', verbose=verbose)
                tm.process(verbose=verbose)

                tm = find_symbol(tape, 'A', Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
            
            previous_starting_symbol = '-'
            
    return tm

def remove_node_from_queue(tape, verbose=False):
    
    tm = find_symbol(tape, 'U', Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, 'A', verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = find_symbol(tape, 'B', Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = print_symbol(tape, ' ', verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = find_symbol(tape, 'Q', Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)
    
    go_to_symbol = 'Q'
    
    go_to_symbol = find_next_in_queue(tape, go_to_symbol, verbose=verbose)
    
    if tape.read() == 'E':
        print("TERMINATE: remove_node_from_queue")
    
    tm = print_symbol(tape, 'B', verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = find_symbol(tape, 'A', Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = move(tape, Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)
    
    while True:
    
        tm = check_bits_between_two_symbols(tape, 'A', 'B', 'E', ['0', '1'], Direction.Left, Direction.Right, verbose)

        if tape.read() == 'D':

            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, 'B', Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose) 
            
            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, go_to_symbol, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'Y', verbose=verbose)
            tm.process(verbose=verbose) 
            
            break
        else:
            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose) 
            
            tm = find_symbol(tape, '-', Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            go_to_symbol = find_next_in_queue(tape, go_to_symbol, verbose=verbose)
            
            if tape.read() == 'E':
                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = find_symbol(tape, '@', Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
                
                break

            tm = print_symbol(tape, 'B', verbose=verbose)
            tm.process(verbose=verbose) 
            
            tm = find_symbol(tape, 'U', Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'A', verbose=verbose)
            tm.process(verbose=verbose) 
            
            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
    
            go_to_symbol = '-'
        
    tm = find_symbol(tape, '@', Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)
            
    return tm

def check_if_node_in_queue(tape, previous_starting_symbol, verbose=False):
    
    while tape.read() == 'Y':

        tm = find_symbol(tape, '-', Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        if tape.read() == 'E':
            break

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        previous_starting_symbol = '-'

    return previous_starting_symbol

def initialize_distance_data_second_tape(tape, tape_prev_nodes, verbose=False):
    
    tm = find_symbol(tape, 'd', Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = move(tape_prev_nodes, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)
    
    while tape.read() != 'E':
        
        if tape.read() == '0':
            tm = print_symbol(tape_prev_nodes, '0', verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape_prev_nodes, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape_prev_nodes, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
        elif tape.read() == '1':
            tm = print_symbol(tape_prev_nodes, '1', verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape_prev_nodes, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape_prev_nodes, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
        elif tape.read() == '-':
            tm = print_symbol(tape_prev_nodes, '-', verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape_prev_nodes, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape_prev_nodes, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
        elif tape.read() == '$':
            tm = print_symbol(tape_prev_nodes, '$', verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape_prev_nodes, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape_prev_nodes, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
        else:
            print("Error")
            
        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
    tm = find_symbol(tape, '@', Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)
            
    return tm

def add_two_bits(tape, tape_temp, carry, verbose=False):
    
    if tape.read() == '0':
        tm = find_symbol(tape, 'B', Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)  
        
        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        if tape.read() == '0' and carry == 0:
            tm = print_symbol(tape_temp, '0', verbose=verbose)
            tm.process(verbose=verbose)
            carry = 0
        elif tape.read() == '0' and carry == 1:
            tm = print_symbol(tape_temp, '1', verbose=verbose)
            tm.process(verbose=verbose)
            carry = 0
        elif tape.read() == '1' and carry == 0:
            tm = print_symbol(tape_temp, '1', verbose=verbose)
            tm.process(verbose=verbose)
            carry = 0
        elif tape.read() == '1' and carry == 1:
            tm = print_symbol(tape_temp, '0', verbose=verbose)
            tm.process(verbose=verbose)
            carry = 1
        
    elif tape.read() == '1':
        tm = find_symbol(tape, 'B', Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)  
        
        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        if tape.read() == '0' and carry == 0:
            tm = print_symbol(tape_temp, '1', verbose=verbose)
            tm.process(verbose=verbose)
            carry = 0
        elif tape.read() == '0' and carry == 1:
            tm = print_symbol(tape_temp, '0', verbose=verbose)
            tm.process(verbose=verbose)
            carry = 1
        elif tape.read() == '1' and carry == 0:
            tm = print_symbol(tape_temp, '0', verbose=verbose)
            tm.process(verbose=verbose)
            carry = 1
        elif tape.read() == '1' and carry == 1:
            tm = print_symbol(tape_temp, '1', verbose=verbose)
            tm.process(verbose=verbose)
            carry = 1
    else:
        print("Error in adding numbers")
        
    return carry

def add_two_numbers(tape, tape_temp, carry, verbose=False):
    
    while True:

        carry = add_two_bits(tape, tape_temp, carry, verbose=verbose)
        
        tm = move(tape_temp, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape_temp, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = print_symbol(tape, ' ', verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)

        tm = print_symbol(tape, 'B', verbose=verbose)
        tm.process(verbose=verbose)

        tm = find_symbol(tape, 'A', Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = print_symbol(tape, ' ', verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)

        tm = print_symbol(tape, 'A', verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)

        if tape.read() == 'M':
            break

    return tm

def check_if_in_queue_and_compute_temp_number(tape, verbose=False):
    
    while True:
    
        tm = check_bits_between_two_symbols(tape, 'A', 'B', '-', ['0', '1'], Direction.Left, Direction.Right, verbose)

        if tape.read() == '-' or tape.read() == 'M':
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, 'B', Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, '#', Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            if tape.read() == 'E':
                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = find_symbol(tape, 'd', Direction.Left, verbose=verbose)
                tm.process(verbose=verbose) 

                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)

                tm = print_symbol(tape, 'B', verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
            else:
                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)

                tm = print_symbol(tape, 'B', verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)

            tm = find_symbol(tape, 'U', Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'A', verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            # make new tape for temporary data, for convenience
            tape_temp = Tape('', '01 ')
            
            tm = find_symbol(tape, '@', Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            while tape.read() != '#':
                tm = move(tape_temp, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = print_symbol(tape_temp, '0', verbose=verbose)
                tm.process(verbose=verbose) 
                
                tm = move(tape_temp, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

            tm = move(tape_temp, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = find_symbol(tape, 'A', Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
                
            carry = 0

            tm = add_two_numbers(tape, tape_temp, carry, verbose=verbose)

            return tape_temp

        else:
            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, '-', Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'B', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, 'A', Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, '-', Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'A', verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

def find_next_in_queue(tape, go_to_symbol, verbose=False):
    
    while True:
    
        if tape.read() == 'Y':
            tm = find_symbol(tape, '-', Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            if tape.read() == 'E':
                break
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            go_to_symbol = '-'
        else: 
            break
        
    return go_to_symbol

def if_else_find_check_in_different_tape(tape, tape_2, check_symbol, symbol_find, verbose=False):
    
    if tape_2.read() == check_symbol[0]:

        if tape.read() != check_symbol[0]:
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'X', verbose=verbose)
            tm.process(verbose=verbose)
        else:
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
    else:
        
        if tape.read() != check_symbol[1]:
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'X', verbose=verbose)
            tm.process(verbose=verbose)

        else:
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
        
    return tm

def check_bits_between_two_symbols_in_different_tape(tape, tape_2, symbol1, symbol2, symbol3, symbols_if, verbose=False):
    
    # symbol1: The symbol which determines the start of the data on the tape.
    # symbol2: The symbol which determines where to copy the data on the tape.
    # symbol3: The symbol which determines when to stop the copying process. 
    
    while True:
        # This if statement is equivalent to a state where we check 
        # at the current position of the tape we observe symbol3.
        # If we do, then we terminate the machine.
        if tape_2.read() != symbol3:
            tm = if_else_find_check_in_different_tape(tape, tape_2, symbols_if, symbol2, verbose=verbose)  
            
            # This if statement is equivalent to a state where we check 
            # at the current position of the tape we observe symbol3.
            # If we do, then we terminate the machine.
            if tape.read() == 'X':
                return tm
            else:
                
                tm = print_symbol(tape, ' ', verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
            
                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = print_symbol(tape, symbol2, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape_2, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = print_symbol(tape_2, ' ', verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape_2, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape_2, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = print_symbol(tape_2, symbol1, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = move(tape_2, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
        else:
            return tm
        
    return tm

def find_in_prev_node_tape(tape, tape_prev_nodes, verbose=False):

    while True:
        tm = check_bits_between_two_symbols_in_different_tape(tape, tape_prev_nodes, 'A', 'B', '-', ['0', '1'], verbose)
    
        if tape.read() == 'X':
            tm = move(tape_prev_nodes, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape_prev_nodes, ' ', verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = find_symbol(tape_prev_nodes, '$', Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape_prev_nodes, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape_prev_nodes, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape_prev_nodes, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape_prev_nodes, 'A', verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape_prev_nodes, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, '-', Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'B', verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
        else:
            tm = move(tape_prev_nodes, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape_prev_nodes, ' ', verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape_prev_nodes, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape_prev_nodes, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape_prev_nodes, 'A', verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape_prev_nodes, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
            
            break
            
    return tm

def find_node_in_distances(tape, verbose=False):

    while True:
        tm = check_bits_between_two_symbols(tape, 'A', 'B', ':', ['0', '1'], Direction.Right, Direction.Left, verbose)
    
        if tape.read() == 'X':
            
            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = find_symbol(tape, '$', Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape, 'B', verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, 'A', Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = find_symbol(tape, '-', Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'A', verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
        else:
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape, 'A', verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
            
            break
            
    return tm

def compare_numbers_and_copy_if_smaller_for_distance_update(tape, tape_temp, verbose=False):
    
    if tape_temp.read() == '0':
        
        if tape.read() != '0':
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape, 'D', verbose=verbose)
            tm.process(verbose=verbose)
    else:
        
        if tape.read() == '0':
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape, 'C', verbose=verbose)
            tm.process(verbose=verbose)
              
    return 0 # do nothing
    
def copy_number_if_smaller_for_distance_update(tape, tape_temp, verbose=False):
    
    while True:
    
        compare_numbers_and_copy_if_smaller_for_distance_update(tape, tape_temp, verbose=verbose)
        
        if tape.read() == 'D' or tape.read() == 'C':
            break
            
        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = print_symbol(tape, ' ', verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = print_symbol(tape, 'B', verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape_temp, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape_temp, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
       
    if tape.read() == 'D':

        tm = print_symbol(tape, ' ', verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = find_symbol(tape, '-', Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = find_symbol(tape_temp, '@', Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)

        tm = move(tape_temp, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = copy_between_two_symbols_for_distances(tape, tape_temp, 'E', ['0', '1'], ['0', '1'], verbose=verbose)

    elif tape.read() == 'C':
        return tm
        
    else:        
        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = print_symbol(tape, ' ', verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = print_symbol(tape, 'B', verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape_temp, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = move(tape_temp, Direction.Right, verbose=verbose)
        tm.process(verbose=verbose)
    
    return tm

def copy_between_two_symbols_for_distances(tape, tape_temp, symbol, symbols_if, symbols_print, verbose=False):
    
    while True:
            
        if tape_temp.read() == symbols_if[0]:
            tm = print_symbol(tape, symbols_print[0], verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape_temp, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape_temp, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

        else:
            tm = print_symbol(tape, symbols_print[1], verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape_temp, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = move(tape_temp, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
        if tape_temp.read() == symbol:            
            break
            
    return tm

def update_distances(tape, tape_prev_nodes, verbose=False):

    tm = find_symbol(tape, '#', Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, 'B', verbose=verbose)
    tm.process(verbose=verbose)

    tm = find_symbol(tape, 'U', Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, 'A', verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)
    
    while True:

        tm = check_bits_between_two_symbols(tape, 'A', 'B', '-', ['0', '1'], Direction.Left, Direction.Right, verbose)

        if tape.read() == 'D':
            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, 'B', Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'B', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, 'Q', Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_next_in_queue(tape, 0, verbose=verbose)

            if tape.read() == 'E':
                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = print_symbol(tape, ' ', verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = find_symbol(tape, '@', Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
                
                break

            tm = print_symbol(tape, 'A', verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
            
            tape_temp = check_if_in_queue_and_compute_temp_number(tape, verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, 'B', Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, '-', Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'B', verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape_prev_nodes, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape_prev_nodes, '@', Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape_prev_nodes, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape_prev_nodes, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape_prev_nodes, 'A', verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape_prev_nodes, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_in_prev_node_tape(tape, tape_prev_nodes, verbose=verbose)

            tm = move(tape_temp, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, '-', Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'A', verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, 'd', Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'B', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, 'A', Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_node_in_distances(tape, verbose=verbose)

            tm = find_symbol(tape, 'B', Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'B', verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = copy_number_if_smaller_for_distance_update(tape, tape_temp, verbose=verbose)
            
            if tape.read() != 'C':
                tm = find_symbol(tape, 'U', Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)

                tm = copy_between_two_symbols_for_distances(tape_prev_nodes, tape, 'E', ['0', '1'], ['0', '1'], verbose=verbose)

                tm = move(tape_prev_nodes, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)

                tm = find_symbol(tape_prev_nodes, 'A', Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)

                tm = print_symbol(tape_prev_nodes, ' ', verbose=verbose)
                tm.process(verbose=verbose)

                tm = find_symbol(tape_prev_nodes, '@', Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)

                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
            else:
                tm = print_symbol(tape, ' ', verbose=verbose)
                tm.process(verbose=verbose) 
                
                tm = move(tape_prev_nodes, Direction.Right, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = print_symbol(tape_prev_nodes, ' ', verbose=verbose)
                tm.process(verbose=verbose)

                tm = find_symbol(tape_prev_nodes, '@', Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
            
            tm = find_symbol(tape, 'A', Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, '#', Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            if tape.read() == 'E':
                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = print_symbol(tape, ' ', verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = find_symbol(tape, '@', Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
                
                break
                
            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'B', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, 'U', Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'A', verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

        else:
            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, '#', Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            if tape.read() == 'E':
                tm = move(tape, Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = print_symbol(tape, ' ', verbose=verbose)
                tm.process(verbose=verbose)
                
                tm = find_symbol(tape, '@', Direction.Left, verbose=verbose)
                tm.process(verbose=verbose)
                
                break

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'B', verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = find_symbol(tape, 'A', Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)
            
            tm = print_symbol(tape, ' ', verbose=verbose)
            tm.process(verbose=verbose)

            tm = find_symbol(tape, 'U', Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Right, verbose=verbose)
            tm.process(verbose=verbose)

            tm = print_symbol(tape, 'A', verbose=verbose)
            tm.process(verbose=verbose)

            tm = move(tape, Direction.Left, verbose=verbose)
            tm.process(verbose=verbose)
    
    return tm

def reset_minimum_distance(tape, verbose=False):
    
    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, 'A', verbose=verbose)
    tm.process(verbose=verbose)

    tm = find_symbol(tape, 'M', Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, 'C', verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = move(tape, Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = find_symbol(tape, 'A', Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = move(tape, Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)

    tm = copy_between_two_symbols(tape, 'A', 'C', 'U', ['0', '1'], ['1', '1'], verbose=verbose)
    
    tm = find_symbol(tape, 'A', Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = print_symbol(tape, ' ', verbose=verbose)
    tm.process(verbose=verbose)

    tm = find_symbol(tape, '@', Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)

    return tm

def reset_minimum_distance_node(tape, verbose=False):
    
    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, 'A', verbose=verbose)
    tm.process(verbose=verbose)

    tm = find_symbol(tape, 'U', Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = print_symbol(tape, 'C', verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = move(tape, Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = find_symbol(tape, 'A', Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = move(tape, Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)

    tm = copy_between_two_symbols(tape, 'A', 'C', 'E', ['0', '1'], ['1', '1'], verbose=verbose)
    
    tm = move(tape, Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = find_symbol(tape, 'A', Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = print_symbol(tape, ' ', verbose=verbose)
    tm.process(verbose=verbose)

    tm = find_symbol(tape, '@', Direction.Left, verbose=verbose)
    tm.process(verbose=verbose)

    return tm

def is_queue_empty(tape, verbose=False):
    
    tm = find_symbol(tape, 'Q', Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)
    
    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)

    tm = move(tape, Direction.Right, verbose=verbose)
    tm.process(verbose=verbose)
    
    temp = find_next_in_queue(tape, '', verbose=verbose)
    
    if tape.read() == 'E':
        tm = move(tape, Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
        tm = print_symbol(tape, 'X', verbose=verbose)
        tm.process(verbose=verbose)
    else:
        tm = find_symbol(tape, '@', Direction.Left, verbose=verbose)
        tm.process(verbose=verbose)
        
    return tm