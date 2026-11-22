"""The tool and the resource are plain functions under their decorators, so they test like any other."""
from server import find, policy


def test_find_returns_every_matching_line_with_its_file():
    lines = find("store credit")
    assert lines and all("store credit" in line.lower() for line in lines)
    assert all(line.split(": ")[0].endswith(".txt") for line in lines)


def test_find_ignores_case():
    assert find("STORE CREDIT") == find("store credit")


def test_policy_reads_one_document():
    assert "return" in policy("returns").lower()
