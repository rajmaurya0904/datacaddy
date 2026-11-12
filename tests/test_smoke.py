"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import datacaddy


def test_version_is_set() -> None:
    assert datacaddy.__version__
