"""Financial projection checks.

Reads data/financials.csv and data/startup_costs.csv and verifies the arithmetic:
surplus = revenue - operating costs, cumulative = running total, start-up total.
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PERIODS = ["year_1", "year_2", "year_3_plus"]


def load_financials(path: Path = ROOT / "data" / "financials.csv") -> dict[str, list[float]]:
    with open(path, newline="", encoding="utf-8") as f:
        return {r["category"]: [float(r[p]) for p in PERIODS] for r in csv.DictReader(f)}


def load_startup_costs(path: Path = ROOT / "data" / "startup_costs.csv") -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def surplus(revenue: list[float], costs: list[float]) -> list[float]:
    return [r - c for r, c in zip(revenue, costs)]


def cumulative(values: list[float]) -> list[float]:
    out, total = [], 0.0
    for v in values:
        total += v
        out.append(total)
    return out


def startup_total(rows: list[dict]) -> float:
    return sum(float(r["amount"]) for r in rows)


def main() -> None:
    fin = load_financials()
    s = surplus(fin["total_revenue"], fin["total_operating_costs"])
    cum = cumulative(s)
    print("Surplus computed  :", s, "| in data:", fin["surplus"])
    print("Cumulative        :", cum, "| in data:", fin["cumulative_surplus"])
    print("Start-up total    :", startup_total(load_startup_costs()))
    ok = s == fin["surplus"] and cum == fin["cumulative_surplus"]
    print("Arithmetic checks :", "OK" if ok else "MISMATCH")


if __name__ == "__main__":
    main()
