"""Generate the charts in assets/images/ from the CSV data."""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from cppi import ROOT, load_ranking
from financials import load_financials

OUT = ROOT / "assets" / "images"


def ranking_chart() -> None:
    rows = load_ranking()
    names = [r[0] for r in rows]
    scores = [r[1] for r in rows]
    colors = ["#B3261E" if n == "Myanmar" else "#8FA3B5" for n in names]
    fig, ax = plt.subplots(figsize=(7, 4.5))
    bars = ax.barh(names, scores, color=colors)
    ax.invert_yaxis()
    ax.set_xlabel("CPPI score (%)")
    ax.set_title("CPPI ranking across ASEAN")
    for b, s in zip(bars, scores):
        ax.text(s + 0.3, b.get_y() + b.get_height() / 2, f"{s:.1f}", va="center", fontsize=9)
    ax.set_xlim(0, max(scores) * 1.12)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(OUT / "cppi_ranking.png", dpi=150)
    plt.close(fig)


def financial_chart() -> None:
    fin = load_financials()
    labels = ["Year 1", "Year 2", "Year 3+"]
    x = np.arange(len(labels))
    w = 0.27
    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.bar(x - w, fin["total_revenue"], w, label="Revenue", color="#3B6EA5")
    ax.bar(x, fin["total_operating_costs"], w, label="Operating costs", color="#B0B7BF")
    ax.bar(x + w, fin["surplus"], w, label="Surplus (reinvested)", color="#2E8B57")
    ax.set_xticks(x, labels)
    ax.set_ylabel("Units (standardised)")
    ax.set_title("Financial projection (model, not measured)")
    ax.legend(frameon=False)
    ax.yaxis.set_major_formatter(lambda v, _: f"{int(v):,}")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(OUT / "financial_projection.png", dpi=150)
    plt.close(fig)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    ranking_chart()
    financial_chart()
    print("Saved charts to", OUT)


if __name__ == "__main__":
    main()
