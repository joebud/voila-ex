#!/bin/bash

echo "Synching notebooks..."

# jupytext --set-formats ipynb,py:percent index.ipynb  # Turn index.ipynb into a paired ipynb/py notebook

jupytext --sync index.ipynb  

voila index.ipynb  # --strip_sources=False
