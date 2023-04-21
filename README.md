# interaction1
import streamlit as st 
import pandas as pd
import numpy as np
from PIL import Image

st.write("My First Web App")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.write(chart_data)

image = Image.open('/Users/anitabaculima/Desktop/myapp/logo1.jpg')
st.image(image)
st.dataframe(chart_data)
option = st.selectbox('Select',['a','b','c'])
st.bar_chart(chart_data[option])
