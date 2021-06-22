# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.8.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # So easy, *voilà*!
#
# In this example notebook, we demonstrate how Voilà can render Jupyter notebooks with interactions requiring a roundtrip to the kernel.

# %% [markdown]
# ## Jupyter Widgets

# %%
import ipywidgets as widgets

slider = widgets.FloatSlider(description='$x$', value=0)
text = widgets.FloatText(disabled=True, description='$x^3$')

def compute(*ignore):
    text.value = str(slider.value ** 3)

slider.observe(compute, 'value')

widgets.VBox([slider, text])

# %%
# [markdown]
# ## Basic outputs of code cells

# %%
# import pandas as pd

# iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
# iris

# %%
