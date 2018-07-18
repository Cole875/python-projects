jungle_map = {}
with open("Tarzan.txt", "r") as file:
    for line in file:
        for word in line.split(" "):
            if word.lower() in jungle_map:
                jungle_map[word.lower()] += 1
            else:
                jungle_map[word.lower()] = 1
for key in sorted(jungle_map.keys()):
    print(key, " ", jungle_map[key])