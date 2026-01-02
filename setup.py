# -*- coding: utf-8 -*-
"""
Created on Fri Jan  2 2026
@author: Michel Robitaille

Setup file for the Dynamic PSA Survival Predictor (DPSP)
Fichier de configuration pour l'installation du module DPSP
"""

from setuptools import setup, find_packages
import os

# Lecture du README pour la description longue / Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dpsp",
    version="0.1.0",
    author="Michel Robitaille",
#    author_email="votre.email@exemple.com",  # Optionnel / Optional
    description="Dynamic PSA Survival Predictor - Modèle de survie dynamique pour le cancer de la prostate",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/votre-nom/dpsp",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "pandas",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    python_requires='>=3.6',
)