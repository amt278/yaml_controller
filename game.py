import random
import yaml

with open('game_config.yml', 'r') as f:
    config = yaml.safe_load(f)

r_min = config['range']['min']
r_max = config['range']['max']

guesses = config['guesses']

solve = False

correct = 5 #random.randint(r_min, r_max)
is_solved = False

for i in range(guesses):
    guess = int(input('enter a number: '))
    if guess == correct:
        print('correct!!')
        is_solved = True
        break
    elif guess > correct:
        print('too high')
    else:
        print('too low')
else:
    if not is_solved:
        print('you lost')
