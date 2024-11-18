# Automatic YouTube Navigator with Selenium 
This Python project provides a complete solution for automating YouTube interactions and recording both screen and audio during video playback. The script handles pop-ups, performs video searches, applies filters, and adjusts playback settings—all while ensuring high-quality recordings. The project also integrates functionality to merge audio and video, analyze the output, and collect video metadata for further use.

## Features
### YouTube Automation:
- Opens YouTube and handles pop-ups for terms and YouTube Premium
- Searches for a specified term and filters videos based on preference
- Selects a specific video and adjusts playback speed
- Collects the video's metadata like: title, URL, channel, number of subs, etc.
  
### Recording Functionality:
- Records desktop screen activity during video playback at optimal FPS rate
- Records system audio in a high-quality format
  
### Merging and Analysis:
- Merges the recorded video and audio into a single file using FFmpeg
- Analyzes the merged file for audio levels and saves the results
  
### Monitoring and Logging:
- Monitors the internet connection to ensure uninterrupted functionality
- Ensures the browser driver remains responsive
- Logs all actions and errors for easy debugging and analysis

## Prerequisites

### System Requirements
- Python 3.8 or later
- macOS, Linux, or Windows
  
### Python Libraries
- Install the required libraries using pip:
```bash
pip install -r requirements.txt
```

### ChromeDriver
Ensure that the ChromeDriver executable is installed and accessible. You can download it from [ChromeDriver Downloads](https://developer.chrome.com/docs/chromedriver/downloads) and place it in <b>/usr/local/bin</b> or update the path in <b>initialize_driver</b>

### Download ffmpeg
https://ffmpeg.org/download.html

### Usage
- Clone this repository:
```bash
git clone https://github.com/mateicaragea31/Automatic-YouTube-Navigation-System.git
cd Automatic-YouTube-Navigation-System
```
- Update the <b>chromedriver_path</b> in <b>initialize_driver</b> if needed
- Run the main script:
```bash
python main.py
```

### Notes
- Adjust the recording duration and FPS in main.py as needed
- Ensure the device_index is selected according to your system's devices
- Ensure FFmpeg is installed on your system
