## Eye Blink Counter using OpenCV and Webcam

This project is a simple Python application that utilizes the OpenCV library to detect eye blinks in real-time using a webcam feed. It counts the number of blinks that occur while the program is running.

## Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy


## Usage

1. Navigate to the project directory:

    ```
    cd Eye-Blink-Counter
    ```

2. Run the Python script:

    ```
    python Blink.py
    ```

3. A window will open displaying the webcam feed. The program will continuously monitor for eye blinks and display the count in the terminal.

4. To exit the program, press the 'q' key.

## How it Works

The program uses the Haar Cascade classifier provided by OpenCV to detect faces in the webcam feed. Once a face is detected, it then uses a pre-trained eye cascade classifier to detect eyes within the face region.

By tracking changes in the aspect ratio of the eyes (e.g., blinking), the program counts the number of blinks that occur over time.

## Contributors

- Niranjanaa Manoj(https://github.com/NiranManoj)



---

