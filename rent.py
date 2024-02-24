#importing necessary packages
import pandas as pd
import streamlit as st
import pickle 

#loading the dataset for options
data=pd.read_csv(r"C:\\Users\\devli\\cf projects\\rent\\data.csv")

#creating dictionaries and mapping for options
type_dict=dict(zip(data['type'].unique(), data['type_e'].unique()))
lease_type_dict=dict(zip(data['lease_type'].unique(), data['lease_type_e'].unique()))
facing_dict=dict(zip(data['facing'].unique(), data['facing_e'].unique()))

#setting page title
st.set_page_config(page_title='Rent Prediction', page_icon=':bar_chart:', layout='wide')
st.title((":red[_Rent Predictor_]"))

#creating columns for input featutes 
col1, col2, col3, col4 = st.columns(4)

with col1:
    type_key=st.selectbox('Flat type',options=type_dict)
with col2:
    lease_type_key=st.selectbox('Lease Type',options=lease_type_dict)
with col3:
    facing_key=st.selectbox('Facing',options=facing_dict)
with col4:
    gym=st.selectbox('1 for gym,0 for no gym',options=[0,1])
with col1:
    property_size=st.number_input('Flat size',value=0)
with col2:
    bathroom=st.number_input('no of bathrooms',value=0)
with col3:
    total_floor=st.number_input('Total floor',value=0)
with col4:
    balcony=st.number_input('balcony',value=0)

#loading the model
def model():
    with open("C:\\Users\\devli\\cf projects\\rent\\linear.pkl","rb") as files:
        model=pickle.load(files)
    return model
#creating a predict function
def predict(model, a, b, c, d, e, f, g, h):
    pred_value = model.predict([[a, b, c, d, e, f, g, h]])
    return pred_value

#creating a pedict button
if st.button('Predict Rent'):
    
    
    type=type_dict[type_key]
    lease_type=lease_type_dict[lease_type_key]
    facing=facing_dict[facing_key]

    pred=predict(model(),type,lease_type,facing,gym,property_size,
                 bathroom,total_floor,balcony)
    
    st.success(f'Predicted Rent: RS {pred[0]:,.2f}')
##creating a sidebar
with st.sidebar:
     st.title(":red[_Rent Predictor_]")
     st.divider()
     st.caption('''This Streamlit app allows users to predict the rent of a flat 
                by selecting different parameters based on requirement ''')
     st.caption("This App is created as a part of GUVI Master Data Science Program")
     st.caption("This app is created by Joel Gracelin")
     st.write("[Ghithub](https://github.com/Joel717)") 
    