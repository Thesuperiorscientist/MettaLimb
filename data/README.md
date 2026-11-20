# Data

| File | Contents | Provenance |
|---|---|---|
| `cppi_scores_asean.csv` | CPPI score for ten ASEAN countries | Read from the bar chart on slide 16 of the deck |
| `cppi_inputs_myanmar.csv` | Myanmar's CPPI components, weights and sources | Table on slide 15 of the deck; the source for each component follows the order the sources are listed on the slide |
| `financials.csv` | Revenue, operating costs and surplus by period | Slide 23 of the deck; the last column is labelled "Year 2+" in the deck |
| `startup_costs.csv` | One-time start-up costs | Slide 22 of the deck |

## To add
Only Myanmar's raw inputs are available. To let anyone recalculate the whole ranking, add a file with these columns for every country, plus the source and year for each value:

```
country,waste_tons,disability_rate_pct,pet_recycling_readiness_pct,unmet_need_pct
```

Amounts in the financial files are in standardised units, as stated in the deck.
