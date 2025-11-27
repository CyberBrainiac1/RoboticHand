# Robotic Hand Project

This project is a 3D-printed robotic hand designed to mimic human finger flexion using a tendon-based mechanism. Each finger uses a servo to pull a string routed through the joints, allowing the finger to curl smoothly. A Raspberry Pi 4b paired with a 16-channel PWM HAT controls all six servos.

---

## Why I Built This

I wanted hands-on experience with tendon-driven actuation, multi-servo control, and mechanical design. Building a robotic hand gave me a real-world challenge that combined CAD, robotics, control systems, and mechanical problem-solving.

---

## 3D Model Screenshots

<img width="445" height="637" alt="image" src="https://github.com/user-attachments/assets/d58d0ab8-7019-46b1-9cf2-67ba2af5bec8" />

## PCB
I designed a custom PCB that will allow me to easily connect the servos to a usbc and my raspberry pi.
Schematic
<img width="954" height="455" alt="image" src="https://github.com/user-attachments/assets/262819bc-55a2-49bc-b58d-8f39eef93cd2" />
PCB
<img width="888" height="538" alt="image" src="https://github.com/user-attachments/assets/049e920b-72de-4bd0-a0a8-e3420ef0a8d5" />



---
## Wiring
I want to do the wiring exactly like this
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/25cc2481-d731-4d76-85a8-fdfcbda2c24a" />

---

## Bill of Materials (BOM)

| Item                              | Description                                 | Qty | Unit Price ($) | Total ($) | URL                                                                                                                   | Source     | Running Total ($) |
|----------------------------------|---------------------------------------------|-----|-----------------|-----------|-----------------------------------------------------------------------------------------------------------------------|------------|---------------------|
| MG90S 9g Micro Servo (15-pack)   | Metal gear micro servos for robotic fingers | 1   | 15.00           | 15.00     | https://www.aliexpress.us/item/3256807925508335.html                                                                 | AliExpress | 15.00              |
| AliExpress Shipping              | Shipping for AliExpress items               | 1   | 5.00            | 5.00      | N/A                                                                                                                   | AliExpress | 20.00              |
| Adafruit 16-Channel Servo HAT    | Servo control board for Raspberry Pi        | 1   | 17.50           | 17.50     | https://www.adafruit.com/product/2327                                                                                 | Adafruit   | 37.50              |
| Shipping (Adafruit)              | Standard shipping                           | 1   | 5.95            | 5.95      | https://www.adafruit.com                                                                                              | Adafruit   | 43.45              |
| Servo Horn (AliExpress, prev.)   | Metal servo attachment                      | 1   | 0.99            | 0.99      | https://www.aliexpress.com/item/3256802841540071.html                                                                 | AliExpress | 44.44              |
| Raspberry Pi 4B                  | *You already own this item*                 | 1   | 0.00            | 0.00      | https://www.raspberrypi.org/products/raspberry-pi-4-model-b/                                                          | Local      | 44.44              |
| **TOTAL**                        | —                                           | —   | —               | **44.44** | —                                                                                                                     | —          | **44.44**          |

