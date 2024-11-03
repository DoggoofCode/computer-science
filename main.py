import streamlit as st
from TrajectoryCalculator import TitlePage, SingleSolve, FullSolve


def main():
    # Sets Essential Page Configuration (wide-screen mode)
    st.set_page_config(
        page_title="Trajectory Calculator",
        layout="wide"
    )

    # Adds a title to the Sidebar
    st.sidebar.title("Model Selection")

    # Adds a selection box to the Sidebar
    page_selection = st.sidebar.selectbox(
        "Select a page:",
        [
            "Title Page",
            "Single Solve",
            "Full Solve",
        ]
    )

    # Runs the selected page
    if page_selection == "Title Page":
        TitlePage.Run()
    elif page_selection == "Single Solve":
        SingleSolve.Run()
    elif page_selection == "Full Solve":
        FullSolve.Run()


if __name__ == '__main__':
    main()