# -*- coding: utf-8 -*-
"""
Created on Fri Jan 2 2026
@author: Michel Robitaille
DPSP Model Demonstration (English)
"""

import numpy as np
import matplotlib.pyplot as plt
from dpsp import DynamicSurvivalModel

def run_analysis():
    model = DynamicSurvivalModel(threshold=4.0)
    time = np.arange(0, 61, 6)
    
    # Simulation
    psa_responder = 12 * np.exp(-0.05 * time)   # Patient A: Responder
    psa_progression = 5 + (0.7 * time)          # Patient B: Progression
    
    # Calculations
    surv_a = model.predict_survival(time, psa_responder)
    surv_b = model.predict_survival(time, psa_progression)
    hr_final_b = model.get_hazard_ratio(psa_progression[-1])
    velocity_b = model.get_velocity(time, psa_progression)

    # Visualization
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

    ax1.plot(time, psa_responder, 'o-', color='tab:blue', label="Patient A (Responder)")
    ax1.plot(time, psa_progression, 's-', color='tab:orange', label="Patient B (Progression)")
    ax1.axhline(y=4.0, color='red', linestyle='--', alpha=0.6, label="Threshold (4.0 ng/mL)")
    ax1.set_ylabel("PSA (ng/mL)")
    ax1.set_title("PSA Biomarker Evolution")
    ax1.legend()
    ax1.grid(alpha=0.2)

    ax2.step(time, surv_a, where='post', color='tab:blue', lw=2.5, label="Survival Patient A")
    ax2.step(time, surv_b, where='post', color='tab:orange', lw=2.5, label=f"Survival Patient B (Final HR: {hr_final_b:.1f})")
    ax2.set_ylabel("Survival Probability S(t)")
    ax2.set_xlabel("Time (months)")
    ax2.set_ylim(0, 1.05)
    ax2.set_title(f"Dynamic Survival Prediction (Velocity B: {velocity_b:.2f} ng/mL/month)")
    ax2.legend()
    ax2.grid(alpha=0.2)

    plt.tight_layout()
    plt.show()

    print("-" * 50)
    print(f"CLINICAL CONCLUSION (Patient B):")
    print(f"At 60 months, the patient's PSA level is {psa_progression[-1]:.1f} ng/mL.")
    print(f"The Hazard Ratio is {hr_final_b:.1f}, meaning the risk is")
    print(f"{hr_final_b:.1f} times higher compared to the reference threshold.")
    print("-" * 50)

if __name__ == "__main__":
    run_analysis()