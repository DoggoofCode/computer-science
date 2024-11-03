import streamlit as st
from TrajectoryCalculator.TrajectoryCalculation import TrajectoryPropertyFuncs

class SingleSolve:
    @classmethod
    def Run(cls):
        # Gives a title to the page / tabs
        st.title("Single Solver")
        max_height_tab, time_of_flight_tab, horizontal_range_tab =  st.tabs(
            ["Maximum Height", "Time of Flight", "Horizontal Range"]
        )

        # Tab 1: Maximum Height
        with max_height_tab:
            # Creates a 2 columns (inline) for the input
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

            # Out of line, the gravitational acceleration is set
            gravitational_acceleration = st.number_input(
                "(Advanced) Input gravitational acceleration (m/s²)",
                min_value=0.01,
                value=9.8,
                key="max_height_gravitational_acceleration"
            )

            # Button to calculate the answer
            if st.button("Calculate Maximum Height"):
                # Creates a border around the answer
                answer_container = st.container(border=True)
                with answer_container:
                    # Display the answer
                    st.write(
                        f"The Maximum Height is {
                            TrajectoryPropertyFuncs.MaximumHeight(
                                release_velocity,
                                release_angle,
                                gravitational_acceleration
                            ):.2f}"
                        f" meters")

        # Tab 2: Time of Flight
        with time_of_flight_tab:
            # Creates a 2 columns (inline) for the input
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

            # Button to calculate the answer
            if st.button("Calculate Time of Flight"):
                answer_container = st.container(border=True)
                with answer_container:
                    # Writes the answer, calls the function and formats the answer
                    st.write(
                        f"The time of flight is {TrajectoryPropertyFuncs.TimeOfFlight(
                            release_velocity,
                            release_angle,
                            gravitational_acceleration
                        ):.2f}"
                        f" seconds"
                    )

        # Tab 3: Horizontal Range
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
