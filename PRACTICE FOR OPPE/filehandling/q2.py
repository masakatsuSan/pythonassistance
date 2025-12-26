filename = "somu.txt"
with open(filename,"r") as file:
    content = file.read()
    lines = content.split("\n")
    inputline = lines[-1]
    songs = lines[:-1]
    input = inputline.split("-") #['2','3','1']
    order = [int(x)-1 for x in input] # 0-index ['1','2','0']
    for i in order :
        print(songs[i])

# Shape of You
# Dance Monkey
# Blinding Lights