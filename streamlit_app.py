import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie
st.title("Automated Parking System using number plate detection")
hide_streamlit_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
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

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked1 = False

# if "button_clicked2" not in st.session_state:    
#     st.session_state.button_clicked2 = False

enter = st.button("Enter")

def callback():
    st.session_state.button_clicked =True


if enter:
    _left,left,l0,l1,l2, mid,_right = st.columns(7)
    with left:
        st.image("Cars428.png",width=500)
    import time

    my_bar = st.progress(0)
    st.info('Model is running ', icon="ℹ️")
    for percent_complete in range(100):
        time.sleep(0.001)
        my_bar.progress(percent_complete + 1)
    
    

# exit = st.button("Exit")

if st.button("Exit",on_click=callback):
    st.write(f"Payment amount : x Rs")
    st.write(f"Payment QR code :")
    _left,l1, mid,m1, _right,r1,r2 = st.columns(7)
    with mid:
        st.image("rick.jpg",width=200)
    
    
    pay = st.button("Make payment")
    # print(pay)
    if pay:
        st.success("Payment Successful")

    # accept = st.button("Accept")

    # if accept:

        # st.success("Payment successful")
