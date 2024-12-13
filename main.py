import cv2
import numpy as np
import pygame
import random

# Function to compute epipolar line from the Fundamental Matrix
def calculate_epipolar_line(F, point):
    return np.dot(F, point)  # l' = F * p

# Function to render an epipolar line on the image
def get_epipolar_line(line, x_start, x_end, image_y_start, image_y_end, color):
    a, b, c = line
    
    # Handle vertical lines
    if abs(b) < 1e-6:
        x = -c / a
        return [(x, image_y_start), (x, image_y_end)], color

    y_start = -(a * x_start + c) / b
    y_end = -(a * x_end + c) / b

    # Clamp y-values to the image boundaries
    y_start = max(image_y_start, min(image_y_end, y_start))
    y_end = max(image_y_start, min(image_y_end, y_end))

    return [(x_start, y_start), (x_end, y_end)], color

# Generate random colors for visualization
def get_random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

# Initialize pygame for visualization
pygame.init()
screen_width, screen_height = 1600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Epipolar Geometry with Stereo Cameras")

# Precomputed calibration parameters
K = np.array([[700, 0, 320],
              [0, 700, 240],
              [0, 0, 1]])

F = np.array([[0, -0.001, 0.01],
              [0.002, 0, -0.05],
              [-0.01, 0.05, 0]])

# Open stereo cameras
left_camera = cv2.VideoCapture(1)
right_camera = cv2.VideoCapture(1)

if not left_camera.isOpened() or not right_camera.isOpened():
    print("Error: Unable to open stereo cameras")
    exit()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Capture frames from both cameras
    ret_left, left_frame = left_camera.read()
    ret_right, right_frame = right_camera.read()

    if not ret_left or not ret_right:
        print("Error: Failed to capture frames")
        break

    # Convert frames to grayscale for feature detection
    gray_left = cv2.cvtColor(left_frame, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(right_frame, cv2.COLOR_BGR2GRAY)

    # Detect features using ORB
    orb = cv2.ORB_create()
    keypoints_left, descriptors_left = orb.detectAndCompute(gray_left, None)
    keypoints_right, descriptors_right = orb.detectAndCompute(gray_right, None)

    # Match features between left and right images
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors_left, descriptors_right)

    # Sort matches by distance
    matches = sorted(matches, key=lambda x: x.distance)

    # Visualize matches using OpenCV (debugging purposes)
    matches_image = cv2.drawMatches(left_frame, keypoints_left, right_frame, keypoints_right, matches, None)
    cv2.imshow("Feature Matches", matches_image)

    # Compute epipolar lines for matched points
    left_epipolar_lines = []
    right_epipolar_lines = []
    for match in matches:
        left_point = np.array([*keypoints_left[match.queryIdx].pt, 1.0])
        right_point = np.array([*keypoints_right[match.trainIdx].pt, 1.0])

        epipolar_line_left = calculate_epipolar_line(F.T, right_point)
        epipolar_line_right = calculate_epipolar_line(F, left_point)

        color = get_random_color()
        left_epipolar_lines.append(get_epipolar_line(epipolar_line_left, 0, 400, 0, 600, color))
        right_epipolar_lines.append(get_epipolar_line(epipolar_line_right, 400, 800, 0, 600, color))

    # Render frames in pygame
    screen.fill((255, 255, 255))

    for line, color in left_epipolar_lines:
        pygame.draw.line(screen, color, line[0], line[1], 2)

    for line, color in right_epipolar_lines:
        pygame.draw.line(screen, color, line[0], line[1], 2)

    pygame.display.flip()
    clock.tick(30)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
left_camera.release()
right_camera.release()
cv2.destroyAllWindows()
pygame.quit()
