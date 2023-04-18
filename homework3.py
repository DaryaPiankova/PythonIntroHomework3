PointsForLetters = {'АВЕНОРСТAEIOULNSTR': 1, 'ДКЛМПУDG': 2,
                    'БГЁЬЯBCMP': 3, 'ЙЫFHVWY': 4, 'ЖЗХЦЧK': 5, 'ШЭЮJX': 8, 'ФЩЪQZ': 10}

word = input('введите слово: ')

pointsCounter = 0
for i in word:
    for j in PointsForLetters.keys():
        if i in j:
            pointsCounter += PointsForLetters.get(j)

print(pointsCounter)
