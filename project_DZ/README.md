# Проект 1. Домашнее задание. Игра: Угадай число

## Оглавление 
[1. Описание проекта](https://github.com/SvetlanaLis/sf_data_scince/tree/main/project_DZ#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)

[2. Какой кейс решаем?](https://github.com/SvetlanaLis/sf_data_scince/tree/main/project_DZ#2-%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)

[3. Этапы работы над проектом](https://github.com/SvetlanaLis/sf_data_scince/tree/main/project_DZ#3-%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)

[4. Результат](https://github.com/SvetlanaLis/sf_data_scince/tree/main/project_DZ#4-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82)


### 1. Описание проекта
Угадать загаданное компьютером число за минимальное число попыток

:arrow_up:[к оглавлению](https://github.com/SvetlanaLis/sf_data_scince/tree/main/project_DZ#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 2. Какой кейс решаем?
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**
- Компьютер загадывает целое число от 0 до 100, а нам его нужно угадать. Под "угадать" подразумевается "написать" программу, которая угадывает число
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам
- Необходимо добиться того, чтобы программа угадывала число меньше, чем за 20 попыток.

**Метрика качества**
Результаты оцениваются по среднему количеству попыток при 1000 повторений. Необходимо добиться минимального количества попыток.

**Что практикуем**
- Учимся писать хороший код на Python
- Учимся работать с IDE
- Учимся работать с GitHub

:arrow_up:[к оглавлению](https://github.com/SvetlanaLis/sf_data_scince/tree/main/project_DZ#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 3. Этапы работы над проектом
Этап 1.
Подход 1: Случайное угадывание
Простейший способ решения: научить программу случайным образом выбирать число до тех пор, пока оно не будет угадано. Этот способ не дает хорошего результата, однако будет для нас хорошей стартовой точкой.

Этап 2.
Подход 2: Угадывание с коррекцией
Сначала устанавливаем любое случайное число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.

Этап 3.
Пишем функцию для оценки. Эта функция необходима, чтобы определить, за какое число попыток программа угадывает наше число. Определяем, какой подход лучше, и получаем, что две предложенные программы показывают не лучший результат.

Этап 4.
Подход 3: Новое решение
Пишем функцию, которая принимает на вход загаданное число и возвращает число попыток угадывания - меньше 20.

:arrow_up:[к оглавлению](https://github.com/SvetlanaLis/sf_data_scince/tree/main/project_DZ#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 4. Результат
- Была написана программа, которая угадывает число за минимальное число попыток. 
- Выполнены все условия соревнования. 
- Метрика качества соответствует заданным условиям.
- На практики использованы указанные навики.

:arrow_up:[к оглавлению](https://github.com/SvetlanaLis/sf_data_scince/tree/main/project_DZ#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)




