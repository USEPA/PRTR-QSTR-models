#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importing libraries
import logging
logging.basicConfig(level=logging.INFO)


def modeling_pipeline(df_ml):
    '''
    Function to run the modeling 
    '''

    logger = logging.getLogger(' Data-driven modeling --> Modeling')