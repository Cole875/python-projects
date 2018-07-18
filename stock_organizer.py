with open("All_Currencies.csv", "r") as file:
    all_highs = 0.0
    high_count = 0
    for i, line in enumerate(file):
        if i == 0:
            continue
        #print(line)
        for j, word in enumerate(line.split(",")):
            if j == 1:
                month_year = word.split("/")[-1] + word.split("/")[0]
                with open ('%s.csv' %month_year, 'a') as new_file:
                    new_file.write(line)
                if int(word.split("/")[-1]) == 2017 and int(word.split("/")[0]) >= 5 or int(word.split("/")[-1]) == 2018 and int(word.split("/")[0]) < 6:
                    print(float(line.split(",")[4]))
                    all_highs += float(line.split(",")[4])
                    high_count += 1

        if i > 10000:
            print(all_highs)
            print(high_count)
            print(all_highs / high_count)
            break
    print(all_highs / high_count)

