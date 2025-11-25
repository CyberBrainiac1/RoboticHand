# Robotic Hand Project

This project is a 3D-printed robotic hand designed to mimic human finger flexion using a tendon-based mechanism. Each finger uses a servo to pull a string routed through the joints, allowing the finger to curl smoothly. A Raspberry Pi Zero 2 W paired with a 16-channel PWM HAT controls all six servos.

---

## Why I Built This

I wanted hands-on experience with tendon-driven actuation, multi-servo control, and mechanical design. Building a robotic hand gave me a real-world challenge that combined CAD, robotics, control systems, and mechanical problem-solving.

---

## 3D Model Screenshots

<img width="792" height="640" alt="image" src="https://github.com/user-attachments/assets/9df56278-d786-4002-a5de-12b7fc4fa829" /> <img width="624" height="689" alt="image" src="https://github.com/user-attachments/assets/fa767b0e-6f4f-428e-ad54-0caea4c539d8" /> <img width="1298" height="624" alt="image" src="https://github.com/user-attachments/assets/9dd18fdf-923b-4231-9a8f-af79eaaf349d" />

---

## Servo Torque Justification

I chose to use **20 kg·cm servos** because I cannot precisely anticipate the real torque demands of a tendon-driven finger mechanism. Even though the fingers are lightweight, friction at each joint, the angles in the string routing, changing lever arms as the finger bends, and dynamic loads all multiply the torque the servo must provide. Instead of risking stalling, weak curls, or inconsistent grip strength, using high-torque servos gives a large safety margin and ensures smooth, reliable operation no matter how the mechanical system behaves. This also leaves room for future upgrades or heavier finger designs without needing to replace the actuators.

---

## Bill of Materials (BOM)

| Item | Description | Qty | Unit Price ($) | Total ($) | URL | Running Total ($ with Tax) |
|------|-------------|-----|----------------|-----------|------|-----------------------------|
| 20KG Digital Servo (AliExpress) | High-torque servo for finger actuation | 6 | 8.79 | 52.74 | AliExpress | 52.74 |
| AliExpress Shipping | Shipping for servos | 1 | 9.77 | 9.77 | N/A | 62.51 |
| Adafruit 16-Channel PWM/Servo HAT | Multi-servo controller for Raspberry Pi | 1 | 17.50 | 17.50 | Adafruit | 80.01 |
| Shipping (Adafruit) | Standard shipping | 1 | 5.95 | 5.95 | Adafruit | 85.96 |
| Metal Servo Horn | Stronger horn for string attachment | 1 | 0.99 | 0.99 | AliExpress | 86.95 |


