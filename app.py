import streamlit as st
from streamlit_option_menu import option_menu

from views import (
    ciu_analysis,
    data_upload,
    spend_impact
)
from views.ai_recommendation import home_page
from views.clustering_analysis import cluster_analysis_page

st.set_page_config(page_title="Data Analyser", page_icon=":bar_chart:", layout="wide")


with st.sidebar:
    st.title("Data Analyser")
    st.write("Select a page to navigate:")
    page = option_menu(
        menu_title=None,
        options=["Data Upload", 'CIU Analysis', "Spend Impact", "AI Recommendation", "Clustering Analysis"], 
        icons=['cloud-upload', 'bar-chart', 'bag', 'robot', 'search'],
        menu_icon="list", default_index=0
    )

if page == "Data Upload":
    data_upload.main()
elif page == "CIU Analysis":
    ciu_analysis.main()
elif page == "Spend Impact":
    spend_impact.main()
elif page == "AI Recommendation":
    home_page.main()
elif page == "Clustering Analysis":
    cluster_analysis_page.main()
else:
    st.error("Page not found. Please select a valid page from the sidebar.")
