def value(colors):
    number = 10*color_code(colors[0])
    number += color_code(colors[1])
    return number

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