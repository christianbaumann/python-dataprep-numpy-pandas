import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='whitegrid', palette='colorblind')


def main():
    fig = plt.figure(figsize=(12, 9), dpi=100, layout='constrained')
    gs = fig.add_gridspec(2, 2)
    ax_top = fig.add_subplot(gs[0, :])
    ax_bottom_left = fig.add_subplot(gs[1, 0])
    ax_bottom_right = fig.add_subplot(gs[1, 1])

    tips = sns.load_dataset('tips')
    print(tips)

    # sns.scatterplot(x="total_bill", y="tip", data=tips)

    print('-' * 100)

    # Wieviel % Trinkgeld wurde gegeben?
    tips['tip_percentage'] = tips['tip'] / tips['total_bill'] * 100
    print(tips)
    tips['tip_percentage'].plot.hist(bins=100, ax=ax_top, xlim=(0, 50))

    print('-' * 100)

    print(tips['sex'])
    print()
    print(tips['day'])
    print()
    print(tips['time'])
    print()

    print('-' * 100)

    party_counts = pd.crosstab(tips['day'], tips['size'])
    print(party_counts)
    print()
    party_counts_per_day = party_counts.sum(axis='columns')
    print(party_counts_per_day)
    print()
    party_counts_normalized = party_counts.div(party_counts_per_day,
                                               axis='rows')  # Normalisieren, Größen auf 1 runterbrechen
    print(party_counts_normalized)
    party_counts_normalized.plot.bar(stacked=True, ax=ax_bottom_left)

    print('-' * 100)

    # sns.barplot(data=tips, x='tip_percentage', y='day', ax=ax_bottom_right)
    # sns.barplot(data=tips, x='tip_percentage', y='day', hue='day', ax=ax_bottom_right)
    # sns.barplot(data=tips, x='tip_percentage', y='day', hue='sex', ax=ax_bottom_right)
    # sns.boxplot(data=tips, x='tip_percentage', y='day', hue='sex', ax=ax_bottom_right)
    # sns.boxplot(data=tips, x='tip_percentage', y='sex', hue='sex', ax=ax_bottom_right)
    sns.barplot(data=tips, x='tip_percentage', y='day', hue='size', errorbar=None, palette='flare', ax=ax_bottom_right)

    plt.show()


if __name__ == '__main__':
    main()
