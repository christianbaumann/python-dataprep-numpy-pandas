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

    # TODO


if __name__ == '__main__':
    main()
