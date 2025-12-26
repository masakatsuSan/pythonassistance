filename = "sampple.txt"
with open(filename,"r") as file :
    content = file.read()
    lines = content.split("\n")
    inputline = lines[-1]
    input = inputline.split(",") # ["2","4","3","1"]
    data = lines[:-1]
    order = [int(x)-1 for x in input] # 0 - index
    for i in order :
        print(data[i]) 

        
# Crack the eggs into a bowl.
# Whisk the mixture thoroughly.
# Heat the oil in the pan.
# Serve hot with garnish.