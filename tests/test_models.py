"""Checks that the code reproduces the numbers in the deck.

Run with:  python tests/test_models.py   (or pytest)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "models"))

import cppi
import financials
import impact


def test_weights_sum_to_one():
    assert abs(sum(cppi.WEIGHTS.values()) - 1.0) < 1e-12


def test_myanmar_cppi():
    rows = cppi.load_decomposition()
    norm = {r["component"]: float(r["normalized"]) for r in rows}
    score = cppi.cppi(norm)
    assert abs(score - 26.31) < 0.01              # exact value from the table
    rounded_sum = sum(round(v, 3) for v in cppi.contributions(norm).values())
    assert abs(rounded_sum - 0.264) < 1e-9        # the figure shown in the deck


def test_ranking_order():
    ranking = cppi.load_ranking()
    assert ranking[0][0] == "Myanmar"
    assert ranking[-1][0] == "Brunei"
    assert len(ranking) == 10


def test_normalize_by_max():
    out = cppi.normalize_by_max({"a": 2.0, "b": 4.0})
    assert out == {"a": 0.5, "b": 1.0}


def test_financial_arithmetic():
    fin = financials.load_financials()
    s = financials.surplus(fin["total_revenue"], fin["total_operating_costs"])
    assert s == fin["surplus"]
    assert financials.cumulative(s) == fin["cumulative_surplus"]


def test_startup_total():
    assert financials.startup_total(financials.load_startup_costs()) == 15000


def test_tis_as_presented():
    assert round(impact.total_impact_score(500, 1250, 0.585)) == 575


def test_impact_from_coefficients():
    # 500 tons * 1.5 t CO2/t = 750 (the deck uses 1,250; see docs/model-notes.md)
    assert impact.co2_saved(500) == 750
    assert abs(impact.jobs_created(500) - 0.585) < 1e-9
    assert impact.unit_cost(250) == 150


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
        print("ok  ", t.__name__)
    print(f"\n{len(tests)} checks passed")
