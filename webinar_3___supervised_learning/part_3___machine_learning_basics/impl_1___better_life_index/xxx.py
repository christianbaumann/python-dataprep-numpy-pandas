import numpy as np
import pandas as pnd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# constants
GDP = 'GDP per capita'
SATISFACTION = 'Life satisfaction'


def main():
    # Load data.
    oecd_bli = pnd.read_csv('oecd_bli_2015.csv', thousands=',')
    print(oecd_bli.head(10))
    print()
    gdp_per_capita = pnd.read_csv('gdp_per_capita.csv', thousands=',',
                                  delimiter='\t', encoding='latin1', na_values='n/a')
    print(gdp_per_capita.head(10))
    print()

    # Prepare data.
    country_stats, x, y = prepare_data(oecd_bli, gdp_per_capita)
    print(country_stats)
    print()

    # Select and train model.
    model = LinearRegression()
    model.fit(x, y)
    t0, t1 = model.intercept_[0], model.coef_[0][0]  # intercept: Achsenabschnitt, _: interne Variablen
    print(f't0 = {t0} | t1 = {t1}')

    # Predict for different GDP.
    x_new = [[22587]]  # Cyprus
    y_predicted = model.predict(x_new)
    print(f'y_predicted = {y_predicted}')

    # Visualize data.
    fig, ax = plt.subplots(dpi=300, layout='constrained')
    country_stats.plot(kind='scatter', x=GDP, y=SATISFACTION, color='b', ax=ax)
    x_linspace = np.linspace(0, 60000, 1000 + 1)
    ax.set_xlim((0, 60000))
    ax.set_ylim((0, 10))
    ax.plot(x_linspace, t0 + t1 * x_linspace, 'r')
    ax.plot(x_new, y_predicted, 'ro')
    fig.show()  # or plt.show()


def prepare_data(oecd_bli, gdp_per_capita):
    oecd_bli = oecd_bli[oecd_bli['INEQUALITY'] == 'TOT']
    oecd_bli = oecd_bli.pivot(index='Country', columns='Indicator', values='Value')
    gdp_per_capita.rename(columns={'2015': GDP}, inplace=True)
    gdp_per_capita.set_index('Country', inplace=True)
    full_country_stats = pnd.merge(left=oecd_bli, right=gdp_per_capita, left_index=True, right_index=True)
    full_country_stats.sort_values(by=GDP, inplace=True)
    remove_indices = [] #[0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(36)) - set(remove_indices))
    sample_country_stats = full_country_stats[[GDP, SATISFACTION]].iloc[keep_indices]
    x = np.c_[sample_country_stats[GDP]]
    y = np.c_[sample_country_stats[SATISFACTION]]
    return full_country_stats[[GDP, SATISFACTION]].iloc[keep_indices], x, y


if __name__ == '__main__':
    pnd.set_option("display.max_columns", None)
    pnd.set_option("display.width", 1000)
    sns.set_theme(style='whitegrid', palette='colorblind')
    main()
