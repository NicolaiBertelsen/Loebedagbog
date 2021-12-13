import streamlit as st
import numpy as np
import pandas as pd
import plotly as pl
import plotly.express as px
from matplotlib import pyplot as plt
import matplotlib as matplotlib

st.set_page_config(page_title="Løbedagbog",
                   page_icon=":runner:",
                   layout="wide")

title = st.title(":running: Løbedagbog :running:")


st.markdown("---")

Navne = ["Nicolai", "Victor", "Mathias", "Jacob", "Oliver"]

Navn_valgt = st.selectbox("Vælg person", Navne)

#Dag = st.select_slider('Vælg en dag (februar)', options=list(range(1, 30)))

# LISTE MED DAGE I FEBRUAR
dage_i_februar = []
feb = ". februar"
for i in range(1, 30):
    dage_i_februar.append(str(i) + feb)
#st.write(dage_i_februar)


Antal_KM = {"Nicolai": [0, 5.23, 8.27, 6.52, 0, 0, 4.76, 8.23, 4.46, 0, 7.55, 0, 6.88, 0, 4.39, 4.42, 0, 4.48, 0, 6.17, 6.11, 6.15, 4.83, 0, 8.20, 0, 5.07, 0, 0],
            "Victor": [5.20, 4.63, 0, 5.80, 0, 9.31, 0, 0, 6.06, 6.29, 0, 8.16, 0, 0, 0, 7.53, 0, 6.17, 5.02, 0, 7.76, 7.07, 0, 8.54, 7.05, 0, 5.54, 0, 0],
            "Mathias": [11.21, 5.33, 0, 9.34, 5.10, 0, 0, 9.56, 0, 9.02, 0, 0, 0, 0, 0, 8.02, 0, 6.18, 0, 0, 13.98, 5.26, 0, 10.32, 0, 8.22, 0, 0, 0],
            "Jacob": [5.30, 9.03, 0, 0, 0, 9.28, 0, 5.05, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            "Oliver": [3, 0, 0, 3.63, 5.22, 9.98, 0, 1.93, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.12, 0, 0]
            }

#st.subheader('Antal kilometer løbet på denne dato ' + "(" + Navn_valgt + ")" + ":")
#st.text(Antal_KM[Navn_valgt][Dag-1])

# DATAFRAME

Navn_df = ["Nicolai", "Victor", "Mathias", "Jacob", "Oliver"]

df = pd.DataFrame(data=Antal_KM, index=dage_i_februar, columns=Navn_df)
#st.subheader("Overblik over løbeforløb")
#st.dataframe(df)

# GRAFER

total_run = sum(Antal_KM[Navn_valgt]) #Finder total antal km for person valgt
total_run = int(total_run) #Laver det til et helt tal

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total antal kilometer løbet i februar")
    st.subheader(total_run)

with middle_column:
    Dag = st.select_slider('Vælg en dag (februar)', options=list(range(1, 30)))
    st.subheader('Antal kilometer løbet på denne dato ' + "(" + Navn_valgt + ")" + ":")
    st.subheader(Antal_KM[Navn_valgt][Dag - 1])

with right_column:
    st.subheader("Overblik over løbeforløb")
    st.dataframe(df)

st.markdown("---")

#FIGURE 1 WITH TOTAL KM RUN ON DIFFERENT DAYS

left_column, right_column = st.columns(2)

with left_column:

    color_list = ["Green", "Red", "Blue", "Purple", "Orange"]

    fig_km_loebet = px.bar(
        df,
        x= df.columns,
        y= df.index,
        orientation="h",
        title="<b>Antal KM fordelt på dage</b>",
        template="plotly_white",
        color_discrete_sequence= color_list,
    )

    fig_km_loebet.update_layout(
        plot_bgcolor= "rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
    )

    st.plotly_chart(fig_km_loebet)

with right_column:

    # LINE GRAPH
    km_loebet = []
    accum = 0
    for w in Antal_KM[Navn_valgt]:
        accum = round(accum + w, 2)
        km_loebet.append(accum)

    fig, ax = plt.subplots()
    ax.plot(range(1, 30), km_loebet)
    plt.title("Løbende udvikling i februar (" + Navn_valgt + ")")
    plt.xlabel("Dage")
    plt.ylabel("Antal Kilometer")
    #ax.set_facecolor("#0083B8")
    fig.patch.set_facecolor("#0083B8") #sætter baggrundsfarven på grafen
    st.pyplot(fig)
# HIDE STREAMLIT STYLE

#hide_st_style = """
    #<style>
    #Mainmenu {visibility: shown;}
    #footer {visibility: hidden;}
    #header {visibility: hidden;}
    #</style>
    #"""
#st.markdown(hide_st_style, unsafe_allow_html=True)
