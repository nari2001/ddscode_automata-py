# -*- coding: utf-8 -*-

from automata.fa.dfa import DFA
import random as r

ddsc = ['ドド', 'スコ']  # given list

modulo = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q2', '1': 'q0'},
        'q2': {'0': 'q3', '1': 'q0'},
        'q3': {'0': 'q4', '1': 'q0'},
        'q4': {'0': 'q0', '1': 'q5'},
        'q5': {'0': 'q6', '1': 'q0'},
        'q6': {'0': 'q7', '1': 'q0'},
        'q7': {'0': 'q8', '1': 'q0'},
        'q8': {'0': 'q0', '1': 'q9'},
        'q9': {'0': 'q10', '1': 'q0'},
        'q10': {'0': 'q11', '1': 'q0'},
        'q11': {'0': 'q12', '1': 'q0'},
        'q12': {'0': 'q12', '1': 'q12'}
    },
    initial_state='q0',
    final_states={'q12'}
)

# convert <'ドド' and 'スコ'> into <'1' and '0'>
ddsc_cvt = {'ドド': '1', 'スコ': '0'}

# first random choice from <'ドド' and 'スコ'>
choice_first = r.choice(ddsc)
print(choice_first)
nums = ddsc_cvt[choice_first]  # store as binary numbers (str)

while not modulo.accepts_input(nums):
    # following choice
    choice_follow = r.choice(ddsc)
    print(choice_follow)
    num = ddsc_cvt[choice_follow]
    nums += num

    # If you are at 'q0', initialize 'nums'
    if modulo.read_input_stepwise(nums) == 'q0':
        choice_first = r.choice(ddsc)
        print(choice_first)
        nums = ddsc_cvt[choice_first]

print('ラブ注入♡')
