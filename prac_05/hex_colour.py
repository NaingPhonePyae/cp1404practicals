NAME_TO_CODE = {"absolutezero": "#0048ba",
                "acidgreen": "#b0bf1a",
                "aliceblue": "#f0f8ff",
                "alizarincrimson": "#e32636",
                "amaranth": "#e52b50",
                "amber": "#ffbf00",
                "amethyst": "#9966cc",
                "antiquewhite": "#faebd7",
                "antiquewhite1": "#ffefdb",
                "antiquewhite2": "#eedfcc"}

print(NAME_TO_CODE)
colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        print(colour_name.title(), "colour code is", NAME_TO_CODE[colour_name])
    except KeyError:
        print("Invalid short state")
    colour_name = input("Enter colour name: ").lower()
