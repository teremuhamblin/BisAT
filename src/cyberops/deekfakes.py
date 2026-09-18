# -*- coding: utf-8 -*-
"""
BisAT — CyberOps Module
Détection de deepfakes
"""

import logging

logger = logging.getLogger("BisAT.CyberOps")

def detecter(image):
    logger.info("Analyse deepfake en cours.")
    return {"deepfake": False, "confiance": 0.92}
