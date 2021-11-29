import numpy as np
import matplotlib.pyplot as plt


def generate_newton_polynomial(features, degree):
    pass


def generate_polynomial_features(features, degree):
    result = np.array()

    for i in range(0, degree):
        newton_polynomial = generate_newton_polynomial(features, i)
        np.append(result, newton_polynomial)

    return result


def main():
    data = np.load("./lib/data.npz")

    fig = plt.figure()
    ax = plt.axes(projection="3d")
    plt.show()

    x1 = data["x1"]
    x2 = data["x2"]
    y = data["y"]

    x1_test = data["x1_test"]
    x2_test = data["x2_test"]
    y_test = data["y_test"]

    print(list(data.keys()))
