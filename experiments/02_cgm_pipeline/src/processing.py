"""
Sensor-processing functions for the synthetic CGM pipeline.
"""

import numpy as np


def simulate_sensor_lag(
    glucose: np.ndarray,
    alpha: float = 0.2,
) -> np.ndarray:
    """
    Simulate a first-order sensor response to glucose.

    Parameters
    ----------
    glucose : np.ndarray
        Ground-truth glucose signal.
    alpha : float
        Sensor response coefficient. Smaller values produce
        greater smoothing and latency.

    Returns
    -------
    np.ndarray
        Simulated sensor signal.
    """
    sensor = np.zeros_like(glucose, dtype=float)

    sensor[0] = glucose[0]

    for i in range(1, len(glucose)):
        sensor[i] = (
            sensor[i - 1]
            + alpha * (glucose[i] - sensor[i - 1])
        )

    return sensor

def add_sensor_noise(
    sensor: np.ndarray,
    noise_std: float = 3.0,
    random_seed: int | None = 42,
) -> np.ndarray:
    """
    Add Gaussian measurement noise to a sensor signal.

    Parameters
    ----------
    sensor : np.ndarray
        Sensor signal.
    noise_std : float
        Standard deviation of measurement noise in mg/dL.
    random_seed : int or None
        Seed for reproducible noise.

    Returns
    -------
    np.ndarray
        Sensor signal with added measurement noise.
    """
    rng = np.random.default_rng(random_seed)

    noise = rng.normal(
        loc=0.0,
        scale=noise_std,
        size=len(sensor),
    )

    return sensor + noise

def add_sensor_drift(
    sensor: np.ndarray,
    sampling_interval_minutes: float = 5.0,
    drift_rate: float = 0.5,
) -> np.ndarray:
    """
    Add a slowly varying baseline drift to a sensor signal.

    Parameters
    ----------
    sensor : np.ndarray
        Sensor signal.
    sampling_interval_minutes : float
        Time between samples in minutes.
    drift_rate : float
        Drift in mg/dL per hour.

    Returns
    -------
    np.ndarray
        Sensor signal with added drift.
    """
    time_hours = (
        np.arange(len(sensor))
        * sampling_interval_minutes
        / 60
    )

    drift = drift_rate * time_hours

    return sensor + drift

def simulate_raw_sensor(
    glucose: np.ndarray,
    alpha: float = 0.2,
    noise_std: float = 3.0,
    sampling_interval_minutes: float = 5.0,
    drift_rate: float = 0.5,
    random_seed: int | None = 42,
) -> np.ndarray:
    """
    Simulate a raw CGM sensor measurement.

    Applies sensor dynamics, measurement noise, and baseline drift
    to an underlying glucose signal.

    Parameters
    ----------
    glucose : np.ndarray
        Ground-truth glucose signal.
    alpha : float
        Sensor response coefficient.
    noise_std : float
        Standard deviation of measurement noise in mg/dL.
    sampling_interval_minutes : float
        Sensor sampling interval.
    drift_rate : float
        Baseline drift in mg/dL per hour.
    random_seed : int or None
        Seed for reproducible noise.

    Returns
    -------
    np.ndarray
        Simulated raw sensor signal.
    """
    sensor = simulate_sensor_lag(
        glucose,
        alpha=alpha,
    )

    sensor = add_sensor_noise(
        sensor,
        noise_std=noise_std,
        random_seed=random_seed,
    )

    sensor = add_sensor_drift(
        sensor,
        sampling_interval_minutes=sampling_interval_minutes,
        drift_rate=drift_rate,
    )

    return sensor


def moving_average(
    signal: np.ndarray,
    window_size: int,
) -> np.ndarray:

    filtered = np.zeros_like(signal, dtype=float)

    half_window = window_size // 2

    for i in range(len(signal)):
        start = max(0, i-half_window)
        end = min(len(signal), i+half_window + 1)
        filtered[i] = np.mean(signal[start:end])

    return filtered