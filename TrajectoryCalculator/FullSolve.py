import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from TrajectoryCalculator.TrajectoryCalculation import TrajectoryPropertyFuncs

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

        # Solution used as then the slider is used the button is set to false,
        # which hides the answer. This solution is neccessary

        def click_button():
            st.session_state.button = not st.session_state.button

        if 'button' not in st.session_state:
            st.session_state.button = False

        st.button("Calculate", on_click=click_button)

        if st.session_state.button:
            # Adjust / Calculate the values
            time_of_flight = TrajectoryPropertyFuncs.TimeOfFlight(release_velocity, release_angle, gravitational_acceleration)
            max_height = TrajectoryPropertyFuncs.MaximumHeight(release_velocity, release_angle, gravitational_acceleration)
            horizontal_range = TrajectoryPropertyFuncs.HorizontalRange(release_velocity, release_angle, gravitational_acceleration)
            # Create a container for the answer
            answer_container = st.container(border=True)
            with answer_container:
                full_answer_properties, full_answer_graph = st.columns(2)
                with full_answer_properties:
                    # Display the answers
                    st.write(f"The time of flight is {time_of_flight:.2f} seconds")
                    st.write(f"The Maximum Height is {max_height:.2f} meters")
                    st.write(f"The horizontal range is {horizontal_range:.2f} meters")
                with full_answer_graph:
                    # Draws graph of the trajectory

                    # Set the Matplotlib parameters for a black theme
                    plt.style.use('dark_background')

                    # Creates a linspace to draw the Graph
                    # Note → Vega, the inbuilt grapher of Streamlit DOES NOT WORK!
                    x = np.linspace(0, horizontal_range, 100)

                    release_angle = release_angle * np.pi / 180

                    subraction = np.tan(release_angle) * x
                    numerator = (gravitational_acceleration * (x ** 2))
                    denominator = 2 * release_velocity ** 2 * np.cos(release_angle)**2
                    y = (subraction - numerator / denominator) * 100

                    plt.title("Trajectory")
                    plt.plot(x, y)
                    plt.xlabel("Distance (m)")
                    plt.ylabel("Height (m)")
                    st.pyplot(plt)
                full_answer_slider, full_answer_slider_answer = st.columns(2)
                with full_answer_slider:
                    # Creates a slider to the thrown time
                    arc_time_slider = st.slider(
                        "Adjust the angle (º)",
                        min_value=0.,
                        max_value=100.,
                        step=0.01,
                        value = 1.
                    )
                with full_answer_slider_answer:
                    # Calculates the height of the object at the given time
                    adjusted_time = arc_time_slider * release_velocity

                    subraction = np.tan(release_angle) * adjusted_time
                    numerator = (gravitational_acceleration * (adjusted_time ** 2))
                    denominator = 2 * release_velocity ** 2 * np.cos(release_angle) ** 2
                    arc_height = (subraction - numerator / denominator) * 100

                    st.write(f"The height of the object at {arc_time_slider:.2f} seconds is {float(arc_height):.2f} meters")