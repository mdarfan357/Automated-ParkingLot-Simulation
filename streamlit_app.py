import streamlit as st
# import edgenum as en
import edgenum as en 
import time
import datetime as ts
import requests
import json
from streamlit_lottie import st_lottie
# IMAGE_PATH = "g9.png" # "g7.jpg" # "g8.jpg"
IMAGE_PATH = "g11.jpg"


if "func_out" not in st.session_state:
    st.session_state.func_out = en.edgenum(IMAGE_PATH)



st.title("Automated Parking System using number plate detection")

def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()

lottie_hello = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_khm3kzeu.json")
            

st_lottie(
    lottie_hello,
    speed=0.75,
    reverse=False,
    loop=False,
    quality="low", # medium ; high
  
    height=None,
    width=None,
    key=None,
)

hide_streamlit_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False
    
enter = st.button("Enter")

def callback():
    st.session_state.button_clicked =True

output = st.session_state.func_out

if enter:
    _left,left,l0,l1,l2, mid,_right = st.columns(7)
    with left:
        st.image(IMAGE_PATH,width=500)


    my_bar = st.progress(0)
    
    for percent_complete in range(100):
        time.sleep(0.001)
        my_bar.progress(percent_complete + 1)
    st.info('Vehicle entry registered, press exit to simulate vehicle exit ', icon="ℹ️")

dt1 = ts.datetime(2022, 11, 26, 12, 25, 29, 674107)    
# dt1 = ts.datetime(2022, 11, 27, 5, 25, 29, 674107)   

timedf = output[0]-dt1


diff_in_minutes = timedf.total_seconds() / 60
if diff_in_minutes <= 60:
    Amount = 20
elif diff_in_minutes > 60 and diff_in_minutes <= 120:
    amount = 30
elif diff_in_minutes > 120 and diff_in_minutes <= 180:
    amount = 40
elif diff_in_minutes > 180:
    amount = 50

if st.button("Exit",on_click=callback):

    st.markdown(f"**Payment amount for vehicle number {output[1]} : {amount} Rs for {round(diff_in_minutes/60,2)} hours.**")
    st.write(f"Payment QR code :")
    _left,l1, mid,m1, _right,r1,r2 = st.columns(7)
    with mid:
        st.image("rick.jpg",width=200)
    
    
    pay = st.button("Make payment")
    # print(pay)
    if pay:
        time.sleep(500)
        st.success("Payment Successful")

