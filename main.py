import streamlit as st
import numpy as np

class TitlePage:
    @classmethod
    def Run(cls):
        pass

class SingleSolve:
    @classmethod
    def Run(cls):
        pass

class FullSolve:
    @classmethod
    def Run(cls):
        pass

def main():
    # Adds a title to the Sidebar
    st.sidebar.title("Model Selection")

    # Adds a selection box to the Sidebar
    model_selection = st.sidebar.selectbox(
        "Select a page:",
        [
            "Title Page",
            "Single Solve",
            "Full Solve",
        ]
    )
    if model_selection == "Title Page":
        TitlePage.Run()
    elif model_selection == "Single Solve":
        SingleSolve.Run()
    elif model_selection == "Full Solve":
        FullSolve.Run()


if __name__ == '__main__':
    main()