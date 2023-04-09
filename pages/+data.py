import streamlit as st
from PIL import Image
from app import *

st.markdown("# +data")
st.sidebar.markdown("# +data")


st.write('Podrás observar que hay datos que no son muy coherentes... por ejemplo, si colocamos los datos de una persona que posee altos ingresos (máximo) y el monto es el mìnimo posible, el modelo infiere que tendrá probelmas en abonar su préstamo. A continuación un análisis que se hizo de manera previa, donde se observan casos de este tipo en los datos que brindaron para entrenamiento')


image = Image.open('images/graf1.png')

st.image(image, caption='Graf1')

st.write('Entendi que es valioso dejar estos casos y no considerarlos outsiders ni tampoco balancear discrecionalmente la cantidad de casos, dado que se considera informacioón valiosa para el caso puntual')

author()