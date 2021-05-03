from random import *
from PIL import Image


coloss = Image.open(r'img\coloss_titan.jpg')
bron = Image.open(r'img\bron_titan.jpg')
attack = Image.open(r'img\attacked_titan.jpg')
female = Image.open(r'img\female_titan.jpg')
iron = Image.open(r'img\iron_titan.jpg')
small = Image.open(r'img\small_titan.jpg')
animal = Image.open(r'img\animal_titan.jpg')
car = Image.open(r'img\car_titan.jpg')
main = Image.open(r'img\main_titan.png')


TITANS = {'Колоссальный Титан':coloss, 'Бронированный Титан': bron, 'Атакующий Титан':attack, 
          'Титан Женская особь':female, 'Титан Молот войны':iron, 'Титан Челюсти':small,
          'Звероподобный Титан':animal, 'Титан Грузоперевозчик':car,
          'Титан Прародитель':main}

rand_titan = choice(list(TITANS.keys()))
print(f'Поздравляю вы {rand_titan}!')
test = TITANS.get(rand_titan)
test.show()