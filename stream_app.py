import streamlit as st
from import_embedding import inserttodb, similar_thoughts
import pandas as pd
import matplotlib.pyplot as plt
from utils import compute_pca 


st.header(':blue[How was your day?] :sunglasses:', divider=True)
with st.form("my_form"):
    thought=st.text_area('Enter your thoughts here:', max_chars=512)
    thought = thought.replace("'", "''")
    thought = thought.replace('"', '""')
    submitted = st.form_submit_button("Submit")
    if submitted:
        inserttodb=inserttodb(thought)
        if inserttodb:
            st.write("Your thoughts have been recorded.")
            similar_thoughts = similar_thoughts(thought)
            st.write("You had a similar thought before.")
            thought_table = pd.DataFrame(similar_thoughts, columns=['thought', 'entry_date'])
            st.dataframe(thought_table, hide_index=True, column_order=['entry_date','thought'])
            #make me a pca graph
            pca = compute_pca()
            st.scatter_chart(pca, x='PC1', y='PC2', color='thoughts')