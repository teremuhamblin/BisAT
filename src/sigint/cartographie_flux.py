# -*- coding: utf-8 -*-
"""
BisAT — SIGINT Module
Cartographie des flux électromagnétiques
"""

import logging

logger = logging.getLogger("BisAT.SIGINT")

def cartographier(flux):
    """
    Génère une cartographie simplifiée des flux.
    """
    logger.info("Cartographie des flux en cours.")
    return {"clusters": len(set(flux)), "densité": len(flux)}
