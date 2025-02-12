# Piano_Cam

## Overview
The **Piano Cam** is an interactive application that allows users to play a virtual piano using hand gestures captured via a webcam. Leveraging **MediaPipe Hands** for hand tracking and **OpenCV** for real-time video processing, this project transforms your hand movements into piano notes. Each key on the virtual piano corresponds to a specific note, and when your hand touches a key, the corresponding sound is played using **Pygame**.

This project is a fun and innovative way to explore the intersection of computer vision, machine learning, and music. It’s perfect for beginners and enthusiasts interested in AI, computer vision, or music technology.

## Features
- Real-time hand tracking using MediaPipe Hands.
- Virtual piano with labeled keys (both white and black keys).
- Play piano notes by touching the virtual keys with your hand.
- Full-screen or centered window display options.
- Easy-to-understand code structure for customization.

## How to Run

### Prerequisites
1. Python 3.x installed on your system.
2. A working webcam.
3. Required Python libraries: `opencv-python`, `mediapipe`, `pygame`.

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ritampatra76/Piano_Cam.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd Piano_Cam
   ```
3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project
1. **Run the application**:
   ```bash
   python app.py
   ```
2. Position your hand in front of the webcam and start playing the virtual piano by touching the keys displayed on the screen.

3. Press the `q` key to quit the application.

### Demo Video
Check out the demo video to see the AI Piano Player in action:  
[**demo.mp4**](demo.mp4)

## Customization
- You can modify the piano layout, key positions, or add more notes by editing the `draw_piano` function.
- Replace the sound files in the `piano_notes` dictionary with your own `.wav` files for custom sounds.

## Dependencies
- `opencv-python`
- `mediapipe`
- `pygame`
- `numpy`

## License
This project is open-source. Feel free to use, modify, and distribute it as per the license terms.

---

Enjoy playing the virtual piano with your hands! 🎹✨
