with open("All_Currencies.csv", "r") as file:
    volumes_2016 = []
    volumes_2017 = []
    for i, line in enumerate(file):
        if i == 0:
            continue
        #print(line)
        for j, word in enumerate(line.split(",")):
            if j == 1:
                year = word.split("/")[0]
                if int(word.split("/")[-1]) == 2016:
                    volumes_2016.append(int(line.split(",")[7]))
                if  int(word.split("/")[-1]) == 2017:
                    volumes_2017.append(int(line.split(",")[7]))
        if i > 15000:
            break
    volumes_2016.sort()
    volumes_2017.sort()
    print(volumes_2016)
    print(volumes_2017)
    print(volumes_2016[int(len(volumes_2016) / 2)])
    print(volumes_2017[int(len(volumes_2017) / 2)])