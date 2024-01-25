import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, validation_curve, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

# constants
SCATTER_N = 50
IDEAL_N = 1000 + 1
PLOT_DEGREES = (1, 2, 5, 10)
SEARCH_DEGREES = np.arange(1, 20 + 1)

rng = np.random.default_rng()


def main():
    # Prepare first plot.
    fig, ax = plt.subplots(dpi=300, layout='constrained')
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-2, 12)
    ax.grid()

    # Create scattered x and y data.
    # TODO

    # Split scattered data into training and test data.
    # TODO

    # background: functionality of PolynomialFeatures
    # linear_data = np.arange(1, 5 + 1).reshape(-1, 1)
    # print(linear_data)
    # print()
    # polynomial_features = PolynomialFeatures(3)
    # polynomial_data = polynomial_features.fit_transform(linear_data)
    # print(polynomial_data)

    # Create ideal x data.
    # TODO

    # Train, predict, and plot polyonomials of several degrees.
    # TODO

    # Finish first plot.
    # ax.legend()
    # fig.show()  # or plt.show()

    # validation curve
    # TODO

    # fig, ax = plt.subplots(dpi=300, layout='constrained')
    # ax.set_ylim(-1.1, 0.1)
    # ax.plot(SEARCH_DEGREES, np.mean(training_score, axis=1), c='blue', label='training score')
    # ax.plot(SEARCH_DEGREES, np.mean(validation_score, axis=1), c='red', label='validation score')
    # ax.legend()
    # fig.show()  # or plt.show()

    # grid search
    # TODO


if __name__ == '__main__':
    main()
