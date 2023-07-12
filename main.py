import os

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letter_lists = {letter: [] for letter in letters}

for letter in letters:
    folderdir = "letters/" + letter
    for image in os.listdir(folderdir):
        if image.endswith(".png"):
            letter_lists[letter].append(image)
