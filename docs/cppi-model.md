# CPPI: Circular Prosthetic Potential Index

A weighted, normalised index used to decide where MettaLimb should start.

```
CPPI_c = Σ [ w_i × ( x_ic / max(x_i) ) ] × 100
```

| Component | Weight | Meaning |
|---|---|---|
| Waste | 0.40 | Plastic waste generated |
| Need | 0.30 | Prosthetic need (disability rate) |
| Readiness | 0.20 | PET recycling readiness |
| Gap | 0.10 | Accessibility gap (unmet need for assistive products) |

Expanded:

```
CPPI_c = [ 0.40 × Waste_c/Waste_max + 0.30 × Need_c/Need_max
         + 0.20 × Readiness_c/Readiness_max + 0.10 × Gap_c/Gap_max ] × 100
```

## Myanmar breakdown
| Component | Raw value | Normalised | Contribution | Weight |
|---|---|---|---|---|
| Waste | 1.44M tons (2020) | 0.177 | 0.071 | 0.40 |
| Need | 7.6% disability rate | 0.076 | 0.023 | 0.30 |
| Readiness | 74% PET recycling (Yangon) | 0.740 | 0.148 | 0.20 |
| Gap | 21.5% unmet need | 0.215 | 0.022 | 0.10 |
| **Score** | | | **0.264, i.e. 26.4%** | |

Sources: Our World in Data (2020), 2024 Myanmar Census, Statista (2019), rATA Survey (2021).

Myanmar's score is driven mainly by high PET recycling readiness (74% in Yangon) and significant unmet need (21.5%), so recycling infrastructure already exists and the need is well documented.

## ASEAN ranking
See the chart in the [README](../README.md) and the data in [`data/cppi_scores_asean.csv`](../data/cppi_scores_asean.csv).

What the ranking suggests:
- **Data prioritisation:** a weighted index replaces intuition
- **Concentration:** the top four countries account for 72% of ASEAN's plastic waste and need (as presented in the deck)
- **Dual-crisis overlap:** high waste and high prosthetic need overlap significantly
- **Modular design:** the index can be reused for other regions and supports phased expansion

## Reproduce
```bash
python models/cppi.py
```

## Limitations and next steps
- Weights are chosen by the team. Add the reasoning, and a sensitivity analysis showing how the ranking changes with different weights
- Publish the raw inputs for every country (see [`data/README.md`](../data/README.md)) so the full ranking can be recalculated, not only Myanmar's
- Normalisation needs one consistent rule, see [model-notes.md](model-notes.md)
