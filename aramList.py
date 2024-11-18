import random


# Function to read lines from a file and store them in a list
def read_file_to_list(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines() if line.strip()]


# Function to generate two random lists with unique elements
def generate_random_lists(source_list, size=15):
    random.shuffle(source_list)  # Shuffle the original list
    return source_list[:size], source_list[size:size * 2]


# Run the main function
if __name__ == "__main__":
    filename = 'heros.txt'

    # Read lines from the file
    source_list = read_file_to_list(filename)

    # Generate two random lists
    list1, list2 = generate_random_lists(source_list)
    print("Team 1:")
    for e in list1:
        print(e)
    print("\nTeam 2:")
    for e in list2:
        print(e)
