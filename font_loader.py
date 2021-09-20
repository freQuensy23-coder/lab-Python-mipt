import json


def load(font_name):
    with open(font_name, "r") as f:
        return eval(f.read())