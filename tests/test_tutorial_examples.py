from fractions import Fraction as F
import unittest


def matvec(matrix, vector):
    return [sum(a * x for a, x in zip(row, vector)) for row in matrix]


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


class TutorialExampleTests(unittest.TestCase):
    def test_changed_span_covers_every_target(self):
        matrix = [[1, 2], [2, 3]]
        for p, q in [(3, 5), (1, 0), (-2, 7), (0, 0)]:
            self.assertEqual(matvec(matrix, [2 * q - 3 * p, 2 * p - q]),
                             [p, q])
        for a, b in [(0, 1), (3, 0), (-2, 4)]:
            output = matvec([[1, 2], [2, 4]], [a, b])
            self.assertEqual(output[1], 2 * output[0])

    def test_nonorthogonal_projection_double_counts(self):
        first, second = [1, 1, 0], [1, 0, 1]
        extra = [F(dot(second, first), dot(second, second)) * x
                 for x in second]
        naive = [a + b for a, b in zip(first, extra)]
        self.assertNotEqual(naive, first)
        remainder = [b - F(dot(first, second), dot(first, first)) * a
                     for a, b in zip(first, second)]
        self.assertEqual(remainder, [F(1, 2), -F(1, 2), 1])
        self.assertEqual(dot(first, remainder), 0)

    def test_svd_directions_follow_sum_and_difference(self):
        # A=M/sqrt(2), unit directions=w/sqrt(2), so Av=Mw/2.
        matrix = [[2, 2], [-1, 1]]
        for direction, expected in [([1, 1], [2, 0]), ([-1, 1], [0, 1])]:
            output = [F(x, 2) for x in matvec(matrix, direction)]
            self.assertEqual(output, expected)
        self.assertEqual(dot([1, 1], [-1, 1]), 0)

    def test_row_swap_examples(self):
        self.assertEqual(matvec([[0, 1, 1], [1, 1, 0], [2, 1, 1]],
                                [1, 2, 3]), [5, 3, 7])
        self.assertEqual(matvec([[0, 1, 1], [1, -1, 0], [2, 1, -1]],
                                [2, 1, 3]), [4, 1, 2])

    def test_two_free_variables(self):
        matrix = [[0, 1, 2, 1], [1, 2, 3, 1], [2, 5, 8, 3]]
        n1, n2 = [1, -2, 1, 0], [1, -1, 0, 1]
        for direction in [n1, n2]:
            self.assertEqual(matvec(matrix, direction), [0, 0, 0])
        for s, t in [(0, 0), (1, -1), (-2, 3)]:
            candidate = [1 + s + t, 2 - 2 * s - t, s, t]
            self.assertEqual(matvec(matrix, candidate), [2, 5, 12])
        self.assertEqual(matvec(matrix, [1, 0, 0, 0]), [0, 1, 2])

    def test_four_spaces_use_different_null_directions(self):
        matrix = [[1, 1, 0], [0, 1, 1], [1, 2, 1]]
        input_null, output_null = [1, -1, 1], [-1, -1, 1]
        self.assertEqual(matvec(matrix, input_null), [0, 0, 0])
        for column in zip(*matrix):
            self.assertEqual(dot(column, output_null), 0)
        self.assertEqual(dot(output_null, [2, 3, 5]), 0)
        self.assertEqual(dot(output_null, [2, 3, 6]), 1)
        self.assertNotEqual(dot(input_null, [2, 3, 5]), 0)

    def test_plane_projection_and_pythagoras(self):
        target = [2, 3, 6]
        basis = [[1, 0, 1], [-1, 2, 1]]
        projected = [sum(F(dot(q, target), dot(q, q)) * q[i]
                         for q in basis) for i in range(3)]
        self.assertEqual(projected, [F(7, 3), F(10, 3), F(17, 3)])
        residual = [a - b for a, b in zip(target, projected)]
        self.assertEqual(dot(residual, residual), F(1, 3))
        for q in basis:
            self.assertEqual(dot(q, residual), 0)
        extra = [a - b for a, b in zip(projected, [2, 3, 5])]
        self.assertEqual(dot(residual, residual) + dot(extra, extra), 1)

    def test_exact_house_fit(self):
        matrix = [[80, 1], [100, 2], [90, F(1, 2)]]
        prices = [150, 180, 180]
        fitted = matvec(matrix, [F(951, 460), -F(315, 23)])
        residual = [a - b for a, b in zip(prices, fitted)]
        self.assertEqual(residual, [-F(39, 23), F(15, 23), F(18, 23)])
        for column in zip(*matrix):
            self.assertEqual(dot(column, residual), 0)

    def test_rank_deficient_shortest_coefficients(self):
        matrix = [[1, 2], [2, 4], [0, 0]]
        shortest = [F(3, 25), F(6, 25)]
        self.assertEqual(matvec(matrix, shortest), [F(3, 5), F(6, 5), 0])
        self.assertEqual(dot(shortest, [-2, 1]), 0)
        self.assertEqual(dot(shortest, shortest), F(9, 125))
        for t in [F(0), F(1, 5), F(-1)]:
            candidate = [F(3, 5) - 2 * t, t]
            self.assertEqual(dot(candidate, candidate),
                             5 * (t - F(6, 25)) ** 2 + F(9, 125))

    def test_centering_changes_the_principal_direction(self):
        data = [[10, 2], [10, -2], [12, 2], [12, -2]]
        means = [F(sum(column), len(data)) for column in zip(*data)]
        self.assertEqual(means, [11, 0])
        centered = [[x - mean for x, mean in zip(row, means)] for row in data]
        centered_columns = list(zip(*centered))
        raw_columns = list(zip(*data))
        self.assertEqual([dot(c, c) for c in centered_columns], [4, 16])
        self.assertEqual(dot(*centered_columns), 0)
        self.assertEqual([dot(c, c) for c in raw_columns], [488, 16])
        self.assertEqual(F(16, 4 + 16), F(4, 5))


if __name__ == '__main__':
    unittest.main()
