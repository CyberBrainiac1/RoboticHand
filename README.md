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

| Item                                  | Description                                | Qty | Unit Price ($) | Total Price ($) | URL | Running Total ($ with Tax) |
|---------------------------------------|--------------------------------------------|-----|----------------|------------------|-----|------------------------------|
| 20KG Digital Servo (AliExpress)       | High-torque waterproof servo               | 6   | 8.79           | 52.74            | https://www.aliexpress.us/item/3256808992396501.html | 52.74 |
| AliExpress Shipping (Servo Order)     | Shipping for AliExpress servo/horn bundle  | 1   | 15.50          | 15.50            | N/A | 68.24 |
| Adafruit 16-Channel PWM/Servo HAT     | Servo control board for Raspberry Pi       | 1   | 17.50          | 17.50            | https://www.adafruit.com/product/2327 | 85.74 |
| Shipping (Adafruit)                   | Standard shipping                          | 1   | 5.95           | 5.95             | https://www.adafruit.com | 91.69 |
| Servo Horn (AliExpress)               | Metal servo attachment                     | 1   | 0.99           | 0.99             | https://www.aliexpress.com/item/3256802841540071.html | 92.68 |



