import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_circles, make_moons
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC, SVC


def main():
    # Create samples.
    pass  # TODO

    # Create samples.
    # features, targets = make_blobs(n_samples=100, centers=2, cluster_std=1.0)
    # features, targets = make_circles(n_samples=100, noise=0.1, factor=0.1)
    features, targets = make_moons(n_samples=1000, noise=0.2)

    # scaled support vector classifier
    # scaled_svc = make_pipeline(StandardScaler(), LinearSVC(C=1_000_000, dual='auto'))
    # scaled_svc = make_pipeline(StandardScaler(), SVC(kernel='rbf', C=100_000))
    scaled_svc = make_pipeline(StandardScaler(), SVC(kernel='poly', C=10_000, degree=3, coef0=1))
    scaled_svc.fit(features, targets)

    # visualization
    fig, ax = plt.subplots(dpi=300, layout='constrained')
    ax.scatter(features[:, 0], features[:, 1], c=targets)
    x_limits = ax.get_xlim()
    y_limits = ax.get_ylim()
    grid_x, grid_y = np.meshgrid(np.linspace(x_limits[0], x_limits[1], num=100 + 1),
                                 np.linspace(y_limits[0], y_limits[1], num=100 + 1))
    all_x_y_pairs = np.array((grid_x, grid_y)).T.reshape(-1, 2, order='F')
    decision_function_values = scaled_svc.decision_function(all_x_y_pairs).reshape(grid_x.shape)
    ax.contour(grid_x, grid_y, decision_function_values, levels=[0], colors='gray')
    fig.show()  # or plt.show()


if __name__ == '__main__':
    main()
