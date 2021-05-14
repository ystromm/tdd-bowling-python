from unittest import TestCase

from assertpy import assert_that

import Bowling


class BowlingScoreTests(TestCase):

    def test_score_should_be_0_when_starting(self):
        assert_that(Bowling.score([])).is_zero()