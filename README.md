
# Unit Converter Web App

A **web-based unit converter** built with **Flask**, Python, HTML, and CSS/Bootstrap. Convert between different units of **length, weight, and temperature** in a clean, interactive interface.

---

## 🛠 Features

- Convert units for:
  - **Length**: Meter, Kilometer, Mile
  - **Weight**: Milligram, Gram, Kilogram, Ounce, Pound
  - **Temperature**: Celsius, Fahrenheit, Kelvin
- Interactive form-based interface
- Results display immediately below the conversion form
- Responsive design using **Bootstrap**
- Supports multiple conversions without refreshing the page

---

## 📂 File Structure

```

Unit_converter_web/
│
├─ app.py                # Main Flask application
├─ converter/            # Python conversion logic
│   ├─ length.py
│   ├─ weight.py
│   └─ temperature.py
├─ templates/            # HTML templates
│   ├─ base.html
│   ├─ index.html
│   ├─ length.html
│   ├─ weight.html
│   └─ temperature.html
└─ static/
├─ css/
│   └─ style.css
└─ image/
└─ logo.png

````

---

 💻 Installation & Setup

1. **Clone the repo**  
```bash
git clone <your-repo-url>
````

2. **Navigate into the project folder**

```bash
cd Unit_converter_web
```

3. **Create a virtual environment and activate it**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

4. **Install Flask**

```bash
pip install Flask
```

5. **Run the app**

```bash
python app.py
```

6. **Open in browser**

```
http://127.0.0.1:5000/
```

---

## ⚡ Technologies

* **Python** – Flask framework for backend
* **HTML/CSS** – Page structure & styling
* **Bootstrap** – Responsive layout & components
* **Jinja2** – Dynamic templates in Flask

---

## ✅ Notes

* All conversions are handled in Python functions in the `converter` folder.
* Conversion formulas are accurate to industry standards.
* Static assets like CSS and images are stored in `static/`.

---

## 📬 Contact

Created by **[ananya mengistu]**.
Check out my GitHub: [Your GitHub URL]

```
