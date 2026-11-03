import math

from darts import estimate_pi


def test_estimate_is_close_to_pi():
    assert abs(estimate_pi(n_darts=100_000, seed=159) - math.pi) < 0.05


def test_same_seed_gives_same_answer():
    assert estimate_pi(seed=1) == estimate_pi(seed=1)
