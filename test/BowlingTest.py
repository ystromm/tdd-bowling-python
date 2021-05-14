from unittest import TestCase

from assertpy import assert_that

import Bowling


class BowlingScoreTests(TestCase):

    def test_score_should_be_0_when_starting(self):
        assert_that(Bowling.score([])).is_zero()

    def test_score_with_roll_knocking_down_1_pin_should_be_1(self):
        assert_that(Bowling.score([1])).is_equal_to(1)