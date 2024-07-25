# contains axb as substring
class NFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def process_input(self, input_str):
        current_states = {self.start_state}
        for char in input_str:
            next_states = set()
            for state in current_states:
                if (state, char) in self.transition_function:
                    next_states.update(self.transition_function[(state, char)])
            current_states = next_states
        return any(state in self.accept_states for state in current_states)

states = {'q0', 'q1', 'q2'}
alphabet = {'a', 'b', '0', '1'}
transition_function = {
    ('q0', 'a'): {'q1'},
    ('q1', 'b'): {'q2'},
    ('q1', '0'): {'q1'},
    ('q1', '1'): {'q1'}
}
start_state = 'q0'
accept_states = {'q2'}

nfa = NFA(states, alphabet, transition_function, start_state, accept_states)
input_str = 'a01b'
print(f"Does the NFA accept '{input_str}'? {nfa.process_input(input_str)}")