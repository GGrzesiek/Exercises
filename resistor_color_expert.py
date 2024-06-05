def resistor_label(colors):
    ohms = "ohms"
    if len(colors)== 1:
        return "0 ohms"
    elif len(colors)== 4:
        number = 10*color_code(colors[0])
        number += color_code(colors[1])
        expo = pow(10,color_code(colors[2]))
        tol = resistor_tolerance(colors[3])
    elif len(colors)== 5:
        number = 100*color_code(colors[0])
        number += 10*color_code(colors[1])
        number = color_code(colors[2])
        expo = pow(10,color_code(colors[3]))
        tol = resistor_tolerance(colors[4])
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
    label = f"{number} {ohms} ±{tol}"
    return label
    
    
def color_code(color):
    return colors().index(color)

def resistor_tolerance(color):
    res_tol = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%"
    }
    return res_tol[color]

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
