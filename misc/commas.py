

def comma_placement():
    words = [
        "red",
        "blue",
        "green" # <- missing comma
        "yellow"]

    # above is legit, will print ['red', 'blue', 'greenyellow']

    # to avoid, just add comma after all items

    words = [
        "red",
        "blue",
        "green",
        "yellow", # last item has comma but legit syntax
        ]

    # words =
