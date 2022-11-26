import streamlit as st
# import edgenum as en
from edgenum.py import edgenum as en 
import datetime as ts

if "func_out" not in st.session_state:
    st.session_state.func_out = en.edgenum("C:/Users/rgkul/Downloads/images/g7.jpg")


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
    quality="high", # medium ; high
  
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
    st.session_state.button_clicked1 = False

# if "button_clicked2" not in st.session_state:    
#     st.session_state.button_clicked2 = False

enter = st.button("Enter")

def callback():
    st.session_state.button_clicked =True

# def callback2():
#     st.session_state.button_clicked =True
output = st.session_state.func_out
# output = en.edgenum("C:/Users/rgkul/Downloads/images/g7.jpg")

if enter:
    _left,left,l0,l1,l2, mid,_right = st.columns(7)
    with left:
        st.image("images/g7.jpg",width=500)
    import time

    my_bar = st.progress(0)
    
    for percent_complete in range(100):
        time.sleep(0.001)
        my_bar.progress(percent_complete + 1)
    st.info('Vehicle entry registered, press exit to simulate vehicle exit ', icon="ℹ️")

dt1 = ts.datetime(2022, 11, 26, 12, 25, 29, 674107)    
try:
    timedf = output[0]-dt1
except:
    pass
# append_to_csv(tweet[0],tweet[1])

# tweet - date time and car plate
diff_in_minutes = timedf.total_seconds() / 60
if diff_in_minutes <= 60:
    Amount = 20
elif diff_in_minutes > 60 and diff_in_minutes <= 120:
    amount = 30
elif diff_in_minutes > 120 and diff_in_minutes <= 180:
    amount = 40
elif diff_in_minutes > 180:
    amount = 50
# exit = st.button("Exit")

if st.button("Exit",on_click=callback):

    st.markdown(f"**Payment amount for vehicle number {output[1]} : {amount} Rs for {round(diff_in_minutes/60,2)} hours.**")
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
