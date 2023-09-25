"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np
# Объявим функцию, которая на вход будет принимать загаданное число 
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    max_number = 100
    min_number = 0    
    predict = np.random.randint(1, 101) 
    while True:
        count += 1
        if predict > number:
            max_number = predict-1
            predict = (max_number+min_number)//2
        elif predict< number:
            min_number = predict +1
            predict = (max_number+min_number)//2
        else:
            break
    return count
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
#RUN
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)





 
    



  

 