import streamlit as st
from img_classification import teachable_machine_classification
from PIL import Image, ImageOps

st.title("使用谷歌的可教机器进行图像分类")
st.header("天气图像")
st.text("上传彩色天气图片")

uploaded_file = st.file_uploader("选择..", type=["jpg","png","jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='上传了图片。', use_column_width=True)
    st.write("")
    st.write("分类...")
    label = teachable_machine_classification(image, 'keras_model.h5')
    if label == 0:
        st.write("dew,露")
    elif label == 1:
        st.write("fogsmog,雾霾")
    elif label == 2:
        st.write("frost,霜")
    elif label == 3:
        st.write("glaze,釉")
    elif label == 4:
        st.write("hail,冰雹")
    elif label == 5:
        st.write("lighning,闪电")
    elif label == 6:
        st.write("rain,雨")
    elif label == 7:
        st.write("rainbow,彩虹")
    elif label == 8:
        st.write("rime,雾凇")
    elif label == 9:
        st.write("sandstorm,沙暴")
    else:
        st.write("snow,雪")

st.text("类:露, 雾霾,  霜, 釉, 冰雹, 闪电, 雨, 彩虹, 雾凇, 沙暴, 雪 ")