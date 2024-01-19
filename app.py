# Python In-built packages
from pathlib import Path
import PIL

# External packages
import streamlit as st

# Local Modules
import settings
import helper

# Setting page layout
st.set_page_config(
    page_title="Drowing Detection",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
st.title("Drowning-probability detection")

# Sidebar
st.sidebar.header("ML Model Config")


confidence = float(st.sidebar.slider(
    "Select Model Confidence", 15, 60, 25)) / 100


model_path = 'best.pt'
# Load Pre-trained ML Model
try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)

st.sidebar.header("Image/Video Config")
source_radio = st.sidebar.radio(
    "Select Source", settings.SOURCES_LIST)

source_img = None
# If image is selected
if source_radio == settings.IMAGE:
    source_img = st.sidebar.file_uploader(
        "Choose an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))
    if source_img is None:
        default_image_path = str(settings.DEFAULT_IMAGE)
        default_image = PIL.Image.open(default_image_path)
        st.image(default_image_path, caption="Default Image",
                    use_column_width=True)
    else:
        uploaded_image = PIL.Image.open(source_img)
        st.image(source_img, caption="Uploaded Image",
                    use_column_width=True)
        
    if source_img is None:
        default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
        default_detected_image = PIL.Image.open(
            default_detected_image_path)
        st.image(default_detected_image_path, caption='Detected Probability',
                    use_column_width=True)
    else:
        if st.sidebar.button('Detect Drowning'):
            res = model.predict(uploaded_image,
                                conf=confidence
                                )
            boxes = res[0].boxes
            res_plotted = res[0].plot()[:, :, ::-1]
            st.image(res_plotted, caption='Detected Image',
                        use_column_width=True)
            try:
                with st.expander("Detected Proability"):
                    for box in boxes:
                        st.write(box.data)
            except Exception as ex:
                # st.write(ex)
                st.write("No image is uploaded yet!")

elif source_radio == settings.VIDEO:
    helper.play_stored_video(confidence, model)

elif source_radio == settings.WEBCAM:
    helper.play_webcam(confidence, model)

elif source_radio == settings.RTSP:
    helper.play_rtsp_stream(confidence, model)

elif source_radio == settings.YOUTUBE:
    helper.play_youtube_video(confidence, model)

else:
    st.error("Please select a valid source type!")

settings.account_sid = st.sidebar.text_input("Your Twilio account_sid")
settings.auth_token = st.sidebar.text_input("Your Twilio auth_token")
settings.to_ = st.sidebar.text_input("Your Twilio to_")
settings.from_ = st.sidebar.text_input("Your Twilio from_")
settings.imgbb_api = st.sidebar.text_input("Your ImgBB api-key")
# settings.alertmsg = st.sidebar.text_input("Your Custom alert message", "Drowning Alerts!!! Someone is drowning!!! 🛟🌊🛟🌊🛟")

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p><a style='display: block; text-align: center;' href="https://musabbir-arrafi.me/" target="_blank">🧑🏻‍💻 Musabbir Arrafi</a></p>
</div>
"""
# st.markdown(footer,unsafe_allow_html=True)