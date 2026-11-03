"""Estimate pi by throwing random darts at a square with an inscribed circle."""
import numpy as np


def estimate_pi(n_darts=100_000, seed=159):
    rng = np.random.default_rng(seed)
    x = rng.uniform(-1, 1, n_darts)
    y = rng.uniform(-1, 1, n_darts)
    inside_circle = (x**2 + y**2) <= 1
    return 4 * inside_circle.sum() / n_darts


if __name__ == "__main__":
    print(f"Estimated pi: {estimate_pi():.5f}")
