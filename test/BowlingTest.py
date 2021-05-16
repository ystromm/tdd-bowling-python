from unittest import TestCase

from assertpy import assert_that

import Bowling


class ExampleTests(TestCase):
    def test_1_plus_1_should_return_2(self):
        assert_that(1 + 1).is_equal_to(2)

    def test_1_plus_1_should_be_close_to_2(self):
        assert_that(1.1 + 1).is_close_to(2, 0.1)

    def test_a_plus_bc_should_not_be_empty(self):
        assert_that("a" + "bcd").is_not_empty().contains("a").contains("bc")


class BowlingScoreTests(TestCase):

    def test_game_with_only_misses_should_be_0(self):
        assert_that(Bowling.score("0" * 20)).is_zero()

    def test_score_with_roll_knocking_down_1_pin_should_be_1(self):
        assert_that(Bowling.score("1" + "0" * 19)).is_equal_to(1)

    def test_score_with_all_rolls_knocking_down_1_pin_should_be_20(self):
        assert_that(Bowling.score("1"*20)).is_equal_to(20)

    def test_score_with_rolls_knocking_down_diffent_pins_should_be_45(self):
        assert_that(Bowling.score("0123456789"+"0"*10)).is_equal_to(45)

    def test_score_with_strike_in_first_frame_should_be_10(self):
        assert_that(Bowling.score("X"+"0"*18)).is_equal_to(10)

    def test_score_with_one_and_spare_in_first_frame_should_be_10(self):
        assert_that(Bowling.score("1/"+"0"*18)).is_equal_to(10)

    def test_score_with_two_and_spare_in_first_frame_should_be_10(self):
        assert_that(Bowling.score("2/"+"0"*18)).is_equal_to(10)

    def test_score_spare_should_get_bonus_from_next(self):
        assert_that(Bowling.score("2/1"+"0"*17)).is_equal_to(12)

    def test_score_strike_should_get_bonus_from_the_two_following(self):
        assert_that(Bowling.score("X12"+"0"*16)).is_equal_to(16)

    def test_two_strikes_in_a_row_should_get_bonus_from_the_two_following(self):
        assert_that(Bowling.score("XX"+"0"*12)).is_equal_to(30)
