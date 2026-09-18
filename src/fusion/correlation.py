# -*- coding: utf-8 -*-
"""
BisAT — Fusion Module
Corrélation multi-sources
"""

import logging

logger = logging.getLogger("BisAT.Fusion")

def correlier(sources):
    logger.info("Corrélation des sources.")
    return {"sources": len(sources), "cohérence": True}
