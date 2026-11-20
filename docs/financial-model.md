# Financial model

Lean costs, affordable pricing, reinvested surplus. Amounts are shown in standardised units for ASEAN-wide comparability, as in the deck.

## One-time start-up costs
| Category | Item | Amount |
|---|---|---|
| Equipment | Compact shredder and extruder | 5,000 |
| Equipment | 3D printer (prosthetic capable) | 3,000 |
| Technology | Microcontrollers, actuators, sensors | 2,000 |
| Facility | Small workshop setup | 2,000 |
| Training | Local technician training | 3,000 |
| **Total** | | **15,000** |

## Projection
| | Year 1 | Year 2 | Year 3+ |
|---|---|---|---|
| Total revenue | 125,000 | 315,000 | 580,000 |
| Total operating costs | 72,400 | 153,600 | 245,000 |
| **Surplus** | 52,600 | 161,400 | 335,000 |
| Surplus use | Reinvested | Reinvested | Reinvested |
| Cumulative surplus | 52,600 | 214,000 | 549,000 |

Every unit of surplus is reinvested, not distributed.

## Reproduce
```bash
python models/financials.py
```
The script checks the arithmetic (surplus = revenue minus costs, running total, start-up total).

## Assumptions still to document
The deck gives totals only. To make the model reusable, add:
- Price per device and number of devices per year behind each revenue figure
- Breakdown of operating costs (materials, labour, maintenance, outreach)
- Funding sources for the start-up cost
- Currency and the year the units refer to
