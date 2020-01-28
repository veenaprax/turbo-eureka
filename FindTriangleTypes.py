import unittest

# Check if right number of parameters
def classify_triangle(sides):
    if min(sides) <= 0 or sum(sorted(sides)[:-1]) < sorted(sides)[-1] or len(sides) > 3 or len(sides) < 3:
        return False
    else:
        return True

# Check if all sides are equal
def equilateral(sides):
    triangle = classify_triangle(sides)
    if triangle:
        x, y, z = sides
        return x == y == z
    else:
        return False

# Check if 2 sides are equal
def isosceles(sides):
    triangle = classify_triangle(sides)
    if triangle:
        x, y, z = sides
        return x == y or y == z or z == x
    else:
        return False

# Check if all sides are different
def scalene(sides):
    if equilateral(sides) or isosceles(sides):
        return False
    return classify_triangle(sides)


# Check if 3 sides equal to a2 + b2 = c2
def right_angled(sides):
    triangle = classify_triangle(sides)
    if triangle:
        a, b, c = sides
        return (a * a + b * b == c * c) or (c * c + b * b == a * a) or (a * a + c * c == b * b)
    else:
        return False

# Test to check if parameters are correct
class TestIsATriangle(unittest.TestCase):
    def test_all_parameters(self):
        self.assertIs(classify_triangle([2, 2, 2, 4]), False)

    def test_less_parameters(self):
        self.assertIs(classify_triangle([2, 1]), False)

    def test_right_parameters(self):
        self.assertIs(classify_triangle([2, 2, 3]), True)

    def test_float_parameters(self):
        self.assertIs(classify_triangle([0.5, 2, 3]), False)

    def test_zero_parameters(self):
        self.assertIs(classify_triangle([0, 0, 0]), False)

# Test with different parameters. Input different values
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
