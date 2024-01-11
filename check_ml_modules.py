# Version 2024.01

import platform
import seaborn  # Hover --> Install package seaborn --> Wait until packages and skeletons updated successfully
import sklearn  # Hover --> Install package scikit-learn --> Wait until packages and skeletons updated successfully
import tensorflow  # Hover --> Install package tensorflow --> Wait until packages and skeletons updated successfully


def main():
    print(f'Python: {platform.python_version()}')  # 3.11.7 or 3.10.12
    print(f'seaborn: {seaborn.__version__}')  # 0.13.1 or 0.12.2
    print(f'scikit-learn: {sklearn.__version__}')  # 1.3.2
    print(f'TensorFlow: {tensorflow.__version__}')  # 2.15.0


if __name__ == '__main__':
    main()

# https://link.simplexacode.ch/fn39

