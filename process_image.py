import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import skimage
from skimage import io
from skimage.transform import resize
from skimage.color import rgb2hsv, hsv2rgb
import base64
from io import BytesIO

from sklearn.cluster import KMeans, MiniBatchKMeans



# image - input image
# x - number of colours (an int between 0 and 15)
# stitches - how many stitches accross should the image be
# c_space - colour space: 0 = RGB, 1 = HSV
# algo - algorithm: 0 = k-means, 1 = agglomerative clustering ("Agg")

def process_image(image, x, stitches, c_space):
    
    # convert from rgb-a to rgb (remove 4th element of colour) if necessary:
    # ------------------------------
    if image.shape[2]==4:
        image_rgb = image[:,:,:3]
        print('after:', image_rgb.shape)
    else:
        image_rgb = image

        
    # specify colour space
    # ------------------------------
    if c_space == 1:
        image_rgb = rgb2hsv(image_rgb)
        
        
    # stretch image to the correct (stitch shape) ratio
    # ------------------------------
    ratio = 1.25
    h = round(image_rgb.shape[0]*ratio)
    w = image_rgb.shape[1]
    image_resized = resize(image_rgb, (h, w), anti_aliasing=True)
    
    
    # resize (to pixelate) the image   
    # ------------------------------
    # the new height, width
    h_2 = image_resized.shape[0]
    w_2 = image_resized.shape[1]
    # Calculate resizing factor using stiches (# desired stitches across image)
    r_factor = stitches/w_2
    # Rescale:
    im_rescaled = resize(image_resized, (round(h_2*r_factor),round(w_2*r_factor)), anti_aliasing = False)
    
    
    # cluster the pixels  
    # ------------------------------
    X = im_rescaled.reshape(-1,3)

    kmeans = KMeans(n_clusters = x).fit(X)
    labels_0 = kmeans.labels_
    segmented_img = kmeans.cluster_centers_[kmeans.labels_]
    segmented_img = segmented_img.reshape(im_rescaled.shape)
    
    
    # if c_space was hsv, turn back to RGB for display to user
    # ------------------------------
    if c_space == 1:
        segmented_img = hsv2rgb(segmented_img)
        
    # turn image back to input aspect ration
    # ------------------------------


    segmented_img = resize(segmented_img, (h_2, int(w_2*ratio)), order = 0, preserve_range = True, anti_aliasing=True)
        
    
    # creates outputs to return
    # ------------------------------

    # Shape of desired output: im_rescaled
    labels = labels_0
    output = labels.reshape(im_rescaled.shape[0:2])
    output = output.astype(int)

    # add header row:
    header_row = [[i for i in range(1,len(output[0])+1)]]
    pattern = np.concatenate((header_row, output), axis=0)
    
    # turn pattern into a dataframe:
    df_pattern = pd.DataFrame(pattern[1:], columns=pattern[0,0:])

    # output is the image, pattern is the pattern for the colour chart
    return segmented_img, df_pattern
    


def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(
        csv.encode()
    ).decode()  # some strings <-> bytes conversions necessary here
    return f'<a href="data:file/csv;base64,{b64}" download="pattern.csv">Download csv file</a>'

