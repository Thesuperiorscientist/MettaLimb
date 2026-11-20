"""Circular Prosthetic Potential Index (CPPI).

    CPPI_c = sum_i [ w_i * (x_ic / max_c x_i) ] * 100

Components: plastic waste, prosthetic need, recycling readiness, accessibility gap.
Weights chosen by the team: 0.40 / 0.30 / 0.20 / 0.10.
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEIGHTS = {"waste": 0.40, "need": 0.30, "readiness": 0.20, "gap": 0.10}


def normalize_by_max(values: dict[str, float]) -> dict[str, float]:
    """Scale each country's value by the maximum across countries (x / max x)."""
    top = max(values.values())
    return {k: v / top for k, v in values.items()}


def contributions(normalized: dict[str, float], weights: dict[str, float] = WEIGHTS) -> dict[str, float]:
    """Weighted contribution of each component (0-1 scale)."""
    return {k: weights[k] * normalized[k] for k in weights}


def cppi(normalized: dict[str, float], weights: dict[str, float] = WEIGHTS) -> float:
    """CPPI on a 0-100 scale from components already scaled to 0-1."""
    if abs(sum(weights.values()) - 1.0) > 1e-9:
        raise ValueError("weights must sum to 1")
    return 100.0 * sum(contributions(normalized, weights).values())


def load_decomposition(path: Path = ROOT / "data" / "cppi_inputs_myanmar.csv") -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_ranking(path: Path = ROOT / "data" / "cppi_scores_asean.csv") -> list[tuple[str, float]]:
    """(country, score) pairs sorted from highest to lowest."""
    with open(path, newline="", encoding="utf-8") as f:
        rows = [(r["country"], float(r["cppi_score"])) for r in csv.DictReader(f)]
    return sorted(rows, key=lambda r: r[1], reverse=True)


def main() -> None:
    rows = load_decomposition()
    normalized = {r["component"]: float(r["normalized"]) for r in rows}
    weights = {r["component"]: float(r["weight"]) for r in rows}
    contrib = contributions(normalized, weights)

    print("CPPI decomposition: Myanmar")
    print(f"{'component':<10} {'raw':>8}  {'unit':<26} {'norm':>6} {'weight':>6} {'contrib':>8}")
    for r in rows:
        c = r["component"]
        print(f"{c:<10} {float(r['raw_value']):>8}  {r['raw_unit']:<26} "
              f"{normalized[c]:>6.3f} {weights[c]:>6.2f} {contrib[c]:>8.4f}")
    score = cppi(normalized, weights)
    rounded_sum = sum(round(v, 3) for v in contrib.values())
    print(f"\nExact CPPI: {score:.2f}")
    print(f"Sum of contributions rounded to 3 decimals: {rounded_sum:.3f} -> {rounded_sum * 100:.1f} (the figure shown in the deck)")

    print("\nASEAN ranking (scores as shown in the deck chart)")
    for i, (country, s) in enumerate(load_ranking(), 1):
        print(f"{i:>2}. {country:<12} {s:>5.1f}")


if __name__ == "__main__":
    main()
