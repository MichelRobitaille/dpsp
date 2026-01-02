# -*- coding: utf-8 -*-
"""
Created on Fri Jan 2 2026
@author: Michel Robitaille
Démonstration du modèle DPSP (Français)
"""

import numpy as np
import matplotlib.pyplot as plt
# Importation du moteur depuis le fichier dpsp.py
from dpsp import DynamicSurvivalModel

def run_analysis():
    model = DynamicSurvivalModel(threshold=4.0)
    temps = np.arange(0, 61, 6)
    
    # Simulation
    psa_baisse = 12 * np.exp(-0.05 * temps)  # Patient A : Répondeur
    psa_hausse = 5 + (0.7 * temps)           # Patient B : Progression
    
    # Calculs
    surv_a = model.predict_survival(temps, psa_baisse)
    surv_b = model.predict_survival(temps, psa_hausse)
    hr_final_b = model.get_hazard_ratio(psa_hausse[-1])
    vitesse_b = model.get_velocity(temps, psa_hausse)

    # Visualisation
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

    ax1.plot(temps, psa_baisse, 'o-', color='tab:blue', label="Patient A (Répondeur)")
    ax1.plot(temps, psa_hausse, 's-', color='tab:orange', label="Patient B (Progression)")
    ax1.axhline(y=4.0, color='red', linestyle='--', alpha=0.6, label="Seuil (4.0 ng/mL)")
    ax1.set_ylabel("PSA (ng/mL)")
    ax1.set_title("Évolution des Biomarqueurs PSA")
    ax1.legend()
    ax1.grid(alpha=0.2)

    ax2.step(temps, surv_a, where='post', color='tab:blue', lw=2.5, label="Survie Patient A")
    ax2.step(temps, surv_b, where='post', color='tab:orange', lw=2.5, label=f"Survie Patient B (HR Final: {hr_final_b:.1f})")
    ax2.set_ylabel("Probabilité de Survie S(t)")
    ax2.set_xlabel("Temps (mois)")
    ax2.set_ylim(0, 1.05)
    ax2.set_title(f"Prédiction de Survie Dynamique (Vitesse B: {vitesse_b:.2f} ng/mL/mois)")
    ax2.legend()
    ax2.grid(alpha=0.2)

    plt.tight_layout()
    plt.show()

    print("-" * 50)
    print(f"CONCLUSION CLINIQUE (Patient B) :")
    print(f"À 60 mois, le patient présente un PSA de {psa_hausse[-1]:.1f} ng/mL.")
    print(f"Son Hazard Ratio est de {hr_final_b:.1f}, soit un risque")
    print(f"multiplié par {hr_final_b:.1f} par rapport au seuil de référence.")
    print("-" * 50)

if __name__ == "__main__":
    run_analysis()