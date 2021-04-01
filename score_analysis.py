def name_score_group_creator(names, scores):
    name_score = []
    group = []
    i = 0
    while i < len(names):
        name_score.append(names[i])
        name_score.append(scores[i])
        group.append(tuple(name_score))
        name_score.remove(names[i])
        name_score.remove(scores[i])
        i = i + 1
    return group


def sorting_score_board(group):
    length = len(group)
    for i in range(length):
        for j in range(length - i - 1):
            if group[j][1] < group[j + 1][1]:
                temp = group[j]
                group[j] = group[j + 1]
                group[j + 1] = temp
    return group


def winner_declare(group):
    sorted_group = sorting_score_board(group)
    winner_names = []
    max_score = sorted_group[0][1]
    i = 0
    while i < len(sorted_group) and max_score != 0:
        if max_score == sorted_group[i][1]:
            winner_names.append(sorted_group[i][0])
        i = i + 1
    if len(winner_names) != 0:
        if len(winner_names) == 1:
            print(f'WINNER\n--------------\n{winner_names[0].upper()}')
        else:
            if len(winner_names) == len(group):
                print('ALL HAVE EQUAL SCORES')
            else:
                print('WINNERS')
                print('-------------')
                for x in winner_names:
                    print(x.upper())
    else:
        print('NO WINNERS')