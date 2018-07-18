with open("All_Currencies.csv", "r") as file:

    volumes_2018 = []
    for i, line in enumerate(file):
        if i == 0:
            continue
        #print(line)
        for j, word in enumerate(line.split(",")):
            if j == 1:
                year = word.split("/")[0]
                if int(word.split("/")[-1]) == 2018:
                    volumes_2018.append(float(line.split(",")[6]))
        if i > 15000:
            break
    volumes_2018.sort()
    print(volumes_2018)
    print(volumes_2018[int(len(volumes_2018) / 2)])
    median = (int(len(volumes_2018)/2))
    sum1 = 0
    for k, num in enumerate(volumes_2018):
        if k >= median:
            break
        sum1 += num
    print(sum1/median)
    sum2 = 0
    for l, num in enumerate(volumes_2018):
        if l <= median:
            continue
        sum2 += num
    print(sum2/median)


