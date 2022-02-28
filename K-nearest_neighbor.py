import numpy as np
import matplotlib.pyplot as plt


def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]
    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
    return arr

class KNearestNeighbor:
    def __init__(self, x, x_point, K):
        self.k = K
        self.x = x
        self.x_point = x_point

    def compute_Euclidean_distances(self):
        lis = []
        mini_coordinate = []
        for i in range(0, 10):
            for j in range(0, 1):
                distances = np.sqrt(np.power((self.x[i][j] - self.x_point[j]), 2) + np.power((self.x[i][j+1] - self.x_point[j + 1]), 2))
                lis.append(distances)
        return lis

    # def swap_2d(self, arr1, arr2):
    #     arr1, arr2 = arr2, arr1
    #     return arr1, arr2


    def seeking_the_mini_coordinates(self):
        mini_coordinate = []
        lis_mini = []
        tmp = []
        mindist = self.compute_Euclidean_distances()[0]
        for i in range(0, 9):
            if(self.compute_Euclidean_distances()[i] > self.compute_Euclidean_distances())[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
                mini_coordinate = x[i]
                lis_mini.append(mini_coordinate)
        result = []
        for c in range(0, self.k):
            result.append(lis_mini[c])
        return result

    def finding_nearest_distances(self):
        nearest_distances = []
        nearest_distances = self.compute_Euclidean_distances()[0]
        for i in range(0, 9):
            if self.compute_Euclidean_distances()[i] < nearest_distances:
                nearest_distances = self.compute_Euclidean_distances()[i]
        return nearest_distances


if __name__ == "__main__":
    x0 = np.random.randint(50, size=(10, 2))
    x1 = np.random.randint(50, size=(10, 2))
    x = np.append(x0, x1)
    x = x.reshape(20, 2)
    # x_point = np.random.randint(50, size=(10, 2))
    x_point = [int(input(f'Input the {i+1} number: ')) for i in range(0, 2)]
    K = int(input('Input K: '))
    # KNN_0 = KNearestNeighbor(x0, x_point, K)
    # minimal_distances_0 = KNN_0.finding_nearest_distances()
    # KNN_1 = KNearestNeighbor(x1, x_point, K)
    # minimal_distances_1 = KNN_1.finding_nearest_distances()
    # result = min(minimal_distances_0, minimal_distances_1)
    KNN = KNearestNeighbor(x, x_point, K)
    minimal_distances = KNN.compute_Euclidean_distances()
    print(f"All of the distances is {minimal_distances}")
    result = bubble_sort(minimal_distances)
    new_list = []
    for i in range(0, K):
        new_list.append(result[i])
    print('The {} nearest distances are {}'.format(K, new_list))
    mini_coordinate = KNN.seeking_the_mini_coordinates()
    print(f"The minimal coordinates are {mini_coordinate}")
    for i in range(0, 9):
        for j in range(0, 1):
            plt.plot(x0[i][j], x0[i][j + 1], 'g^')
            plt.plot(x1[i][j], x1[i][j + 1], 'bD')
    # for i in range(0, 1):
    #     for j in range(0, K-1):
    #         plt.plot(mini_coordinate[i][j], mini_coordinate[i][j + 1], 'g^')
    plt.plot(x_point[:1], x_point[1:], 'ro', label='New data point')
    plt.title("K Nearest Neighbor")
    plt.xlabel("Horizontal axis")
    plt.ylabel("Vertical axis")
    plt.legend(loc='best')
    plt.show()
