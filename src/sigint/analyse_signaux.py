# -*- coding: utf-8 -*-
"""
BisAT — SIGINT Module
Analyse des signaux électromagnétiques
"""

import logging

logger = logging.getLogger("BisAT.SIGINT")

def analyser_signal(data):
    """
    Analyse un signal brut et retourne un rapport minimal.
    """
    logger.info("Analyse du signal lancée.")
    return {
        "longueur": len(data),
        "max": max(data),
        "min": min(data),
        "moyenne": sum(data) / len(data)
    }
