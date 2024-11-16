# M5 StickC Plus2 Firmware Project

This project is a custom firmware designed for the **M5 StickC Plus2** microcontroller. It provides an interactive user interface, multiple functional modes, and real-time battery monitoring. The firmware is perfect for hobbyists and developers looking for a versatile, ready-to-use setup for their M5 StickC Plus2 device.

## 💎 Features
- **Multiple Operational Modes:**
  - **Hold Mode:** Activates the laser while Button B is pressed.
  - **Click Mode:** Emits a single laser pulse when Button B is pressed.
  - **Toggle Mode:** Toggles the laser on/off with each press of Button B.
  - **Spam Mode:** Emits laser pulses at a fixed interval while Button B is held down.
- **Battery Monitoring:**
  - Displays battery level in real-time using visual sprites.
- **Power Saving Mode:**
  - Activated by pressing Button C, dims the screen to conserve power.
  - The screen reactivates when any button is pressed.

## 💎 Controls
- **M5:** Cycles through the operational modes.
- **Button B:** Executes the selected mode's action.
- **Button C:** Toggles power-saving mode.

## 💎 Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/m5stickc-plus2-project.git
2. Use the M5Burner tool to flash the firmware onto your M5 StickC Plus2 device.
3. Restart the device and enjoy!

## 💎 How it works
The firmware leverages M5Stack's hardware features and libraries to create a user-friendly interface and efficient operations. The code is optimized for real-time performance, ensuring seamless transitions between modes and smooth updates of battery status.

## 💎 You can easily modify this firmware for your preferences. Here's how:
- Download main.py file
- Open UiFlow2
- Connect your device to PC
- Connect through COM3 port in console (bottom left button)
- Delete current one, then upload your new modified main.py file
