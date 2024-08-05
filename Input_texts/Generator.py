import random

# file = open('random_numbers.txt')
N_inputs = int(1e6)
for _ in range(N_inputs) :
    a = random.randint(0, 4)
    b = random.randint(0, 4)
    result = a + b

    with open('Input_texts/random_numbers.txt', "a") as f :
        print(f"{a} + {b} = {result}", file = f)