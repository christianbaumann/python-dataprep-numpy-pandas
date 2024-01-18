import pandas as pd

canton_populations = {'Zürich': 1_579_967,
                      'Bern': 1_051_437,
                      'Waadt': 830_431,
                      'Aargau': 711_232,
                      'St. Gallen': 525_967}
canton_areas_1 = {'Graubünden': 7105.30,
                  'Bern': 5958.50,
                  'Wallis': 5224.64,
                  'Waadt': 3212.02,
                  'Tessin': 2812.15}
canton_areas_2 = {'Zürich': 1728.94,
                  'Bern': 5958.50,
                  'Waadt': 3212.02,
                  'Aargau': 1403.80,
                  'St. Gallen': 2028.20}


def main():
    population_series = pd.Series(canton_populations)
    print(population_series)
    print()

    area_series_1 = pd.Series(canton_areas_1, name='area_series_1')
    print(area_series_1)
    print()

    density_series = population_series / area_series_1
    print(density_series)
    print()
    print(density_series.isna())
    print(density_series.notna())
    print()
    print(density_series.loc[density_series.notna()])
    print()
    print(density_series.dropna())
    print()
    print(density_series.ffill())  # forward fill
    print()
    print(density_series.bfill())  # backward fill
    print()
    print(density_series.interpolate())
    print()

    print('-' * 100)

    area_series_2 = pd.Series(canton_areas_2, name='area_series_2')
    print(area_series_1)
    print(area_series_2)
    print()
    print(pd.concat((area_series_1, area_series_2)))
    print()
    # print(pd.concat((area_series_1, area_series_2), verify_integrity=True))  # schmeißt Fehler: ValueError: Indexes have overlapping values: Index(['Bern', 'Waadt'], dtype='object')
    # print()
    print(pd.concat((area_series_1, area_series_2), ignore_index=True))
    print()
    print(pd.concat((area_series_1, area_series_2), keys=['series 1', 'series 2']))
    print()

    print('-' * 100)

    print(pd.merge(area_series_1, area_series_2, how='inner', left_index=True, right_index=True))
    print()
    print(pd.merge(area_series_1, area_series_2, how='outer', left_index=True, right_index=True))
    print()
    print(pd.merge(area_series_1, area_series_2, how='outer', left_index=True, right_index=True)
          .ffill(axis='columns')
          .bfill(axis='columns')
          .loc[:, 'area_series_1']
          )
    print()


if __name__ == '__main__':
    main()
