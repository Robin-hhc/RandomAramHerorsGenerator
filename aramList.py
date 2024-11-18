import random


def generator(filename, size=15):
    # Open the file with heroes
    file = open(filename, 'r', encoding='utf-8')
    source_list = [line.strip() for line in file.readlines() if line.strip()]

    # Shuffle the original list
    random.shuffle(source_list)

    # Form the list into str result
    res = "Team 1:\n"
    for e in source_list[:size]:
        res += e + "\n"
    res += "\nTeam 2:"
    for e in source_list[size:size * 2]:
        res += e + "\n"
    return res


# Run the main function
if __name__ == "__main__":
    filename = 'heroes.txt'
    print(generator(filename))
