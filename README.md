# 🔐 SSTI Vulnerability Demo – Flask Web App

This project demonstrates **Server-Side Template Injection (SSTI)** using a Flask-based event creation web application. The app includes a **toggle switch** to enable or disable SSTI, allowing developers, students, and security enthusiasts to study how SSTI vulnerabilities work — and how to defend against them.

---

## 📚 What is SSTI?

**Server-Side Template Injection (SSTI)** occurs when user input is insecurely embedded in a server-side template, allowing attackers to inject malicious expressions or code.

Popular server-side templating engines (like Jinja2 in Python, Twig in PHP, and Velocity in Java) evaluate expressions in templates. If user input is directly rendered without sanitization, it can lead to **code execution**, **data exposure**, or **server takeover**.

---

## 🧠 What Are Templates?

Templates are pre-designed HTML files embedded with dynamic placeholders (e.g., `{{ variable }}`, `{% if %}`, etc.) that get rendered on the server before being sent to the browser. Frameworks like Flask use **Jinja2**, a Python-based templating engine.

**Example (Jinja2 Template):**


<p>Hello {{ username }}!</p>

If the input username = "Yash" → the browser receives:
<p>Hello Yash!</p>


If an attacker inputs {{7*7}} and it gets rendered as code, the result will be 49.

---

🧑‍💻 Author
Created by Yash Pawar
Project for educational and ethical hacking purposes only.

---
