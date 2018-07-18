with open("All_Currencies.csv", "r") as file:
    for i, line in enumerate(file):
        if i == 0:
            continue
        #print(line)
        for j, word in enumerate(line.split(",")):
            if j == 1:
                month_year = word.split("/")[-1] + word.split("/")[0]
                with open ('%s.csv' %month_year, 'a') as new_file:
                    new_file.write(line)
            if i > 10000:
                break
