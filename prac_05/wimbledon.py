"""
Wimbledon Champions Data Processing
Estimate: 30 minutes
Actual: 40 minutes
"""


def read_wimbledon_data(filename):
    """Reads the Wimbledon champions data from a CSV file."""
    champions_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            # Assuming the CSV format is: Champion, Country, Wins
            parts = line.strip().split(',')
            champions_data.append(parts)
    return champions_data


def count_champions(champions_data):
    """Counts the number of wins for each champion and returns a dictionary."""
    champion_counts = {}
    for champion, country, wins in champions_data:
        wins = int(wins)  # Convert wins to an integer
        if champion in champion_counts:
            champion_counts[champion] += wins
        else:
            champion_counts[champion] = wins
    return champion_counts


def get_countries(champions_data):
    """Returns a set of unique countries from the champions data."""
    countries = {country for _, country, _ in champions_data}
    return countries


def main():
    filename = 'wimbledon.csv'

    # Step 1: Read the data from the CSV file
    champions_data = read_wimbledon_data(filename)

    # Step 2: Count the champions and their wins
    champion_counts = count_champions(champions_data)

    # Step 3: Get the unique countries
    countries = get_countries(champions_data)

    # Output the champions and their win counts
    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_counts.items()):
        print(f"{champion} {wins}")

    # Output the countries in alphabetical order
    print("\nThese countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


# Call the main function to run the program
if __name__ == "__main__":
    main()
