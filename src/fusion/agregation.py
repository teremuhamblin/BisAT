# -*- coding: utf-8 -*-
"""
BisAT — Fusion Module
Agrégation de données
"""

import logging

logger = logging.getLogger("BisAT.Fusion")

def agreguer(donnees):
    logger.info("Agrégation des données.")
    return {"taille": len(donnees), "résumé": str(donnees)[:50]}
