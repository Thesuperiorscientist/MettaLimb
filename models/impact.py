"""Impact model (Total Impact Score) as described in the deck.

    TIS = sum_i (Outcome_i * Weight_i)

Outcomes: prosthetics produced, CO2 saved (tons), jobs created. Weights 0.4 / 0.3 / 0.3.
See docs/model-notes.md for numbers in the deck that do not reconcile.
"""
from __future__ import annotations

PHI = 1000        # yield coefficient, units per ton of PET
EPSILON = 0.6     # scale elasticity, applied as a cost multiplier ($250 * 0.6 = $150)
LAMBDA = 1.5      # tons of CO2 saved per ton of PET recycled
MU = 1.17         # jobs per kiloton (1,000 tons) of PET recycled
TIS_WEIGHTS = (0.4, 0.3, 0.3)   # prosthetics, CO2, jobs


def units_from_pet(pet_tons: float, phi: float = PHI) -> float:
    return pet_tons * phi


def co2_saved(pet_tons: float, lam: float = LAMBDA) -> float:
    return pet_tons * lam


def jobs_created(pet_tons: float, mu: float = MU) -> float:
    return mu * pet_tons / 1000.0


def unit_cost(cost_now: float, epsilon: float = EPSILON) -> float:
    return cost_now * epsilon


def total_impact_score(prosthetics: float, co2_tons: float, jobs: float,
                       weights: tuple = TIS_WEIGHTS) -> float:
    return prosthetics * weights[0] + co2_tons * weights[1] + jobs * weights[2]


def main() -> None:
    pet = 500
    as_presented = total_impact_score(500, 1250, 0.585)
    print("TIS exactly as presented (500, 1,250, 0.585):", round(as_presented, 2), "-> 575")

    print("\nRecalculated from the stated coefficients for 500 tons of PET")
    print("  units at phi = 1,000/ton :", units_from_pet(pet))
    print("  CO2 saved                :", co2_saved(pet), "tons")
    print("  jobs created             :", jobs_created(pet))
    print("  TIS with 500 prosthetics :", round(total_impact_score(500, co2_saved(pet), jobs_created(pet)), 2))
    print("\nUnit cost 2026 -> 2030   :", 250, "->", unit_cost(250))


if __name__ == "__main__":
    main()
