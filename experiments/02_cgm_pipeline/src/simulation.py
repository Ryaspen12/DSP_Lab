"""
Synthetic CGM signal simulation.

This module generates ground-truth glucose trajectories and will
eventually be extended to simulate sensor dynamics, noise, drift,
artifacts, and other real-world measurement effects.
"""

import numpy as np

def generate_time_vector(
    duration_hours: float = 24.0,
    sampling_interval_minutes: float = 5.0,
) -> np.ndarray:
    """
    Generate a uniformly sampled time vector.

    Parameters
    ----------
    duration_hours : float
        Duration of the simulated signal in hours.
    sampling_interval_minutes : float
        Sampling interval in minutes.

    Returns
    -------
    np.ndarray
        Time vector in minutes.
    """
    duration_minutes = duration_hours * 60

    return np.arange(
        0,
        duration_minutes,
        sampling_interval_minutes,
    )

def generate_glucose_signal(
    time_minutes: np.ndarray,
    baseline: float = 100.0,
    daily_variation: float = 5.0,
    random_seed: int | None = 42,
) -> np.ndarray:
    """
    Generate a synthetic ground-truth glucose trajectory.

    The model includes:
    - Baseline glucose
    - Slow daily variation
    - Meal-related glucose excursions
    - Exercise-related glucose reductions
    - Small stochastic physiological variation

    Parameters
    ----------
    time_minutes : np.ndarray
        Time vector in minutes.
    baseline : float
        Baseline glucose concentration in mg/dL.
    daily_variation : float
        Amplitude of slow daily variation in mg/dL.
    random_seed : int or None
        Seed for reproducible stochastic variation.

    Returns
    -------
    np.ndarray
        Simulated ground-truth glucose concentration in mg/dL.
    """
    rng = np.random.default_rng(random_seed)

    # Slow daily variation
    daily_cycle = daily_variation * np.sin(
        2 * np.pi * time_minutes / (24 * 60)
    )

    glucose = baseline + daily_cycle

    # Meal-related glucose excursions
    meal_times = [8 * 60, 13 * 60, 19 * 60]

    for meal_time in meal_times:
        meal_response = 35 * np.exp(
            -0.5 * ((time_minutes - meal_time) / 60) ** 2
        )

        glucose += meal_response

    # Exercise-related glucose reduction
    exercise_start = 17 * 60
    exercise_duration = 60

    exercise_mask = (
        (time_minutes >= exercise_start)
        & (time_minutes <= exercise_start + exercise_duration)
    )

    glucose[exercise_mask] -= 20

    # Small physiological variability
    physiological_variation = rng.normal(
        loc=0.0,
        scale=1.0,
        size=len(time_minutes),
    )

    glucose += physiological_variation

    return glucose