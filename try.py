yt_list = ["Pewdipie", "Wallibear", "Markiplier", "MrsOki", "MrBeats", "Belle Deplhine", "KSI", "Vikkstar123", "Manny",
           "Zerkaa", "Pokimane"]

x = input("Enter your first string")
y = input("Enter your second string")
z = input("Enter your third string")

x = x[0]
y = y[0]
z = z[0]
i = 0

for i in range(len(yt_list)):
    if x in yt_list[i] and y in yt_list[i] and z in yt_list[i]:
        print(yt_list[i])


