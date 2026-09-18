# -*- coding: utf-8 -*-
"""
BisAT — Atlas Module
Analyse des clusters
"""

import logging

logger = logging.getLogger("BisAT.Atlas")

def analyser_clusters(points):
    logger.info("Analyse des clusters.")
    return {"clusters": 2, "densité": len(points)}
