f = input()
s = input()
t = input()

color = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7,
         'grey': 8, 'white': 9}

print((color[f]*10 + color[s])*10**color[t])