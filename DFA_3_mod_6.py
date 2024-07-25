# when interpreted as binary number, equivalent to 3 mod 6
class DFA:
    def __init__(self):
        self.states = {
            'q0': {'0': 'q0', '1': 'q1'},
            'q1': {'0': 'q2', '1': 'q3'},
            'q2': {'0': 'q4', '1': 'q5'},
            'q3': {'0': 'q0', '1': 'q1'},
            'q4': {'0': 'q2', '1': 'q3'},
            'q5': {'0': 'q4', '1': 'q5'}
        }
        self.accept_state = 'q3'
        self.current_state = 'q0'
    
    def reset(self):
        self.current_state = 'q0'
    
    def process_input(self, input_str):
        for char in input_str:
            self.current_state = self.states[self.current_state][char]
        return self.current_state == self.accept_state

dfa = DFA()
input_str = '011'
print(f"Does the DFA accept '{input_str}'? {dfa.process_input(input_str)}")