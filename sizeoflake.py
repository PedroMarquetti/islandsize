from unittest.util import sorted_list_difference
import numpy as np


class Graph:
    """
    self.ROW >>> row length
    self.COL >>> col length
    self.graph >>> curr. matrix
    Modified from 'https://www.geeksforgeeks.org/find-number-of-islands/' and 'https://www.geeksforgeeks.org/find-length-largest-region-boolean-matrix/'
    """

    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g

    def is_safe(self, row_item, col_item, visited) -> bool:
        """
        A function to check if a given cell (row, col) can be included in DFS
        """

        return (
            row_item >= 0 and row_item < self.ROW and  # check
            col_item >= 0 and col_item < self.COL and  # boundaries
            not visited[row_item][col_item]  # check if item has been visited
            and self.graph[row_item][col_item]
        )

    def DFS(self, row_item: int, column_item: int, visited: bool, island_size):
        """Recursive func. that searches neighbours of all '1' items found """

        row_neighbour = [-1, -1, -1, 0, 0, 1, 1, 1]  # setting
        col_neighbour = [-1, 0, 1, -1, 1, -1, 0, 1]  # boundaries

        # set current item visited to True
        visited[row_item][column_item] = True

        for index in range(8):
            # for each item around the current '1'
            if self.is_safe(row_item + row_neighbour[index], column_item + col_neighbour[index], visited):
                island_size[0] += 1  # add +1 to the current island total size
                self.DFS(  # run recursive func
                    row_item + row_neighbour[index],
                    column_item + col_neighbour[index],
                    visited, island_size
                )

    def count_islands(self) -> tuple:
        """
        Main func

        Returns tuple with number of islands and their sizes
        """
        visited = [
            [False for col_item in range(self.COL)]for row_item in range(self.ROW)
        ]

        count = 0  # Initial number of islands
        islands = []  # Empty list of islands (and their sizes)

        for row_item in range(self.ROW):
            for column_item in range(self.COL):
                # for each item in graph
                if not visited[row_item][column_item] and self.graph[row_item][column_item] == 1:
                    island_size = [1]  # adding 1 to curr. island size
                    # Passing current item to recursive DFS func,
                    # DFS func. will add to current island size
                    self.DFS(row_item, column_item, visited, island_size)
                    islands.append(island_size[0])

                    # After running recursively, will add to number of islands
                    count += 1

        return count, islands


if __name__ == '__main__':
    random_matrix = np.random.randint(0, 2, (640, 13))
    g = Graph(len(random_matrix), len(random_matrix[0]), random_matrix)
    number_of_islands = g.count_islands()[0]
    sizes = g.count_islands()[1]
    sorted_sizes = sizes
    sorted_sizes.sort(reverse=True)
    print(f"Number of islands is: {number_of_islands}")
    print(f"Island sizes: {sizes}")
    print(f"Sorted Island sizes: {sorted_sizes}")
