import pytest

from module_03.quadratic_equation import EPSILON, solve


@pytest.mark.parametrize("a, b, c, solution", [
    (1., 0., 1., (None, None)),
    (1., 2., 1., (-1., -1.)),

    (1.,  EPSILON, 1., (None, None)),
    (1., -EPSILON, 1., (None, None)),

    (1.,  EPSILON, -1., (0.999999995, -1.000000005)),
    (1., -EPSILON, -1., (1.000000005, -0.999999995)),

    (1., 2. - EPSILON, 1., (None, None)),
    (1., 2. + EPSILON, 1., (-0.9999000050003038, -1.0001000049996962)),
    (1., 0., -1., (1., -1.)),
])
def test_positive(a, b, c, solution):
    assert solve(a, b, c) == solution


@pytest.mark.parametrize("a, b, c, exc_type, exc_text", [
    (0, 0, 0, TypeError, "all arguments must be float"),
    (0., 0., 0, TypeError, "all arguments must be float"),
    (0., 0., 0., ValueError, "argument 'a' сan't be equal to 0"),
    ( EPSILON, 0., 0., ValueError, "argument 'a' сan't be equal to 0"),
    (-EPSILON, 0., 0., ValueError, "argument 'a' сan't be equal to 0"),
])
def test_negative(a, b, c, exc_type, exc_text):
    with pytest.raises(exc_type) as exc:
        solve(a, b, c)
    assert exc.value.args[0] == exc_text
