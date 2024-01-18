import pandas as pd

canton_populations = {'Zürich': 1_579_967,  # NOSONAR
                      'Bern': 1_051_437,
                      'Waadt': 830_431,
                      'Aargau': 711_232,
                      'St. Gallen': 525_967}  # NOSONAR
canton_areas = {'Zürich': 1728.94,
                'Bern': 5958.50,
                'Waadt': 3212.02,
                'Aargau': 1403.80,
                'St. Gallen': 2028.20}


def main():
    my_series = pd.Series((35, 59, 49, 76, 23))
    print(my_series)
    print(my_series.index)
    print(my_series.values)
    print(my_series[1])
    print()

    my_series = pd.Series((35, 59, 49, 76, 23), index=('a', 'b', 'c', 'd', 'e'))
    print(my_series)
    print(my_series['c'])
    print()

    population_series = pd.Series(canton_populations)
    print(population_series)
    print(population_series.index)
    print(population_series['Aargau'])
    print(population_series['Bern':"St. Gallen"])

    print('-' * 100)

    area_series = pd.Series(canton_areas)
    canton_dataframe = pd.DataFrame({'population': population_series, 'area': area_series})
    print(canton_dataframe)
    print()

    print(canton_dataframe.at['Aargau', 'area'])
    print(canton_dataframe.iat[3, 1])
    print()

    print(canton_dataframe.loc['Zürich':'Bern', 'population'])  # wenn mit Name angesprochen, ist die Obergrenze (to) beim sclicing inklusive
    print(canton_dataframe.iloc[0:2, 0])   # to is excluded
    print()

    canton_dataframe['densitiy'] = canton_dataframe['population'] / canton_dataframe['area']
    print(canton_dataframe)
    print()
    print(canton_dataframe.densitiy < 500)
    print(canton_dataframe['densitiy'] < 500)
    print()
    print(canton_dataframe.loc[canton_dataframe['densitiy'] < 500])
    print(canton_dataframe[canton_dataframe['densitiy'] < 500])


if __name__ == '__main__':
    main()
