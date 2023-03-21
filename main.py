import random
stack = []

import random

def generate_brainfuck(num):
    """
    Generates a Brainfuck program with matching opening and closing brackets.
    """
    code = ''
    stack = []

    for i in range(num):
        instructions = ['+', '-', '<', '>', '.', '[']
        weights = [2.8, 0.2, 0.2, 0.2, 0.2, 0.6]
        instruction = random.choices(instructions, weights)[0]
        code += instruction

        if instruction == '[':
            stack.append(len(code) - 1)
        elif instruction == ']':
            if len(stack) == 0:
                # No matching opening bracket, add one at beginning of code
                code = '[' + code
                stack.append(0)
            else:
                # Match opening bracket with this closing bracket
                open_bracket_pos = stack.pop()
                code = code[:open_bracket_pos] + '[' + code[open_bracket_pos:]
                code += ']'

    # Add remaining opening brackets as closing brackets at end of code
    while len(stack) > 0:
        open_bracket_pos = stack.pop()
        code = code[:open_bracket_pos] + '[' + code[open_bracket_pos:]
        code += ']'

    return code



def execute_brainfuck(code):
    """
    Executes the given Brainfuck code and returns its output.
    """
    tape = [0] * 30000
    tape_pos = 0
    code_pos = 0
    output = ''

    while code_pos < len(code):
        command = code[code_pos]


        if command == '>':
            if tape_pos < len(tape) - 1:
                tape_pos += 1
            else:
                # Handle error - trying to access memory cell outside the range of the tape
                break
        elif command == '<':
            if tape_pos > 0:
                tape_pos -= 1
            else:
                # Handle error - trying to access memory cell outside the range of the tape
                break
        elif command == '+':
            tape[tape_pos] += 1
        elif command == '-':
            tape[tape_pos] -= 1
        elif command == '.':
            if tape[tape_pos] < 0 or tape[tape_pos] > 127:
                output += '?'
                print('?', end='')
            else:
                output += chr(tape[tape_pos])
                print(chr(tape[tape_pos]), end='')
        elif command == ',':
            tape[tape_pos] = ord(input())
        elif command == '[':
            if tape[tape_pos] == 0:
                # Skip to matching closing bracket
                while code_pos < len(code) - 1:
                    code_pos += 1
                    if code_pos < len(code) and code[code_pos] == '[':
                        stack.append(code_pos)
                    elif code_pos < len(code) and code[code_pos] == ']':
                        if len(stack) > 0:
                            stack.pop()
                        else:
                            # Handle error - trying to access instruction outside the range of the code
                            break
            else:
                stack.append(code_pos)
        elif command == ']':
            if len(stack) > 0:
                open_bracket_pos = stack.pop()
                if tape[tape_pos] != 0:
                    code_pos = open_bracket_pos
                    stack.append(open_bracket_pos)

        code_pos += 1

    return output


# Generate Brainfuck code
code = generate_brainfuck(1000)

# Execute Brainfuck code


# Print results
print("Generated Brainfuck code: ")
print(code)
print("\nOutput:")
output = execute_brainfuck(code)
print(output)
