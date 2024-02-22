"""
Hunter McMahon
CIS 210
p8.py
desc: data data data! its fun
"""

# imports
import random
import math
import csv
import matplotlib.pyplot as plt


# 8.1
# todo: check to see if solution allowed
def load_numerical_data(filename: str, column_titles: list) -> dict:
    """Load data from a CSV file and return a dictionary with keys being the
    row number and values as tuples of the data in each row, converted to float.

    Args:
        filename: The name of the CSV file to load.
        column_titles: A list of columns to load.

    Returns:
        A dictionary where each element corresponds to a data point, with keys 
        corresponding to the row number and values as a tuple of floats.

    Example:
        If column_titles = ['Col1', 'Col3'], and the CSV file has the following data:
            Col1, Col2, Col3
             2.4,  5.6,  7.8
            10.0, 42.5, -3.2
            31.4,  0.5, 12.3
        Then the return dictionary will be:
            {0: (2.4, 7.8), 1: (10, -3.2), 2: (31.4, 12.3)}
    """
    imported_data = {}
    data_lines = []
    with open(str(filename), 'r', encoding="utf-8", newline='') as input_data:
        raw_extract_data = csv.reader(input_data)
        for line in raw_extract_data:
            data_lines.append(line)
        col1_index = data_lines[0].index(column_titles[0])
        col2_index = data_lines[0].index(column_titles[1])
        for i in range(1, len(data_lines)):
            imported_data[i - 1] = (float(data_lines[i][col1_index]), float(data_lines[i][col2_index]))
            print(imported_data)
    return imported_data


# 8.2
# todo: look into refactoring
def euclid_dist(point1: tuple, point2: tuple) -> float:
    """Compute the Eucledian distance between two points represented as tuples.
    Listing 7.1 in PPC, with modifications for compliance to PEP8

    Args:
        point1: A tuple representing a point in n-dimensional space.
        point2: A tuple representing a point in n-dimensional space.

    Returns:
        float: The Euclidean distance between the two points.

    Example:
        >>> euclid_dist((1, 2.5), (2.1, 4))
        1.8601075237738274
    """
    total = 0
    for i in range(len(point1)):
        diff = (point1[i] - point2[i]) ** 2
        total += diff
    euclid_distance = math.sqrt(total)
    return euclid_distance


# 8.3
# todo: check to refactor
def create_centroids(k: int, data: dict) -> list:
    """Create k centroids by picking random points from the data until 
    you have k unique centroids.

    Args:
        k: The number of centroids to create.
        data: A dictionary where each element corresponds to a data point, with keys
            corresponding to the row number and values as tuples of floats.

    Returns:
        list: a list of centroids, each centroid is a tuple of floats.
    """
    centroids = []
    num_o_centroids = 0
    key_o_centroid = []
    while num_o_centroids < k:
        rkey = random.randint(1, len(data))
        if rkey not in key_o_centroid:
            centroids.append(data[rkey])
            key_o_centroid.append(rkey)
            num_o_centroids += 1
    return centroids


# 8.4
# todo: implement solution
def create_clusters(k: int, centroids: list, data: dict, repeats=100) -> list:
    """Create clusters using the k-means algorithm
    From Listing 7.8, modified to comply with PEP8
    Args:
        k:
        centroids:
        data: list of tuples
        repeats:

    Returns:
        dict: a list of clusters
    """
    for i in range(repeats):
        print('****PASS', i + 1, "****")
        clustas = []
        for x in range(k):
            clustas.append([])
        for key in data:
            distances = []
            for dex in range(k):
                d_table_o_contents = euclid_dist(data[key], centroids[dex])
                distances.append(d_table_o_contents)
            mindist = min(distances)
            index = distances.index(mindist)
            clustas[index].append(key)
        dimensions = len(data[1])
        for dex in range(k):
            sums = [0] * dimensions
            for key in clustas[dex]:
                data_points = data[key]
                for ind in range(len(data_points)):
                    sums[ind] += data_points[ind]
            for ind in range(len(sums)):
                cluster_len = len(clustas[dex])
                if cluster_len != 0:
                    sums[ind] /= cluster_len
            centroids[dex] = sums
        for c in clustas:
            print("CLUSTER")
            for key in c:
                print(data[key], end=" ")
            print()
    return clustas, centroids


# 8.5
# todo: implement solution
def visualize_clusters(dataset_name: str, titles: list, clusters: list,
                       centroids: list) -> plt.Figure:
    """OPTIONAL - Extra credit (up to 50xp)
    Visualize the clusters and centroids. Use a different color for each cluster. 
    Args: 
        dataset_name: The name of the dataset
        titles: list of string column titles
        clusters: list of lists of tuples
        centroids: list of tuples
    Returns:
        matplotlib.pyplot.Figure: The figure object
    """
    pass


def main():
    """ Main driver for the program."""

    # Specifies the files and columns to analyze in the keys, and the number
    # of clusters in the values.
    datasets = {('earthquakes-proj8', ('latitude', 'longitude')): 5,
                ('earthquakes-proj8', ('depth', 'mag')): 5,
                ('cis210-scores', ('Projects', 'Exams')): 5}
    # Feel free to add more datasets or column pairs and experiment with different values of k

    # Compute clusters for all datasets
    for (dataset, titles), k in datasets.items():
        print(f'\nDataset: {dataset} {titles}')
        # Part 8.1
        data = load_numerical_data(dataset + '.csv', column_titles=titles)

        # Part 8.3
        centroids = create_centroids(k, data)
        print("Initialized the centroids.")

        # Parts 8.2 and 8.4 (create_clusters calls euclid_dist)
        clusters, centroids = create_clusters(k, centroids, data)
        print("\nCreated the clusters.")

        # Optional extra-credit 8.5
        visualize_clusters(dataset, titles, clusters, centroids)
        print("Visualized the clusters.")


if __name__ == '__main__':
    main()
