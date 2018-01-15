TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)

def tileprint(arg1):
    for i in arg1:
        if i == "||":
            print("\n")
        else:
            print(i, end="")

tileprint(TILES)