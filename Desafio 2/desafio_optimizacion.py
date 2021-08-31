import itertools
import pandas as pd

def get_min_distance(combination):

    previous_day = combination[0]
    distance_list = []
    for day in combination:

        if day == previous_day:
            continue

        distance = abs(day - previous_day)
        distance_list.append(distance)
        previous_day = day
    
    min_distance = min(distance_list)
    
    return min_distance

def get_days_distribution(days, nm_days, minimum_distance):

    days_combinations = list(itertools.combinations(days, nm_days))
    df_days_combinations = pd.DataFrame([[x] for x in days_combinations], columns=["days_combinations"])

    df_days_combinations = df_days_combinations.assign(min_distance=lambda x: x.days_combinations.apply(lambda value: get_min_distance(value)))

    return df_days_combinations.loc[lambda x: x.min_distance >= minimum_distance]

if __name__ == "__main__":
    import time

    start_time = time.time()
    days = [x for x in range(1,41)]
    nm_days = 7
    minimum_distance = 3

    df_valid_combinations = get_days_distribution(days, nm_days, minimum_distance)
    valid_combination = df_valid_combinations.days_combinations.values[0]
    print(f"Valid combination: {valid_combination}")
    print(f"Total time: {round(time.time() - start_time, 2)} seconds")