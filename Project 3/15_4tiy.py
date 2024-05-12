# -*- coding: utf-8 -*-
"""15.4TIY.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zBok2ut5Xkqixw0NFG3zWqPxXye6CgHh
"""

from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        while len(self.x_values) < self.num_points:

            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])

            next_x = self.x_values[-1] + (x_direction * x_distance)
            next_y = self.y_values[-1] + (y_direction * y_distance)

            self.x_values.append(next_x)
            self.y_values.append(next_y)