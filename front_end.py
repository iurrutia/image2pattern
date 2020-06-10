# SETUP
# -----------------------------------

import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from process_image import process_image, get_table_download_link


st.write(""" # image2stitch""")
st.write(""" Turn an image into a knitting colour chart. """)
st.write(""" To start again, press 'r' or refresh this page. """)


# SIDEBAR
# -----------------------------------
st.sidebar.title("About")
st.sidebar.header("About image2stitch")
st.sidebar.markdown("This webapp produces colour charts of images using machine learning. Upload an image, choose some settings, and click *Process image* to create and download a csv file.")

st.sidebar.header("How do I open my csv file?")
st.sidebar.markdown("Open your csv file in a spreadsheet program, like Microsoft Excel, Google Docs, Numbers, or OpenOffice Calc. When prompted, choose commas as the column delimiter.")

st.sidebar.header("What do the settings mean?")
st.sidebar.markdown("Input the number of colours of yarn you want to use, the number of stitches (wide) for your colour chart, and the colour space. *Colour Space* allows you to pick what colour space the clustering algorithm will run on.")

st.sidebar.header("Can I see your code?")
st.sidebar.markdown("Sure! Check it out the code and the backstory of this project here: "'[github repo](https://github.com/iurrutia/image2pattern)')


# MAIN PAGE
# -----------------------------------
# -----------------------------------

# 1. USER UPLOADS IMAGE
# -----------------------------------
st.write(""" ## 1. Upload an image""")

img_buffer = st.file_uploader("Valid formats: png, jpg or jpeg", type = ["png", "jpg", "jpeg"])

if img_buffer is None:
    img = None
else:
    img = np.array(Image.open(img_buffer))
    
    
# 2. USER SELECTS THE NUMBER OF YARN COLOURS
# -----------------------------------
st.write(""" ## 2. Select your settings """)

x = st.slider("Select a number of yarn colours", value = 5, max_value = 15)

stitches = st.slider("Select the number of stitches (across)", value = 30, max_value = 250)

c_space = st.radio("Colour Space", options = ["RGB","HSV"], index = 0)


# 3. USER CLICKS 'PROCESS'
# -----------------------------------
st.write(""" ## 3. Process """)

if st.button('Process image'):
    
    if img_buffer is None:
        st.write("You have not uploaded a valid image above.")
    else:
        with st.spinner("Patternifying..."):
            # pass args to processing function:
            # output is the image, pattern is the pattern for the colour chart
            output, pattern = process_image(img, x, stitches, c_space)
            st.balloons()
            
            
            # Display image preview to user
            st.write(""" #### Image Preview:""")
            fig, ax = plt.subplots()
            im = ax.imshow(output)
            plt.axis('off')
            st.pyplot()
            
            # Download csv to user
            st.markdown(get_table_download_link(pattern), unsafe_allow_html=True)
            # st.write(""" #### Pattern preview:""")
            # st.write(pattern)
