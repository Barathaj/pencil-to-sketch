
#Lets Grow More Internship

#pencil to Sketch using python

import cv2
import streamlit as st
import numpy as np
from io import BytesIO

st.header('Image To Sketch Using Python')
def convert(uploaded_file):
    img= cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    bit=cv2.bitwise_not(gray)
    blur=cv2.GaussianBlur(bit,(21,21),0)
    bit2=cv2.bitwise_not(blur)
    result=cv2.divide(gray,bit2,scale=256.0)
    return result

uploaded_file=st.file_uploader('choose an image...',type=['jpg','jpeg','png','webp'])

if uploaded_file is not None:
    final=convert(uploaded_file)
    st.image(final, caption='Processed Image', use_column_width=True)
    if st.button("Download Sketched Image"):
       
        processed_image_bytes = cv2.imencode('.jpg', final)[1].tobytes()

        
        processed_image_io = BytesIO(processed_image_bytes)

        st.download_button(
            label="Download processed Image",
            data=processed_image_io,
            file_name="processed_image.jpg",
            key="processed_image_download",
        )