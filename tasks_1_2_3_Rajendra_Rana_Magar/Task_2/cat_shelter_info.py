import sys


def format_time(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60

    if hours == 0:
        return f"{remaining_minutes:02d} mins"
    else:
        return f"{hours:02d} hrs : {remaining_minutes:02d} mins"


def analyze_cat_shelter(log_filename):
    try:
        with open(log_filename, 'r') as file:
            lines = file.readlines()

        visits_my_cat = 0
        visits_intruder_cats = 0
        total_time_in_house = 0
        visit_durations = []

        for line in lines:
            if line.strip() == 'END':
                break

            data = line.strip().split(',')
            cat_type, entry_time, exit_time = data

            entry_time = int(entry_time)
            exit_time = int(exit_time)

            duration = exit_time - entry_time

            if cat_type == 'OURS':
                visits_my_cat += 1
                total_time_in_house += duration
                visit_durations.append(duration)
            elif cat_type == 'THEIRS':
                visits_intruder_cats += 1

        if visits_my_cat > 0:
            average_duration = sum(visit_durations) // visits_my_cat
            longest_duration = max(visit_durations)
            shortest_duration = min(visit_durations)
        else:
            average_duration = longest_duration = shortest_duration = 0

        print("\n==================\nLog File Analysis\n==================")
        print(f"Total Visits of My Cat: {visits_my_cat}")
        print(f"Total Visits of Intruder Cats: {visits_intruder_cats}")
        print(f"\n=========================\nShelter Info About My Cat\n=========================")
        print(f"Total Time in Shelter: {format_time(total_time_in_house)}")
        print(f"\nAverage Visit Length: {format_time(average_duration)}")
        print(f"Longest Visit: {format_time(longest_duration)}")
        print(f"Shortest Visit: {format_time(shortest_duration)}")

    except FileNotFoundError:
        print(f'Cannot open "{log_filename}"!')
    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing command line argument!")
    else:
        input_log_filename = sys.argv[1]
        analyze_cat_shelter(input_log_filename)
