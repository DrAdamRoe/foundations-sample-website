import json

# This file should contain a function called get_color_code().
# This function should take one argument, a color name,
# and it should return one argument, the hex code of the color,
# if that color exists in our data. If it does not exist, you should
# raise and handle an error that helps both you as a developer,
# for example by logging the request and error, and the user,
# letting them know that their color doesn't exist.


def get_color_code(color_name):
    # this is where you should add your logic to check the color.
    # Open the file at data/css-color-names.json, and return the hex code
    # The file can be considered as JSON format, or as a Python dictionary.
    """ Opens the json file and load it to a Python dict """
    with open('/Users/lennartstachowiak/SE/foundations/foundations-sample-website/color_check/data/css-color-names.json') as f:
        color_list = json.load(f)

    if color_name in color_list:
        """ Checks if color in list and save it in hex_code """
        hex_code = color_list[color_name]
        return hex_code
    else:
        return None
