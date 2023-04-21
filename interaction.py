#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st 
import pandas as pd
import numpy as np
from PIL import Image

st.write("My First Web App")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.write(chart_data)

