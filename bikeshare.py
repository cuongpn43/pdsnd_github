import time
import pandas as pd
import numpy as np
<<<<<<< HEAD
import date
""" Project3 github """
=======
"""Project 03 - 4h40PM 02 August 2023 """
>>>>>>> refactoring
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)
<<<<<<< HEAD
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
       

    
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df
=======
    
>>>>>>> documentation

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
     #Add new column months extract month from Start Time 
    df['month'] = df['Start Time'].dt.month
    # Add new column day_of_week extract day from Start Time
    df['day_of_week'] =pd.to_datetime(df['Start Time']).dt.day_name()
    # Add new column hour extract day from Start Time
    df['hour'] = df['Start Time'].dt.hour

    return df
def time_stats(df):
     """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    print("The most common start station is: ", df ['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print("The most common end station is: ", df['End Station'].value_counts().idxmax())
    
    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip")
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def line_data(df):
    start = 0
    end  = 5
    df_line= len(df.index)
    while start < df_line:
        line_data = input("\nWould you like to see data? Enter 'yes' or 'no'.\n")
        if line_data.lower() == 'yes':
            print("\nDisplaying only 5 line of data.\n")
            if end > df_line:
                end = df_line
            print(df.iloc[start:end])
            start += 5
            end += 5
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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
