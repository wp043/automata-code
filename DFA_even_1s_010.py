# contains even number of 1s and ends in 010
class DFA:
    def __init__(self):
        self.states = {
            'qevenqi': {'0': 'qevenq0', '1': 'qoddqi'},
            'qoddqi': {'0': 'qoddq0', '1': 'qevenqi'},
            'qevenq0': {'0': 'qevenq0', '1': 'qoddq01'},
            'qoddq0': {'0': 'qoddq0', '1': 'qevenq01'},
            'qevenq01': {'0': 'qevenq010', '1': 'qoddqi'},
            'qoddq01': {'0': 'qoddq010', '1': 'qevenqi'},
            'qevenq010': {'0': 'qevenq0', '1': 'qoddq01'},
            'qoddq010': {'0': 'qoddq0', '1': 'qevenq01'}
        }
        self.accept_state = 'qevenq010'
        self.current_state = 'qevenqi'
    
    def reset(self):
        self.current_state = 'qevenqi'
    
    def process_input(self, input_str):
        for char in input_str:
            self.current_state = self.states[self.current_state][char]
        return self.current_state == self.accept_state

dfa = DFA()
input_str = '1010'
print(f"Does the DFA accept '{input_str}'? {dfa.process_input(input_str)}")