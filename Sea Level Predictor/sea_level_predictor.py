import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data', color='blue')

    # Line of best fit (all data)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], slope * df['Year'] + intercept, 'r', label='Fit Line')

    # Line of best fit (from year 2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    plt.plot(df_recent['Year'], slope_recent * df_recent['Year'] + intercept_recent, 'g', label='Fit Line (2000 onwards)')

    # Extend lines to year 2050
    plt.plot([df['Year'].min(), 2050], [slope * df['Year'].min() + intercept, slope * 2050 + intercept], 'r--')
    plt.plot([df_recent['Year'].min(), 2050], [slope_recent * df_recent['Year'].min() + intercept_recent, slope_recent * 2050 + intercept_recent], 'g--')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot
    plt.savefig('sea_level_plot.png')
    plt.show()
