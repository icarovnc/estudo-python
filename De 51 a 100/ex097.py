def print_linh(msg):
    t = len(msg) + 5
    print('_' * t)
    print(f'{msg:^{t}}')
    print('_' * t)


print_linh('Não sei de nada')