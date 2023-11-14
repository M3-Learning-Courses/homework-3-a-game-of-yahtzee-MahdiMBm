import sys
import os
root_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_directory)

import unittest
from src.my_yahtzee_project.dice import YahtzeeDice


class TestYahtzeeDice(unittest.TestCase):

    def test_post_init_with_initial_matrix(self):
        yahtzee_set = YahtzeeDice(initial_matrix=[3, 6, None, None, 1])
        self.assertEqual(len(yahtzee_set.dice_set), 5)
        self.assertEqual(yahtzee_set.num_dice, 5)
        self.assertEqual(yahtzee_set.dice_set[2].current_value, None)

    def test_roll_all_with_initial_matrix(self):
        yahtzee_set = YahtzeeDice(initial_matrix=[3, 6, None, None, 1])
        rolled_values = yahtzee_set.roll_all()
        self.assertEqual(len(rolled_values), 5)
        for i, value in enumerate(rolled_values):
            if i in [0, 1, 4]:
                self.assertEqual(value, yahtzee_set.dice_set[i].current_value)
            else:
                self.assertIn(value, range(1, yahtzee_set.sides + 1))

    def test_roll_all_without_initial_matrix(self):
        yahtzee_set = YahtzeeDice()
        rolled_values = yahtzee_set.roll_all()
        self.assertEqual(len(rolled_values), 5)
        for value in rolled_values:
            self.assertIn(value, range(1, yahtzee_set.sides + 1))

    def test_get_values_after_rolling(self):
        yahtzee_set = YahtzeeDice(initial_matrix=[3, 6, None, None, 1])
        yahtzee_set.roll_all()
        values = yahtzee_set.get_values()
        self.assertEqual(len(values), 5)
        for i, value in enumerate(values):
            if i in [0, 1, 4]:
                self.assertEqual(value, yahtzee_set.dice_set[i].current_value)
            else:
                self.assertIn(value, range(1, yahtzee_set.sides + 1))

if __name__ == '__main__':
    unittest.main()