from copy import deepcopy

matches = int(input())
line = input().split()

fighters = [int(x) for x in line]

fightersCopy = deepcopy(fighters)


def calculateFighterScore(fighter):
    fighterIndex = fighters.index(fighter)
    remainingFighters = len(fighters)

    score = fighter

    if (fighterIndex+1) < remainingFighters:
        multipliers = [fighters[fighterIndex+1]]
        # score = fighter * fighters[fighterIndex+1]

        if (fighterIndex-1) >= 0:
            # score = score + fighters[fighterIndex-1]
            multipliers.append(fighters[fighterIndex-1])
        else:
            multipliers.append(0)

        multipliers.sort()
        score = fighter * multipliers[-1] + multipliers[0]

    else:
        score = fighter

    return score


def maximizeScore():
    score = 0
    fights = deepcopy(matches)

    while fights > 0:
        tempScores: list['int'] = list(map(calculateFighterScore, fighters))
        stageMaxScore = max(tempScores)
        score = score + stageMaxScore
        stageMaxScoreIndex = tempScores.index(stageMaxScore)
        fighters.remove(fighters[stageMaxScoreIndex])
        fights = fights - 1

    return score


print(maximizeScore())
