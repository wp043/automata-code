# PDA to 1-PDA
class PDA:
    def __init__(self, states, alphabet, stack_alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.stack_alphabet = stack_alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
        self.stack = []

    def reset(self):
        self.stack = []

    def process_input(self, input_str):
        current_state = self.start_state
        for char in input_str:
            transition_key = (current_state, char)
            if transition_key in self.transitions:
                next_state, stack_action = self.transitions[transition_key]
                current_state = next_state
                if stack_action == "pop":
                    if self.stack:
                        self.stack.pop()
                elif stack_action == "push":
                    self.stack.append(char)
        return current_state in self.accept_states

states = {'q0', 'q1', 'q2'}
alphabet = {'a', 'b'}
stack_alphabet = {'$', 'a', 'b'}
transitions = {
    ('q0', 'a'): ('q1', 'push'),
    ('q1', 'b'): ('q2', 'pop'),
}
start_state = 'q0'
accept_states = {'q2'}

pda = PDA(states, alphabet, stack_alphabet, transitions, start_state, accept_states)
input_str = 'ab'
print(f"Does the PDA accept '{input_str}'? {pda.process_input(input_str)}")
