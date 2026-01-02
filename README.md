# Dynamic PSA Survival Predictor (DPSP)
**Modèle probabiliste de survie dynamique basé sur le PSA** 
**Probabilistic dynamic survival model based on PSA levels**

---

## Description
**FR :** DPSP est un module Python léger conçu pour la simulation et la prédiction de survie basées sur la dynamique longitudinale du PSA (Prostate-Specific Antigen). Contrairement aux approches classiques comme le modèle de Cox (CoxTimeVaryingFitter), DPSP utilise une méthode probabiliste segmentée qui évite les erreurs de convergence (NaN) et permet une projection personnalisée en temps réel.

**EN :** DPSP is a lightweight Python module designed for survival simulation and prediction based on longitudinal PSA (Prostate-Specific Antigen) dynamics. Unlike traditional approaches like the Cox Time-Varying model, DPSP uses a segmented probabilistic method that avoids convergence errors (NaN) and allows for personalized real-time projections.

---

## Pourquoi utiliser DPSP ? / Why use DPSP?

### 1. Stabilité mathématique / Mathematical Stability
* **FR :** Élimine les problèmes de "séparation complète" où les modèles statistiques échouent quand un biomarqueur prédit trop parfaitement un événement.
* **EN :** Eliminates "complete separation" issues where statistical models fail when a biomarker predicts an event too perfectly.

### 2. Interprétation Clinique / Clinical Interpretation
* **FR :** Intègre directement le seuil de **4.0 ng/mL** et le calcul du **Hazard Ratio (HR)** dynamique.
* **EN :** Directly integrates the **4.0 ng/mL** threshold and dynamic **Hazard Ratio (HR)** calculation.

### 3. Optimisé pour Jupyter / Optimized for Jupyter
* **FR :** Conçu pour une utilisation interactive et une visualisation rapide des trajectoires de patients.
* **EN :** Designed for interactive use and rapid visualization of patient trajectories.

---

## Structure du Projet / Project Structure
* `dpsp.py` : Le module contenant la classe `DynamicSurvivalModel`. / *The module containing the DynamicSurvivalModel class.*
* `dpsp_demo.py` : Script de démonstration avec graphiques. / *Demonstration script with plots.*
* `Exemple_Analyse.ipynb` : Notebook de démonstration (PSA hausse vs baisse). / *Demonstration Notebook (PSA rise vs. fall).*

---

## Utilisation Rapide / Quick Start

```python
from dpsp import DynamicSurvivalModel
import numpy as np

# Initialisation (Threshold = 4.0 ng/mL)
model = DynamicSurvivalModel(threshold=4.0)

# Données / Data
time = np.arange(0, 61, 6)
psa_values = 5 + (0.7 * time)

# Calcul de survie / Survival calculation
survival = model.predict_survival(time, psa_values)