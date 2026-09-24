# CGM Algorithm Pipeline

A simulated end-to-end continuous glucose monitoring (CGM) signal-processing pipeline designed to explore practical challenges in biomedical sensor algorithm development.

## Objective

Build and evaluate a processing pipeline that converts an imperfect simulated sensor signal into a glucose estimate while accounting for realistic sensor behavior, including noise, physiological dynamics, latency, drift, and signal artifacts.

The project focuses on the general algorithm-development and validation challenges encountered when working with continuous biomedical sensor data.

## Pipeline

```text
Ground Truth Glucose
        ↓
Physiological Dynamics
        ↓
Simulated Sensor Response
        ↓
Noise / Drift / Artifacts
        ↓
Preprocessing
        ↓
Filtering
        ↓
Calibration
        ↓
Glucose Estimate
        ↓
Validation & Error Analysis
```

## Planned Experiments

1. **Signal Simulation**

   * Generate realistic glucose trajectories
   * Simulate meals, exercise, and glucose transitions
   * Model sensor dynamics and physiological lag

2. **Sensor Processing**

   * Add measurement noise
   * Simulate baseline drift and sensor aging
   * Introduce artifacts and missing data

3. **Filtering**

   * Compare moving-average, FIR, and IIR approaches
   * Evaluate noise reduction versus latency
   * Examine phase and group-delay effects

4. **Calibration**

   * Develop a simple sensor-to-glucose calibration model
   * Investigate sensor-to-sensor variability
   * Explore calibration drift over sensor lifetime

5. **Validation**

   * Compare estimated glucose against known ground truth
   * Evaluate MAE, RMSE, bias, and MARD
   * Analyze error by glucose level, rate of change, and sensor age
   * Compare algorithm performance across simulated sensors

6. **Robustness & Testing**

   * Handle missing samples, NaNs, dropouts, and artifacts
   * Implement signal-quality checks
   * Develop unit and integration tests for pipeline components


*This project uses simulated data to demonstrate signal-processing, algorithm-development, and validation concepts rather than reproducing a proprietary CGM algorithm.*
