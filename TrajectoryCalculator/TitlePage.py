import streamlit as st

class TitlePage:
    @classmethod
    def Run(cls):
        # Title
        st.title("Trajectory Calculator")

        # Line Break
        st.divider()

        # Short Description
        st.write(
            "This project aims to help student calculate the trajectory"
            " of an object in a 2 dimensional plane, as well as finding the"
            " trajectories properties"
        )
