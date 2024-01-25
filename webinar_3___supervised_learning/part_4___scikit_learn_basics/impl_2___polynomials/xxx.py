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
    scatter_x_2d = rng.random((SCATTER_N, 1)) ** 2
    scatter_y = 10 - 1. / (scatter_x_2d.ravel() + 0.1)  # + rng.random(SCATTER_N)
    # print(scatter_y)

    # Split scattered data into training and test data.
    x_training_2d, x_test_2d, y_training, y_test = train_test_split(scatter_x_2d, scatter_y, test_size=0.2)
    ax.scatter(x_training_2d.ravel(), y_training, color='blue', label='training data')
    ax.scatter(x_test_2d.ravel(), y_test, color='red', label='test data')

    # background: functionality of PolynomialFeatures
    # linear_data = np.arange(1, 5 + 1).reshape(-1, 1)
    # print(linear_data)
    # print()
    # polynomial_features = PolynomialFeatures(3)
    # polynomial_data = polynomial_features.fit_transform(linear_data)
    # print(polynomial_data)

    # Create ideal x data.
    ideal_x_2d = np.linspace(-0.1, 1.1, IDEAL_N).reshape((-1, 1))

    # Train, predict, and plot polyonomials of several degrees.

    for degree in PLOT_DEGREES:
        pipeline = make_pipeline(PolynomialFeatures(degree), LinearRegression())
        pipeline.fit(x_training_2d, y_training)
        y_prediction = pipeline.predict(ideal_x_2d)
        ax.plot(ideal_x_2d.ravel(), y_prediction, alpha=0.5, label=f'degree = {degree}')

    # Finish first plot.
    ax.legend()
    fig.show()  # or plt.show()

    # validation curve
    training_score, validation_score = validation_curve(
        make_pipeline(PolynomialFeatures(degree=1), LinearRegression()),
        scatter_x_2d,
        scatter_y,
        param_name='polynomialfeatures__degree',
        param_range=SEARCH_DEGREES,
        cv=5,
        scoring='neg_mean_squared_error')

    fig, ax = plt.subplots(dpi=300, layout='constrained')
    ax.set_ylim(-1.1, 0.1)
    ax.plot(SEARCH_DEGREES, np.mean(training_score, axis=1), c='blue', label='training score')
    ax.plot(SEARCH_DEGREES, np.mean(validation_score, axis=1), c='red', label='validation score')
    ax.legend()
    fig.show()  # or
    # plt.show()

    # grid search
    parameter_grid = {'polynomialfeatures__degree': SEARCH_DEGREES}
    grid_search = GridSearchCV(make_pipeline(PolynomialFeatures(degree=1), LinearRegression()), parameter_grid, cv=5,
                               # scoring='neg_mean_absolute_error', # n_jobs=-1, # verbose=2
                               )
    grid_search.fit(scatter_x_2d, scatter_y)
    print(grid_search.fit(scatter_x_2d, scatter_y))
    print(grid_search.best_params_)


if __name__ == '__main__':
    main()
