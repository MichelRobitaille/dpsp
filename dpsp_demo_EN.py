"""
DPSP MODEL DEMONSTRATION (ENGLISH)
Topic: Trajectory Comparison (PSA Increase vs Decrease)
Created on Fri Jan 2 2026
@author: Michel Robitaille

"""
import matplotlib.pyplot as plt
import numpy as np
import dpsp

# 1. Setup
model = dpsp.DynamicSurvivalModel(threshold=4.0)
time = np.arange(0, 61, 6)

# --- CASE 1: Progression (Increase) ---
psa_inc = 5 + (0.7 * time)
surv_inc = model.predict_survival(time, psa_inc)
hr_inc = model.get_hazard_ratio(psa_inc[-1])

# --- CASE 2: Treatment Response (Decrease) ---
psa_dec = 12 * np.exp(-0.04 * time) 
surv_dec = model.predict_survival(time, psa_dec)
hr_dec = model.get_hazard_ratio(psa_dec[-1])

# 2. Visualisation
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

# PSA Plot
ax1.plot(time, psa_inc, 's-', color='tab:red', label=f"Increase (Final: {psa_inc[-1]:.1f})")
ax1.plot(time, psa_dec, 'o-', color='tab:green', label=f"Decrease (Final: {psa_dec[-1]:.1f})")
ax1.axhline(y=4.0, color='black', linestyle='--', alpha=0.3, label="4.0 Threshold")
ax1.set_ylabel("PSA (ng/mL)")
ax1.set_title("PSA Evolution")
ax1.legend()

# Survival Plot
ax2.step(time, surv_inc, where='post', color='tab:red', lw=2, label=f"Survival - Increase (HR: {hr_inc:.2f})")
ax2.step(time, surv_dec, where='post', color='tab:green', lw=2, label=f"Survival - Decrease (HR: {hr_dec:.2f})")
ax2.set_ylabel("Survival Probability")
ax2.set_xlabel("Time (months)")
ax2.set_ylim(0, 1.05)
ax2.legend()

plt.tight_layout()
plt.show()

print(f"EN Analysis complete: Patient A (HR {hr_inc:.2f}) vs Patient B (HR {hr_dec:.2f})")