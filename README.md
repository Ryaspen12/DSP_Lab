# DSP Lab

A hands-on Python laboratory for developing practical digital signal processing skills through simulation, filter design, signal analysis, and validation.

The goal is not just to learn DSP formulas, but to develop the ability to **design, characterize, and defend signal-processing decisions** in engineering and physiological signal-processing applications.

---

## Objectives

This lab focuses on:

* Sampling, Nyquist, and aliasing
* Time-domain and frequency-domain analysis
* FFT and spectral interpretation
* Convolution and LTI systems
* FIR and IIR filter design
* Magnitude and phase response
* Group delay and latency
* Poles, zeros, and filter stability
* Notch filtering and interference rejection
* Physiological signal preprocessing
* Event/activation detection
* Signal quality and SNR
* Filter validation and engineering tradeoffs
* Real-time vs. offline processing

The emphasis throughout the lab is:

> **Characterize the signal → define the requirement → choose the simplest appropriate method → quantify tradeoffs → validate the result.**

---

## Why This Lab?

Digital signal processing is often taught as a collection of equations and filter types. In practice, the important engineering questions are different:

* What information is actually contained in the signal?
* What noise or artifacts are present?
* What frequencies matter?
* How much attenuation is required?
* How much latency can the system tolerate?
* Does phase distortion matter?
* Is real-time processing required?
* How much computational complexity is acceptable?
* Does the processing change the physiological measurement?
* How do we demonstrate that the algorithm works?

This lab is designed around those questions.

---

# Repository Structure

```text
DSP_Lab/
│
├── README.md
│
├── notebooks/
│   ├── 01_sampling_aliasing.ipynb
│   ├── 02_fft_frequency_analysis.ipynb
│   ├── 03_convolution_lti.ipynb
│   ├── 04_fir_vs_iir.ipynb
│   ├── 05_filter_design.ipynb
│   ├── 06_frequency_phase_group_delay.ipynb
│   ├── 07_notch_filter.ipynb
│   ├── 08_physiological_signal_filtering.ipynb
│   └── 09_filter_validation.ipynb
│
├── src/
│   ├── signals.py
│   ├── filters.py
│   └── analysis.py
│
├── figures/
│
└── data/
    └── simulated/
```

The first several experiments can remain entirely inside notebooks. Functions should be moved into `src/` once patterns begin repeating.

---

# Environment

Recommended Python packages:

```text
numpy
scipy
matplotlib
pandas
jupyter
```

Optional:

```text
scikit-learn
```

Create a virtual environment and install the dependencies before beginning the experiments.

---

# Experiments

## 01 — Sampling, Nyquist, and Aliasing

### Goal

Develop an intuitive understanding of sampling and aliasing.

### Tasks

1. Generate continuous/high-resolution sinusoidal signals.
2. Sample them at different sampling rates.
3. Compare signals below and above the Nyquist frequency.
4. Demonstrate aliasing.
5. Show how different frequencies can produce the same sampled representation.
6. Examine the FFT of sampled signals.

### Questions

* What determines the Nyquist frequency?
* Why can't frequencies above Nyquist simply be "ignored"?
* What role does the analog anti-aliasing filter play?
* Why might a real system sample substantially above the minimum theoretical rate?

---

# 02 — FFT and Frequency Analysis

### Goal

Understand how frequency-domain analysis can be used to characterize signals.

### Tasks

1. Generate single-frequency sinusoids.
2. Generate multi-frequency signals.
3. Add white and colored noise.
4. Compute the FFT.
5. Plot magnitude spectra.
6. Investigate spectral leakage.
7. Investigate the effect of observation length.
8. Examine frequency resolution.

### Questions

* What does an FFT magnitude peak represent?
* How does sampling frequency affect the frequency axis?
* How does record length affect frequency resolution?
* Why does a sinusoid sometimes appear spread across multiple FFT bins?

---

# 03 — Convolution and LTI Systems

### Goal

Build intuition for convolution and linear time-invariant systems.

### Tasks

1. Create an impulse signal.
2. Create simple FIR filters.
3. Perform convolution manually.
4. Compare manual convolution with `scipy.signal`.
5. Examine the impulse response.
6. Pass sinusoids through the system.
7. Build a composite signal and observe filtering.

### Questions

* What does the impulse response tell us about an LTI system?
* Why does convolution implement filtering?
* Why does a sinusoid remain at the same frequency when passed through an LTI system?
* How are convolution and multiplication in the frequency domain related?

---

# 04 — FIR vs. IIR

### Goal

Understand the practical differences between FIR and IIR implementations.

### Tasks

Design filters with comparable frequency-domain requirements using:

* FIR
* IIR

Compare:

* Filter order
* Number of coefficients
* Magnitude response
* Phase response
* Group delay
* Computational requirements
* Stability
* Transient behavior

### Questions

* Why can an IIR achieve a sharp response with relatively low order?
* Why can an FIR provide exact linear phase?
* Why doesn't "FIR" automatically mean "better"?
* When might an IIR be preferable in a real-time system?
* When might an FIR be preferable?

---

# 05 — Filter Design

### Goal

Learn to translate signal requirements into filter specifications.

### Filter Types

Explore:

* Low-pass
* High-pass
* Band-pass
* Band-stop
* Notch

### Filter Families

Compare:

* Butterworth
* Chebyshev Type I
* Chebyshev Type II
* Elliptic
* Bessel

### Tasks

For each filter, investigate:

* Passband edge
* Stopband edge
* Transition bandwidth
* Passband ripple
* Stopband attenuation
* Filter order
* Magnitude response
* Phase response

### Questions

* What determines filter order?
* Why does a narrower transition band generally require a higher-order filter?
* What is the difference between cutoff frequency and transition bandwidth?
* What tradeoff does each filter family make?

---

# 06 — Frequency Response, Phase, and Group Delay

### Goal

Learn to characterize the timing behavior of a filter.

For a filter with frequency response:

$$
H(e^{j\omega})
$$

characterize:

### Magnitude

$$
|H(e^{j\omega})|
$$

### Phase

$$
\phi(\omega)=\angle H(e^{j\omega})
$$

### Group Delay

$$
\tau_g(\omega)
=
-\frac{d\phi(\omega)}{d\omega}
$$

### Tasks

For both FIR and IIR filters:

1. Plot magnitude response.
2. Plot phase response.
3. Plot group delay.
4. Compare linear-phase and nonlinear-phase behavior.
5. Pass a transient/physiological-like waveform through each filter.
6. Measure changes in waveform morphology and event timing.

### Key Question

> Is the filter merely delaying the signal, or is it changing the relative timing of its frequency components?

---

# 07 — 60-Hz Notch Filter

### Goal

Design and characterize a filter for power-line interference.

Assume:

```text
Sampling frequency = 1000 Hz
Interference = 60 Hz
```

### Tasks

1. Calculate the normalized digital frequency.
2. Determine the corresponding angle on the unit circle.
3. Design a notch filter.
4. Inspect its zeros and poles.
5. Plot magnitude response.
6. Plot phase response.
7. Plot group delay.
8. Vary the pole radius.
9. Observe how pole radius affects notch width and selectivity.
10. Test the filter on a signal containing 60-Hz interference.

### Questions

* Why are zeros placed at ±60 Hz?
* Why are the poles placed nearby?
* What does pole radius control?
* What happens as the poles approach the unit circle?
* How does the notch affect nearby physiological frequencies?
* Is a narrow notch always preferable?

---

# 08 — Physiological Signal Filtering

### Goal

Apply DSP concepts to realistic physiological-like signals.

Create a simulated signal containing:

* Physiological information
* Baseline drift
* Broadband noise
* 60-Hz interference
* Transient events

### Example Pipeline

```text
Raw signal
    ↓
Signal characterization
    ↓
Noise characterization
    ↓
Filtering
    ↓
Event detection
    ↓
Measurement
    ↓
Validation
```

Compare several approaches:

* FIR
* IIR
* Different filter orders
* Different cutoff frequencies
* Notch vs. no notch
* Causal vs. zero-phase filtering

### Measure

* SNR
* Residual interference
* Peak amplitude
* Event timing
* Event duration
* Morphology
* False detections
* Missed detections
* Computational cost
* Latency

---

# 09 — Filter Validation

### Goal

Develop a complete engineering validation methodology.

A filter should not be considered successful simply because its frequency response "looks good."

Evaluate three levels.

## Filter-Level Validation

Measure:

* Magnitude response
* Phase response
* Group delay
* Impulse response
* Stability
* Numerical behavior

## Signal-Level Validation

Measure:

* SNR improvement
* Noise suppression
* Signal morphology
* Peak timing
* Activation timing
* Event duration
* Detection performance

## Requirement-Level Validation

Ask:

> Does the resulting system satisfy the actual engineering/clinical requirements?

Examples:

```text
Maximum allowable timing error
Maximum allowable latency
Minimum required attenuation
Maximum passband distortion
Required detection sensitivity
Required computational budget
```

---

# Capstone Experiment

## Real-Time IIR vs. Linear-Phase FIR

Build a simulated physiological signal containing meaningful transient events and 60-Hz interference.

Design:

### Filter A

A linear-phase FIR filter.

### Filter B

A low-order IIR filter.

Attempt to achieve approximately comparable magnitude responses.

Then compare:

```text
                    FIR          IIR
------------------------------------------------
Filter order
Coefficient count
Magnitude response
Phase response
Group delay
Latency
Computational cost
Stability
Morphology change
Timing error
```

### Central Engineering Question

> **If the IIR provides adequate noise rejection but introduces nonlinear phase, when is that tradeoff acceptable?**

Do not assume that either implementation is inherently superior.

Instead, determine whether each satisfies the system requirements.

---

# Medical Signal Processing Lens

Throughout the lab, keep asking:

### Signal

What information are we trying to preserve?

### Noise

What are we trying to remove?

### Timing

Does processing change when an event appears to occur?

### Morphology

Does processing change the shape of the physiological waveform?

### Latency

How quickly can the system produce a usable result?

### Robustness

Does performance remain acceptable across different signal qualities and operating conditions?

### Validation

How do we demonstrate that the algorithm works?

### Deployment

Can the algorithm actually run reliably on the intended hardware/software platform?

---

# Core Equations

### Sampling

$$
f_N = \frac{f_s}{2}
$$

### Digital frequency

$$
\omega = 2\pi\frac{f}{f_s}
$$

### Convolution

$$
y[n] = x[n]*h[n]
$$

$$
y[n] = \sum_k x[k]h[n-k]
$$

### Frequency-domain filtering

$$
Y(e^{j\omega})
=
X(e^{j\omega})H(e^{j\omega})
$$

### Magnitude

$$
|H(e^{j\omega})|
$$

### Phase

$$
\phi(\omega)=\angle H(e^{j\omega})
$$

### Group delay

$$
\tau_g(\omega)
=
-\frac{d\phi(\omega)}{d\omega}
$$

### FIR

$$
y[n]
=
\sum_{k=0}^{N}b_kx[n-k]
$$

### IIR

$$
y[n]
=
\sum_{k=0}^{M}b_kx[n-k]
-
\sum_{k=1}^{N}a_ky[n-k]
$$

### dB Magnitude

$$
20\log_{10}|H(e^{j\omega})|
$$

---

# Interview Practice

Each experiment should finish with a few questions that could plausibly appear in a technical interview.

For every major design decision, be able to answer:

1. **What did you choose?**
2. **Why did you choose it?**
3. **What alternatives did you consider?**
4. **What tradeoffs did you make?**
5. **How did you characterize the result?**
6. **What could go wrong?**
7. **How would you validate it?**
8. **What requirement determines whether the result is acceptable?**

The goal is to progress from:

> "I know what a Butterworth filter is."

to:

> "Given this signal and these requirements, I can justify a filter architecture, quantify its frequency and timing behavior, identify failure modes, and design a validation strategy."

---

# Guiding Principle

**Don't just make the signal look cleaner.**

Understand:

> **What information is in the signal, what information can be sacrificed, what artifacts are present, and whether the processing preserves the measurement that the system actually cares about.**
