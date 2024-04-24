import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score


def polynomial_regression():
    """
    If the graph is more curvy, the relationship between the data points is stronger. and if the graph is less curvy,
    the relationship between the data points is weaker.
    """
    x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
    y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]
    # why 3? because the data points are not linear, and the data points are not quadratic, but cubic
    mymodel = np.poly1d(np.polyfit(x, y, 3))
    # 1 to 22, 100 points
    myline = np.linspace(1, 22, 100)
    plt.scatter(x, y)
    plt.plot(myline, mymodel(myline))
    plt.show()


def r_squared():
    """
    the closer to 1, the better the relationship, the closer to 0, the worse the relationship
    """
    x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
    y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]
    mymodel = np.poly1d(np.polyfit(x, y, 3))

    print(r2_score(y, mymodel(x)))


def predict():
    x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
    y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]
    mymodel = np.poly1d(np.polyfit(x, y, 3))
    speed = mymodel(17)
    print(speed)


def bad_fit():
    x = [89, 43, 36, 36, 95, 10, 66, 34, 38, 20, 26, 29, 48, 64, 6, 5, 36, 66, 72, 40]
    y = [21, 46, 3, 35, 67, 95, 53, 72, 58, 10, 26, 34, 90, 33, 38, 20, 56, 2, 47, 15]

    mymodel = np.poly1d(np.polyfit(x, y, 3))
    myline = np.linspace(2, 95, 100)

    print(r2_score(y, mymodel(x)))
    plt.scatter(x, y)
    plt.plot(myline, mymodel(myline))
    plt.show()


if __name__ == "__main__":
    # polynomial_regression()
    # r_squared()
    # predict()
    bad_fit()
