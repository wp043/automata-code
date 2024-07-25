class TuringMachine:
    def __init__(self, tape, initial_state, final_states, transition_function):
        self.tape = list(tape)
        self.head_position = 0
        self.current_state = initial_state
        self.final_states = final_states
        self.transition_function = transition_function

    def step(self):
        char_under_head = self.tape[self.head_position]
        x = (self.current_state, char_under_head)
        if x in self.transition_function:
            y = self.transition_function[x]
            self.tape[self.head_position] = y[1]
            self.current_state = y[0]
            if y[2] == 'R':
                self.head_position += 1
            elif y[2] == 'L':
                self.head_position -= 1

    def run(self):
        while self.current_state not in self.final_states:
            self.step()
        return ''.join(self.tape).strip('_')

initial_tape = '110'
initial_state = 'q0'
final_states = {'halt'}
transition_function = {
    ('q0', '0'): ('q0', '0', 'R'),
    ('q0', '1'): ('q0', '1', 'R'),
    ('q0', '_'): ('q1', '_', 'L'),
    ('q1', '1'): ('q1', '0', 'L'),
    ('q1', '0'): ('halt', '1', 'L'),
    ('q1', '_'): ('halt', '1', 'L'),
}

tm = TuringMachine(initial_tape + '_', initial_state, final_states, transition_function)
result = tm.run()
print(f"Resulting tape: {result}")