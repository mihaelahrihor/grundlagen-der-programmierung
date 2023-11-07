from logik.hangman import guess,win
from repozitory.state import get_current_state
from repozitory.state import add_state

def hide_word(word, guesses):
    new_word = ''

    for idx in range(len(word))
        if idx in guesses:
            new_word += word[idx]
        else:
            new_word += '_'
    return new_word

def print_state(states, word, max_tries):
    current_state = get_current_state(states)
    """
    max_tries: 10
    guessed: 3
    tries_left: 2
    M_A_S____
    """

    return f'max_tries: \t {max_tires} \n guessed: \t {current_state} \n tries_left: \t \{max_tries - current_state}'

def run(word, states):
    set_initial_states(states, word)

    print(print_state(states, word, tries))

    while True:
        choice = input('choice= ')

        new_state = guess(word, choice, get_current_state(states))
        add_state(states, new_state)

        if get_current_state(states)[0] > max_tries:
            print('You lost')
            return False

        if win(states,word,max_tries):
            print('OK')