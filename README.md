# Robotic Hand Project

This project is a 3D-printed robotic hand designed to mimic human finger flexion using a tendon-based mechanism. Each finger uses a servo to pull a string routed through the joints, allowing the finger to curl smoothly. A Raspberry Pi 4b paired with a 16-channel PWM HAT controls all six servos.

---

## Why I Built This

I wanted hands-on experience with tendon-driven actuation, multi-servo control, and mechanical design. Building a robotic hand gave me a real-world challenge that combined CAD, robotics, control systems, and mechanical problem-solving.

---

## 3D Model Screenshots

<img width="395" height="650" alt="image" src="https://github.com/user-attachments/assets/6b07c691-a54b-4a90-a34d-a1e2c733f9c9" />
<img width="413" height="706" alt="image" src="https://github.com/user-attachments/assets/2cbce2e7-2e32-4fe3-ac27-93fb5b24297f" />

<img width="423" height="771" alt="image" src="https://github.com/user-attachments/assets/8547de84-a66f-4590-bfa7-e42ad193267c" />



---

## Servo Torque Justification

I chose to use **20 kg·cm servos** because I cannot precisely anticipate the real torque demands of a tendon-driven finger mechanism. Even though the fingers are lightweight, friction at each joint, the angles in the string routing, changing lever arms as the finger bends, and dynamic loads all multiply the torque the servo must provide. Instead of risking stalling, weak curls, or inconsistent grip strength, using high-torque servos gives a large safety margin and ensures smooth, reliable operation no matter how the mechanical system behaves. This also leaves room for future upgrades or heavier finger designs without needing to replace the actuators.

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

