from unittest import TestCase
import area

class TestShapeAreas(TestCase): # if you do not include TestCase, 0 tests will run

    # methods MUST start with the word 'test'

    def test_triangle_area(self):
        # A triangle with height 4 and base 5 should have area 10
        self.assertEqual(10, area.triangle_area(4,5))

    def test_triangle_area_floating_point(self):
        self.assertAlmostEqual(17.79875, area.triangle_area(7.25, 4.91))
        # if you used assertEqual instead of assertAlmostEqual, you would encounter an error
        # due to how Python rounds floating numbers

    def test_negative_base_height_raises_value_error(self):
        with self.assertRaises(ValueError): # prints out the ValueError message from area.py
            area.triangle_area(-3, 0)

    def test_base_height_zero(self): # testing edge cases
        self.assertEqual(0, area.triangle_area(0, 4))
        self.assertEqual(0, area.triangle_area(4, 0))
        self.assertEqual(0, area.triangle_area(0, 0))

    
