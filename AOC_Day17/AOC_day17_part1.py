import sys
import re

def combo_operand_value(operand, registers):
    """
    Calculate the value of a combo operand.
    """
    if operand <= 3:
        return operand
    elif operand == 4:
        return registers['A']
    elif operand == 5:
        return registers['B']
    elif operand == 6:
        return registers['C']
    else:
        raise ValueError("Invalid combo operand")

def run_program(initial_registers, program):
    """
    Simulate the execution of the 3-bit computer program.
    
    Args:
        initial_registers: Dictionary with initial values for registers A, B, and C.
        program: List of integers representing the program.

    Returns:
        A string with the output values joined by commas.
    """
    registers = initial_registers.copy()
    instruction_pointer = 0
    output = []

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1] if instruction_pointer + 1 < len(program) else 0

        if opcode == 0:  # adv
            denominator = 2 ** combo_operand_value(operand, registers)
            registers['A'] //= denominator
        elif opcode == 1:  # bxl
            registers['B'] ^= operand
        elif opcode == 2:  # bst
            registers['B'] = combo_operand_value(operand, registers) % 8
        elif opcode == 3:  # jnz
            if registers['A'] != 0:
                instruction_pointer = operand
                continue
        elif opcode == 4:  # bxc
            registers['B'] ^= registers['C']
        elif opcode == 5:  # out
            output.append(combo_operand_value(operand, registers) % 8)
        elif opcode == 6:  # bdv
            denominator = 2 ** combo_operand_value(operand, registers)
            registers['B'] = registers['A'] // denominator
        elif opcode == 7:  # cdv
            denominator = 2 ** combo_operand_value(operand, registers)
            registers['C'] = registers['A'] // denominator
        else:
            raise ValueError(f"Invalid opcode: {opcode}")

        instruction_pointer += 2

    return ",".join(map(str, output))

# Example input
initial_registers = {
    'A': 44374556,
    'B': 0,
    'C': 0
}

program = [2,4,1,5,7,5,1,6,0,3,4,1,5,5,3,0]

# Run the program and print the result
result = run_program(initial_registers, program)
print(result)
