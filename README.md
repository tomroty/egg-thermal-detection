
# Chicken Egg Detection with Thermal Camera

This project utilizes a **MLX90640 thermal camera** with an algorithm to detect chicken eggs based on thermal signatures. The camera captures a temperature array with Python, that is then processed with an algorithm in C that will detect and count the eggs. The result is then sent back to the python script, which will send the data to a firebase database.

## Project Structure

The project is divided into two main folders:

### `/demo`
This folder contains the demo version of the project. It allows you to test the program locally without any hardware or dependencies requirements.


### `/release`
This folder contains the main version of the code that is designed to work with a **MLX90640 thermal camera** connected to a **Raspberry Pi**. 

⚠️ The database part is disabled by default

**➡️ For more infos, check the README file in each folder**

## Hardware Requirements

- **MLX90640 Thermal Camera**: A 32x24 pixel thermal infrared sensor that detects heat patterns in the environment.
- **Raspberry Pi**: A Raspberry Pi with the thermal camera connected to it is required to run the program. The recommended model is **Raspberry Pi 4** or later.

---
