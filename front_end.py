# SETUP
# -----------------------------------

import streamlit as st
import numpy as np
from process_image import process_image

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
st.sidebar.markdown("*Algorithm* allows you to choose which clustering algorithm is used to select the yarn colours. (k-means or agglomerative clustering). *Colour Space* allows you to pick what colour space the clustering algorithm will run on.")

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
    

    # Apply
    # -----------------------------------
    #display, chart = process_image(img, c_space)
    
    
# 2. USER SELECTS THE NUMBER OF YARN COLOURS
# -----------------------------------
st.write(""" ## 2. Select your settings """)

x = st.slider("Select a number of yarn colours", value = 5, max_value = 15)

st.write("You selected", x, "yarn colours.")

c_space = st.radio("Colour Space", options = ["RGB","HSV"], index = 0)

algo = st.radio("Algorithm", options = ["k-means","Agg"], index = 0)


# 3. USER CLICKS 'PROCESS'
# -----------------------------------
st.write(""" ## 3. Process """)

if st.button('Process image'):
    
    if img_buffer is None:
        st.write("You have not uploaded a valid image above.")

    else:
        with st.spinner("Patternifying..."):
            # pass args to processing function:
            output_chart, display = process_image(img, x, c_space, algo)
            st.balloons()
            
            
    np.savetxt("pattern.csv", output_chart, fmt='%i', delimiter=",") 
    f'<a href="data:file/csv;base64,{b64}" download="pattern.csv">Download csv file</a>'