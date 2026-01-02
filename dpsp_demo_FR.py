"""
DÉMONSTRATION DU MODÈLE DPSP (FRANÇAIS)
Sujet : Comparaison de trajectoires (Hausse vs Baisse du PSA)
Created Fri Jan 2 2026
@author: Michel Robitaille
"""
import matplotlib.pyplot as plt
import numpy as np
import dpsp

# 1. Initialisation
model = dpsp.DynamicSurvivalModel(threshold=4.0)
temps = np.arange(0, 61, 6)

# --- CAS 1 : Progression (Hausse) ---
psa_hausse = 5 + (0.7 * temps)
surv_hausse = model.predict_survival(temps, psa_hausse)
hr_hausse = model.get_hazard_ratio(psa_hausse[-1])

# --- CAS 2 : Réponse au traitement (Baisse) ---
psa_baisse = 12 * np.exp(-0.04 * temps) 
surv_baisse = model.predict_survival(temps, psa_baisse)
hr_baisse = model.get_hazard_ratio(psa_baisse[-1])

# 2. Graphiques
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

# Graphique PSA
ax1.plot(temps, psa_hausse, 's-', color='tab:red', label=f"Hausse (Final: {psa_hausse[-1]:.1f})")
ax1.plot(temps, psa_baisse, 'o-', color='tab:green', label=f"Baisse (Final: {psa_baisse[-1]:.1f})")
ax1.axhline(y=4.0, color='black', linestyle='--', alpha=0.3, label="Seuil 4.0")
ax1.set_ylabel("PSA (ng/mL)")
ax1.set_title("Évolution du PSA")
ax1.legend()

# Graphique Survie
ax2.step(temps, surv_hausse, where='post', color='tab:red', lw=2, label=f"Survie - Hausse (HR: {hr_hausse:.2f})")
ax2.step(temps, surv_baisse, where='post', color='tab:green', lw=2, label=f"Survie - Baisse (HR: {hr_baisse:.2f})")
ax2.set_ylabel("Probabilité de Survie")
ax2.set_xlabel("Temps (mois)")
ax2.set_ylim(0, 1.05)
ax2.legend()

plt.tight_layout()
plt.show()

print(f"Analyse FR terminée : Patient A (HR {hr_hausse:.2f}) vs Patient B (HR {hr_baisse:.2f})")