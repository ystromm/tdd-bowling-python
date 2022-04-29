import pytest
from assertpy import assert_that

from test.error import SomeError, raises_some_error


def test_1_minus_1_should_return_0():
    assert 0 == 1 - 1


def test_abc_should_contain_b():
    assert "b" in "abc"


def test_1_plus_1_should_be_close_to_2():
    assert_that(1.1 + 1).is_close_to(2, 0.1)


def test_a_plus_bc_should_not_be_empty():
    assert_that("a" + "bcd").is_not_empty().contains("a").contains("bc")


def test_should_raise_an_error():
    try:
        raises_some_error()
        pytest.fail("Expected SomeError to be raised")
    except SomeError as e:
        assert "borken" in e.message


