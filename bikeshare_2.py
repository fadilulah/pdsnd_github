import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months_included =['january','february','march','april','may','june','all']

days_of_week  = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
               city = input('Enter the name of the city you want to get information about: ')
               city = city.lower()
               if city in CITY_DATA:
                     break
               else:
                     print('You have entered an invalid city, try again')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
              month_tocheck = input('Enter a month from january to june or enter \'all\' to get all months available: ')
              month = month_tocheck.lower()
              if month in months_included:
                break
              else:
                print('You cannot filter by this month ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_inweek = input('Enter a the day you wan to filter by (monday through sunday) or enter \'all\' to get all days available: ')
        day = day_inweek.lower()
        if day in days_of_week:
            break
        else:
            print('You have entered an invalid day please try again ')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.day_name()
    df['month'] = df['Start Time'].dt.month   
    df['hour'] = df['Start Time'].dt.hour                 
    if month != 'all':
        month = months_included.index(month) + 1
        df = df[df['month'] == month] 
                
    if day != 'all':
        df = df[df['day'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is :', common_month)
    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print('The most common day is :', common_day)
    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour is :', common_hour)
                     
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0] 
    print('The most common start station is :', common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station is :', common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    common_start_stopstation = df['Start Station'] + df['End Station']
    common_start_stop_station =common_start_stopstation.mode()[0]
    print('The most frequent combination of start station and end station trip is : ',common_start_stop_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time_travelled = df['Trip Duration'].sum(axis = 0)
    print('The total travel time is : ',total_time_travelled)
    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('the total travel time is : ',average_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('The user type count information is : ',user_types_count)
    # TO DO: Display counts of gender
    try:
        gender_type_count = df['Gender'].value_counts()
        print(f'The gender count information is : {gender_type_count}')
    except: print('The the gender info column does not exist in this city file')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        common_birth_year = df['Birth Year'].mode()[0]
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        print(f'The most common birth year is {common_birth_year} and the most recent year is {most_recent_birth_year}'
              f' \n while the most earliest birth year is {earliest_birth_year}')
    except: print('The Birth Year column does not exist in this city file') 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_raw_data(df):
    display_count = 5
    while True:
        display_data = input("Do you want to see the raw data? (yes/no): ").strip().lower()
        if display_data == "yes":
            print(df.head(display_count))

            while True:
                more_data = input("Do you want to see more data? (yes/no): ").strip().lower()
                if more_data == "yes":
                    try:
                        num_of_data = int(input("How many more would you like to see? "))
                        display_count += num_of_data
                        if display_count <= len(df):
                            print(df.head(display_count))
                        else:
                            print("You have reached the end of the data or entered a value larger than the data length.")
                    except ValueError:
                        print("Please enter a valid number.")
                else:
                    break
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        get_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
