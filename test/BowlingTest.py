from unittest import TestCase
from assertpy import assert_that
import pytest
import Bowling


class SomeError(Exception):
    def __init__(self, message):
        self.message = message


def raises_some_error():
    raise SomeError("Everything is borken")


class ExampleTests(TestCase):
    def test_1_minus_1_should_return_0(self):
        self.assertEqual(0, 1 - 1)

    def test_abc_should_contain_b(self):
        self.assertIn("b", "abc")

    def test_1_plus_1_should_return_2(self):
        assert_that(1 + 1).is_equal_to(2)

    def test_1_plus_1_should_be_close_to_2(self):
        assert_that(1.1 + 1).is_close_to(2, 0.1)

    def test_a_plus_bc_should_not_be_empty(self):
        assert_that("a" + "bcd").is_not_empty().contains("a").contains("bc")

    def test_should_raise_an_error(self):
        try:
            raises_some_error()
            pytest.fail("Expected SomeError to be raised")
        except SomeError as e:
            self.assertIn("borken", e.message)

    def test_should_also_raise_an_error(self):
        with self.assertRaises(SomeError):
            raises_some_error()
