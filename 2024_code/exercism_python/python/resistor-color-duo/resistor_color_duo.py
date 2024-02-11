    
def value(colors):
    code_colors = [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white"
        ]
    return int("".join([str(code_colors.index(color)) for color in colors[:2]]))
        
