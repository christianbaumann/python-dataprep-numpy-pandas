import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import GaussianNB

# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

sns.set_theme(style='whitegrid', palette='colorblind')


def main():
    # iris dataset for classification
    iris_bunch = load_iris(as_frame=True)
    # print(iris_bunch)
    # print(type(iris_bunch))

    print()

    # feature matrix
    iris_x = iris_bunch.data
    # print(iris_x)
    # print(type(iris_x))  # pandas.core.frame.DataFrame

    print()

    # target vector
    iris_y = iris_bunch.target
    # print(iris_y)
    # print(type(iris_y))  # pandas.core.series.Series

    print()

    # target names
    species_names = iris_bunch.target_names
    # print(species_names)

    print()

    # target vector with species names
    iris_y = pd.Categorical.from_codes(iris_y, categories=species_names)
    # print(iris_y)

    print()

    # full dataframe
    iris_dataframe = iris_x.copy()
    iris_dataframe['species'] = iris_y
    # print(iris_dataframe)

    # pairplot
    sns.pairplot(iris_dataframe, hue='species', height=2.0)
    # fig = plt.gcf()
    # fig.set_dpi(300)
    # fig.show()

    print()

    # Split data into training and test data.
    x_training, x_test, y_training, y_test = train_test_split(iris_x, iris_y, test_size=0.2)  # 20% zufällige Prozent sollen "auf die Seite gelegt werden", die werden nicht zum trainieren verwendet.
    # x_training, x_test, y_training, y_test = train_test_split(iris_x, iris_y, test_size=0.2, random_state=4128)  # Random "einfrieren", immer gleich, Seed
    # print(x_training.shape, x_test.shape, y_training.shape, y_test.shape)
    # print()
    # print(x_training)
    # print()
    # print(y_training)
    # print()

    # Create and train model.
    model = GaussianNB()  # Gaussian naives Bayes
    model.fit(x_training, y_training)

    # Predict unknown/test data.
    y_prediction = model.predict(x_test)
    print(y_prediction)
    print()
    y_comparison = pd.DataFrame({'y_test': y_test, 'y_prediction': y_prediction})
    print(y_comparison)
    print()
    print(accuracy_score(y_test, y_prediction))


    print()

    # Show determined model attributes.
    print(model.feature_names_in_)
    print(model.classes_)
    print(model.theta_)  # mean
    print(model.var_)  # var

    print('-' * 100)

    # cross-validation
    model = GaussianNB()  # hier beginnt alles nochmal von vorne
    # scores = cross_val_score(model, iris_x, iris_y, cv=5)  # gleiches wie oben, in einer Zeile; teilt es in 5 Teile auf
    scores = cross_val_score(model, iris_x, iris_y, cv=5, n_jobs=-1, verbose=2)
    print(f'scores = {scores}')
    print(f'mean = {scores.mean()}')


if __name__ == '__main__':
    main()
