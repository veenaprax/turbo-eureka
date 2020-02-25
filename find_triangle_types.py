'''
This program is for different types of triangles
'''
import unittest

# Check if right number of parameters
def classify_triangle(sides):
    """Test to classify triangles"""
    if min(sides) <= 0 or sum(sorted(sides)[:-1]) < sorted(sides)[-1] \
            or len(sides) > 3 or len(sides) < 3:
        return False
    return True

# Check if all sides are equal
def equilateral(sides):
    """Test to classify triangles"""
    triangle = classify_triangle(sides)
    if triangle:
        x_1, y_1, z_1 = sides
        return x_1 == y_1 == z_1
    return False

# Check if 2 sides are equal
def isosceles(sides):
    """Test to classify triangles"""
    triangle = classify_triangle(sides)
    if triangle:
        x_1, y_1, z_1 = sides
        return x_1 == y_1 or y_1 == z_1 or z_1 == x_1
    return False

# Check if all sides are different
def scalene(sides):
    """Test to classify triangles"""
    if equilateral(sides) or isosceles(sides):
        return False
    return classify_triangle(sides)


# Check if 3 sides equal to a2 + b2 = c2
def right_angled(sides):
    """Test to classify triangles"""
    triangle = classify_triangle(sides)
    if triangle:
        a_1, b_1, c_1 = sides
        #Return the right angled triangle results
        return (a_1 * a_1 + b_1 * b_1 == c_1 * c_1) or \
               (c_1 * c_1 + b_1 * b_1 == a_1 * a_1) or \
               (a_1 * a_1 + c_1 * c_1 == b_1 * b_1)
    return False

# Test to check if parameters are correct
class TestIsATriangle(unittest.TestCase):
    """Test if its a triangle. Input different values"""
    def test_all_parameters(self):
        """Test with all parameters. Input different values"""
        self.assertIs(classify_triangle([2, 2, 2, 4]), False)
    def test_less_parameters(self):
        """Test with less parameters. Input different values"""
        self.assertIs(classify_triangle([2, 1]), False)
    def test_right_parameters(self):
        """Test with correct parameters. Input different values"""
        self.assertIs(classify_triangle([2, 2, 3]), True)
    def test_float_parameters(self):
        """Test with float parameters. Input different values"""
        self.assertIs(classify_triangle([0.5, 2, 3]), False)
    def test_zero_parameters(self):
        """ def test_zero_parameters(self):"""
        self.assertIs(classify_triangle([0, 0, 0]), False)

# Test with different parameters. Input different values
class TestEquilateralTriangle(unittest.TestCase):
    """Test for Equilateral Triangle. Input different values"""
    def test_all_sides_are_equal(self):
        """Test if all sides are equal"""
        self.assertIs(equilateral([2, 2, 2]), True)

    def test_all_zero_sides_is_not_a_triangle(self):
        """Test if zero parameters are working"""
        self.assertIs(equilateral([0, 0, 0]), False)

    def test_third_triangle_inequality_violation(self):
        """Test if all sides are not equal"""
        self.assertIs(isosceles([3, 1, 1]), False)

    def test_sides_may_be_floats(self):
        """Test if all sides have floating values"""
        self.assertIs(equilateral([0.5, 0.5, 0.5]), True)


class TestIsoscelesTriangle(unittest.TestCase):
    """Test with different parameters for Isosceles. Input different values"""
    def test_last_two_sides_are_equal(self):
        """Test if two sides are equal"""
        self.assertIs(isosceles([3, 4, 4]), True)

    def test_equilateral_triangles_are_also_isosceles(self):
        """Test if equilateral triangles are also isosceles"""
        self.assertIs(isosceles([4, 4, 4]), True)

    def test_third_triangle_inequality_violation(self):
        """Test if triangle inequality violation"""
        self.assertIs(isosceles([3, 1, 1]), False)

    def test_sides_may_be_floats(self):
        """Test if triangle inputs are floating numbers"""
        self.assertIs(isosceles([0.5, 0.4, 0.5]), True)


class TestScaleneTriangle(unittest.TestCase):
    """Test with different parameters for Scalene. Input different values"""
    def test_no_sides_are_equal(self):
        """Test if No triangle sides are equal"""
        self.assertIs(scalene([5, 4, 6]), True)

    def test_all_sides_are_equal(self):
        """if triangle all sides are equal"""
        self.assertIs(scalene([4, 4, 4]), False)

    def test_third_triangle_inequality_violation(self):
        """Test if triangle inequality violation"""
        self.assertIs(isosceles([3, 1, 1]), False)


class TestRightAngleTriangle(unittest.TestCase):
    """Test with different parameters for Right angled. Input different values"""
    def test_no_sides_are_equal(self):
        """Test if No triangle sides are equal"""
        self.assertIs(right_angled([3, 4, 5]), True)

    def test_all_sides_are_equal(self):
        """if triangle all sides are equal"""
        self.assertIs(right_angled([4, 4, 4]), False)

    def test_third_triangle_inequality_violation(self):
        """Test if triangle inequality violation"""
        self.assertIs(right_angled([3, 1, 1]), False)



if __name__ == "__main__":
    unittest.main()
