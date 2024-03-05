def read_input_file(input_file):
    shows_dict = {}
    with open(input_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(': ')
            num_seasons = int(parts[0])
            shows = parts[1].split('; ')
            shows_dict[num_seasons] = shows
    return shows_dict

def output_keys(output_file, data):
    with open(output_file, 'w') as file:
        for key, value in data.items():
            file.write(f"{key}: {'; '.join(value)}\n")


def output_titles(output_file, data):
    with open(output_file, 'w') as file:
        for key in sorted(data.keys()):
            shows = sorted(data[key])
            file.write(f"{key}: {'; '.join(shows)}\n")

def main():
    input_file = input()
    shows = read_input_file(input_file)

    output_keys('output_keys.txt', shows_dict)

    output_title('output_titles.txt', shows_dict)

if __name__ == '__main__':
    main()