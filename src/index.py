import numpy
import matplotlib


def generate_newton_polynomial(features, degree):
    pass


def generate_polynomial_features(features, degree):
    result = numpy.array()

    for i in range(0, degree):
        newton_polynomial = generate_newton_polynomial(features, i)
        numpy.append(result, newton_polynomial)

    return result


def main():
    data = numpy.load("./lib/data.npz")

    x1 = data["x1"]
    x2 = data["x2"]
    y = data["y"]

    x1_test = data["x1_test"]
    x2_test = data["x2_test"]
    y_test = data["y_test"]

    print(list(data.keys()))
