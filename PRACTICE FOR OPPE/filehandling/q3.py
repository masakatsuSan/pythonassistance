with open("spy.txt","r") as file:
    content = file.readlines()
    for lines in content :
        res = ""
        part = lines.split("|")
        word = part[0]
        idx = part[1]
        indeces = idx.split(",")
        for num in indeces:
            pos = int(num)-1
            res = res + word[pos]
        print(res)
