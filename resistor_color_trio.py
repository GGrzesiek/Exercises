def label(colors):
    number = 10*color_code(colors[0])
    number += color_code(colors[1])
    ohms = "ohms"
    expo = pow(10,color_code(colors[2]))
    number *= expo
    if(1000000>number>1000):
        number //= 1000
        ohms = "kilo" + ohms
    elif(1000000000>number>1000000):
        number //= 1000000
        ohms = "mega" + ohms
    elif(number>1000000000):
        number //= 1000000000
        ohms = "giga" + ohms
    label = f"{number} {ohms}"
    return label
    
    
def color_code(color):
    return colors().index(color)

def colors():
    colors_list = ["black",
          "brown",
          "red",
          "orange",
          "yellow",
          "green",
          "blue",
          "violet",
          "grey",
          "white"]
    return colors_list
