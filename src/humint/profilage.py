# -*- coding: utf-8 -*-
"""
BisAT — HUMINT Module
Profilage comportemental
"""

import logging

logger = logging.getLogger("BisAT.HUMINT")

def profiler(individu):
    logger.info(f"Profilage de {individu.get('id', 'inconnu')}")
    return {
        "risque": "faible",
        "cohérence": True,
        "pattern": "standard"
    }
