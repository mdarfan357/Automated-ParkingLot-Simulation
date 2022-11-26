import streamlit as st
from flask import request
st.title("Automated Parking System using number plate detection")
hide_streamlit_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked1 = False

# if "button_clicked2" not in st.session_state:    
#     st.session_state.button_clicked2 = False

enter = st.button("Enter")

def callback():
    st.session_state.button_clicked =True

def load_lottieurl(url):
  r = request.get(url)
  if r.status_code != 200:
    return None
  return r.json()

lottie_hello = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_khm3kzeu.json")
            



if enter:
    st.write("The following is a simulation of a Automated Parking lot system using CCTV ")     
    _left,left,l0,l1,l2, mid,_right = st.columns(7)
    with left:
        st.image("Cars428.png",width=500)
    import time

    my_bar = st.progress(0)
    
    
    

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
