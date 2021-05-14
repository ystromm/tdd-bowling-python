from unittest import TestCase

from assertpy import assert_that

import Bowling


class ExampleTests(TestCase):
    def test_1_plus_1_should_return_2(self):
        assert_that(1+1).is_equal_to(2)

    def test_1_plus_1_should_be_close_to_2(self):
        assert_that(1.1+1).is_close_to(2, 0.1)

    def test_a_plus_bc_should_not_be_empty(self):
        assert_that("a"+"bcd").is_not_empty().contains("a").contains("bc")
