# -*- coding: utf-8 -*-
"""
BisAT — Atlas Module
Détection des zones rouges
"""

import logging

logger = logging.getLogger("BisAT.Atlas")

def detecter_zones(donnees):
    logger.info("Détection des zones rouges.")
    return {"zones": 3, "niveau": "critique"}
