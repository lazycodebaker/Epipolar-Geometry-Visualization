# Epipolar Geometry Visualization

This project demonstrates epipolar geometry in stereo vision using Python. It visualizes epipolar lines for feature matches between two stereo camera frames and uses pygame for real-time rendering. The system also integrates feature detection, matching, and visualization with OpenCV and pygame.

---

## Features

- **Stereo Camera Integration**: Captures frames from left and right cameras in real-time.
- **Feature Detection**: Uses ORB (Oriented FAST and Rotated BRIEF) for feature detection and matching.
- **Epipolar Line Visualization**: Computes and visualizes epipolar lines for matched points using the fundamental matrix.
- **Real-Time Rendering**: Utilizes pygame to render epipolar lines dynamically.
- **Debugging Utility**: Displays feature matches using OpenCV for debugging purposes.

---

## Prerequisites

### Libraries
Make sure you have the following Python libraries installed:

- OpenCV (`cv2`)
- NumPy (`numpy`)
- pygame

You can install them via pip:

```bash
pip install opencv-python-headless numpy pygame
```

---

## How to Run

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Prepare Your Environment

Ensure you have two connected cameras (stereo setup) for real-time frame capture.

### 3. Run the Script

Execute the Python script:

```bash
python epipolar_visualization.py
```

### 4. Visual Output

- The pygame window will display epipolar lines for matched features.
- A separate OpenCV window will show the feature matches between the left and right frames.

### 5. Exit

- Close the pygame window or press the `q` key in the OpenCV window to terminate the program.

---

## Code Explanation

### Key Components

1. **Fundamental Matrix (F):**
   The script uses a precomputed fundamental matrix (`F`) to compute epipolar lines.

2. **Feature Matching:**
   - Detects features using ORB.
   - Matches features between left and right frames using the BFMatcher.

3. **Epipolar Line Calculation:**
   - Computes epipolar lines from matched points using the fundamental matrix.

4. **Visualization:**
   - Uses pygame to render epipolar lines on a blank canvas.
   - Debugging visualization is done with OpenCV.

### Main Functions

- **`calculate_epipolar_line(F, point)`**:
  Computes the epipolar line from the given fundamental matrix and a point.

- **`get_epipolar_line(line, x_start, x_end, image_y_start, image_y_end, color)`**:
  Returns the endpoints of an epipolar line and its associated color for rendering.

- **`get_random_color()`**:
  Generates a random RGB color for visualizing each epipolar line.

---

## Known Issues

- Ensure that both cameras are properly connected. The program will terminate if the cameras fail to initialize.
- Limited to stereo camera setups; requires further customization for other configurations.

---

## Future Improvements

- Dynamically compute the fundamental matrix using calibration data.
- Add support for other feature detection methods (e.g., SIFT, SURF).
- Enhance visualization by overlaying lines on actual images instead of a blank canvas.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

---

## Author

Developed by [Your Name](https://github.com/your-github-profile).

---

## Acknowledgments

- OpenCV for computer vision capabilities
- pygame for real-time rendering
- NumPy for matrix operations

