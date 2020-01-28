import unittest


def classify_triangle(sides):
    if min(sides) <= 0:
        return False
    if sum(sorted(sides)[:-1]) < sorted(sides)[-1]:
        return False
    return True


def equilateral(sides):
    triangle = classify_triangle(sides)
    if triangle:
        x, y, z = sides
        return x == y == z
    else:
        return False


def isosceles(sides):
    triangle = classify_triangle(sides)
    if triangle:
        x, y, z = sides
        return x == y or y == z or z == x
    else:
        return False


def scalene(sides):
    if equilateral(sides) or isosceles(sides):
        return False
    return classify_triangle(sides)


def right_angled(sides):
    triangle = classify_triangle(sides)
    if triangle:
        a, b, c = sides
        return (a * a + b * b == c * c) or (c * c + b * b == a * a) or (a * a + c * c == b * b)
    else:
        return False


class TestEquilateralTriangle(unittest.TestCase):
    def test_all_sides_are_equal(self):
        self.assertIs(equilateral([2, 2, 2]), True)

    def test_all_zero_sides_is_not_a_triangle(self):
        self.assertIs(equilateral([0, 0, 0]), False)

    def test_third_triangle_inequality_violation(self):
        self.assertIs(isosceles([3, 1, 1]), False)

    def test_sides_may_be_floats(self):
        self.assertIs(equilateral([0.5, 0.5, 0.5]), True)


class TestIsoscelesTriangle(unittest.TestCase):
    def test_last_two_sides_are_equal(self):
        self.assertIs(isosceles([3, 4, 4]), True)

    def test_equilateral_triangles_are_also_isosceles(self):
        self.assertIs(isosceles([4, 4, 4]), True)

    def test_third_triangle_inequality_violation(self):
        self.assertIs(isosceles([3, 1, 1]), False)

    def test_sides_may_be_floats(self):
        self.assertIs(isosceles([0.5, 0.4, 0.5]), True)


class TestScaleneTriangle(unittest.TestCase):
    def test_no_sides_are_equal(self):
        self.assertIs(scalene([5, 4, 6]), True)

    def test_all_sides_are_equal(self):
        self.assertIs(scalene([4, 4, 4]), False)

    def test_third_triangle_inequality_violation(self):
        self.assertIs(isosceles([3, 1, 1]), False)


class TestRightAngleTriangle(unittest.TestCase):
    def test_no_sides_are_equal(self):
        self.assertIs(right_angled([3, 4, 5]), True)

    def test_all_sides_are_equal(self):
        self.assertIs(right_angled([4, 4, 4]), False)

    def test_third_triangle_inequality_violation(self):
        self.assertIs(right_angled([3, 1, 1]), False)


if __name__ == "__main__":
    unittest.main()
