# Impact model

A quantified model linking recycled PET to environmental, social and economic outcomes. Values are planning targets, not measurements.

| Driver | Coefficient | Transformation | Outcome as presented |
|---|---|---|---|
| Yield | φ = 1,000 units per ton | 500 tons PET (2026) | 500 prosthetics |
| Scale elasticity | ε = 0.6 | $250 per unit (2026) | $150 per unit (2030) |
| Emission factor | λ = 1.5 t CO₂ per t PET | 1 ton PET recycled | 1.5 tons CO₂ saved |
| Employment multiplier | μ = 1.17 jobs per kt | 1,000 tons PET recycled | 1.17 jobs |

## Total Impact Score
```
TIS = Σ (Outcome_i × Weight_i)
TIS (2026) = (500 × 0.4) + (1,250 × 0.3) + (0.585 × 0.3) = 575
```

The first term is the number of prosthetics and the third is jobs (500 tons × 1.17 jobs per kt = 0.585). The second term, 1,250, is presumably the CO₂ outcome.

## Reproduce
```bash
python models/impact.py
```
The script prints the score exactly as presented and a recalculation from the stated coefficients.

## Open points
Some numbers above do not reconcile with each other (for example 500 tons of PET at 1.5 t CO₂ per ton is 750, not 1,250). These are listed in [model-notes.md](model-notes.md) and should be resolved before the model is cited.
