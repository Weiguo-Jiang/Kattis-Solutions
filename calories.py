inputs = []
while True:
    try:
        inputs.append(input().split())
    except EOFError:
        break
inputs.pop()

total_calories = 0
total_fat_calories = 0
for i in range(len(inputs)):
    inp = inputs[i]
    if inp[0] == '-':
        print(str(round(total_fat_calories / total_calories * 100)) + '%')
        total_calories = 0
        total_fat_calories = 0
        continue

    cur_calories = 0
    cur_percent = 0
    fat_calories = 0
    fat_percent = 0
    fat, protein, sugar, starch, alcohol = inp
    if fat[-1] == 'g':
        cur_calories += int(fat[:-1]) * 9
        fat_calories += int(fat[:-1]) * 9
    elif fat[-1] == 'C':
        cur_calories += int(fat[:-1])
        fat_calories += int(fat[:-1])
    else:
        cur_percent += int(fat[:-1])
        fat_percent += int(fat[:-1])

    if protein[-1] == 'g':
        cur_calories += int(protein[:-1]) * 4
    elif protein[-1] == 'C':
        cur_calories += int(protein[:-1])
    else:
        cur_percent += int(protein[:-1])

    if sugar[-1] == 'g':
        cur_calories += int(sugar[:-1]) * 4
    elif sugar[-1] == 'C':
        cur_calories += int(sugar[:-1])
    else:
        cur_percent += int(sugar[:-1])

    if starch[-1] == 'g':
        cur_calories += int(starch[:-1]) * 4
    elif starch[-1] == 'C':
        cur_calories += int(starch[:-1])
    else:
        cur_percent += int(starch[:-1])

    if alcohol[-1] == 'g':
        cur_calories += int(alcohol[:-1]) * 7
    elif alcohol[-1] == 'C':
        cur_calories += int(alcohol[:-1])
    else:
        cur_percent += int(alcohol[:-1])

    if cur_percent != 0:
        cur_calories /= (100 - cur_percent) / 100

    total_calories += cur_calories
    total_fat_calories += (fat_percent * cur_calories / 100 + fat_calories)