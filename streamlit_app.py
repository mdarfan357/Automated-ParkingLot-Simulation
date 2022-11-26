import streamlit as st
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

# def callback2():
#     st.session_state.button_clicked =True



if enter:
    st.write("The following is a simulation of a Automated Parking lot system using CCTV ")     
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
