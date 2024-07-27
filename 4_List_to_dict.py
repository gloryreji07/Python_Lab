ListColour = ["Black", "Red", "Maroon", "Yellow"]
ColorCodes = ["000000", "FF0000", "800000", "FFFF00"]

color_dict_list = [{"Color": color, "ColorCode": color_code} for color, color_code in zip(ListColour, ColorCodes)]

print(color_dict_list)
