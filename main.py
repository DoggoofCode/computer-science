import streamlit as st
import numpy as np

def degrees_to_radians(degrees):
    return degrees * np.pi / 180

class TrajectoryPropertyFuncs:
    @classmethod
    def MaximumHeight(cls, release_velocity, release_angle, gravitational_acceleration):
        release_angle = degrees_to_radians(release_angle)
        return (release_velocity ** 2) * (np.sin(release_angle)**2) / 2*gravitational_acceleration

    @classmethod
    def TimeOfFlight(cls, release_velocity, release_angle, gravitational_acceleration):
        release_angle = degrees_to_radians(release_angle)
        return (2 * release_velocity * np.sin(release_angle)) / gravitational_acceleration

    @classmethod
    def HorizontalRange(cls, release_velocity, release_angle, gravitational_acceleration):
        release_angle = degrees_to_radians(release_angle)
        return (release_velocity ** 2) * np.sin(2 * release_angle) / gravitational_acceleration

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

class SingleSolve:
    @classmethod
    def Run(cls):
        st.title("Single Solver")
        max_height_tab, time_of_flight_tab, horizontal_range_tab =  st.tabs(
            ["Maximum Height", "Time of Flight", "Horizontal Range"]
        )
        with max_height_tab:
            column1, column2 = st.columns(2)
            with column1:
                release_velocity = st.number_input(
                    "Please input the release velocity (m/s)",
                    step=0.01,
                    value=10.0,
                    key="max_height_release_velocity"
                )
            with column2:
                release_angle = st.number_input(
                    "Please input the release angle (º)",
                    min_value=0.01,
                    max_value=89.99,
                    step=0.01,
                    value=45.0,
                    key="max_height_release_angle"
                )
            gravitational_acceleration = st.number_input(
                "(Advanced) Input gravitational acceleration (m/s²)",
                min_value=0.01,
                value=9.8,
                key="max_height_gravitational_acceleration"
            )

            if st.button("Calculate Maximum Height"):
                answer_container = st.container(border=True)
                with answer_container:
                    st.write(
                        f"The Maximum Height is {
                            TrajectoryPropertyFuncs.MaximumHeight(
                                release_velocity,
                                release_angle,
                                gravitational_acceleration
                            ):.2f}"
                        f" meters")

        with time_of_flight_tab:
            column1, column2 = st.columns(2)
            with column1:
                release_velocity = st.number_input(
                    "Please input the release velocity (m/s)",
                    step=0.01,
                    value=10.0,
                    key="time_of_flight_release_velocity"
                )
            with column2:
                release_angle = st.number_input(
                    "Please input the release angle (º)",
                    min_value=0.01,
                    max_value=89.99,
                    step=0.01,
                    value=45.0,
                    key="time_of_flight_release_angle"
                )
            gravitational_acceleration = st.number_input(
                "(Advanced) Input gravitational acceleration (m/s²)",
                min_value=0.01,
                value=9.8,
                key="time_of_flight_gravitational_acceleration"
            )

            if st.button("Calculate Time of Flight"):
                answer_container = st.container(border=True)
                with answer_container:
                    st.write(
                        f"The time of flight is {TrajectoryPropertyFuncs.TimeOfFlight(
                            release_velocity,
                            release_angle,
                            gravitational_acceleration
                        ):.2f}"
                        f" seconds"
                    )

        with horizontal_range_tab:
            column1, column2 = st.columns(2)
            with column1:
                release_velocity = st.number_input(
                    "Please input the release velocity (m/s)",
                    step=0.01,
                    value=10.0,
                    key="horizontal_range_release_velocity"
                )
            with column2:
                release_angle = st.number_input(
                    "Please input the release angle (º)",
                    min_value=0.01,
                    max_value=89.99,
                    step=0.01,
                    value=45.0,
                    key="horizontal_range_release_angle"
                )
            gravitational_acceleration = st.number_input(
                "(Advanced) Input gravitational acceleration (m/s²)",
                min_value=0.01,
                value=9.8,
                key="horizontal_range_gravitational_acceleration"
            )

            if st.button("Calculate Horizontal Range"):
                answer_container = st.container(border=True)
                with answer_container:
                    st.write(f"The horizontal range is {TrajectoryPropertyFuncs.HorizontalRange(
                        release_velocity,
                        release_angle,
                        gravitational_acceleration
                    ):.2f} meters")

class FullSolve:
    @classmethod
    def Run(cls):
        st.title("Full Solver")

        column1, column2 = st.columns(2)
        with column1:
            release_velocity = st.number_input(
                "Please input the release velocity (m/s)",
                step=0.01,
                value=10.0,
                key="full_solver_release_velocity"
            )
        with column2:
            release_angle = st.number_input(
                "Please input the release angle (º)",
                min_value=0.01,
                max_value=89.99,
                step=0.01,
                value=45.0,
                key="full_solver_release_angle"
            )
        gravitational_acceleration = st.number_input(
            "(Advanced) Input gravitational acceleration (m/s²)",
            min_value=0.01,
            value=9.8,
            key="full_solver_gravitational_acceleration"
        )


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