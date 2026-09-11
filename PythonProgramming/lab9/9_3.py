import random
from random import randint

treasure_map = [
[1, 2],
[3, 5],
[5, 6],
[7, 8]
]
coor2 = randint(1,8)
coor3 = randint(1,8)
print("Количество сокровищ:")
print(len(treasure_map))
print("Координаты сокровищ:")
for i in treasure_map:
    print(*i)
print("Координаты Александра")
print(coor2, coor3)

min_distance_squared = float('inf')
nearest_treasure = None
for treasure in treasure_map:
    distance_squared = (treasure[0] - coor2) ** 2 + (treasure[1] - coor3) ** 2

    if distance_squared < min_distance_squared:
        min_distance_squared = distance_squared
        nearest_treasure = treasure
print("Ближайшее сокровище")
print(*nearest_treasure)