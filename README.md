# 🌊 Trash Plastic Detection System – Web Interface  
**NASA Space Apps Challenge 2021: Leveraging AI/ML for Plastic Marine Debris**

---

## 🌍 Overview  

Plastic pollution is one of the most pressing environmental challenges of our time. Our **Trash Plastic Detection System** uses **AI/ML and computer vision** to detect plastic debris from **satellite, drone, and underwater images or videos**.  

The **web interface** serves as the **central hub** for collecting, analyzing, and visualizing detected plastics from various sources such as satellites, drones, or underwater robots. It helps visualize pollution data, monitor cleanup progress, and inspire public awareness.


## 🧠 Key Features  

### 🚀 Detection & Upload  
- Upload **videos or images** of oceans, rivers, or lakes.  
- The backend processes these files using the **YOLO deep learning model** to detect plastics.  

### 🛰️ Data Integration  
- AI systems embedded in **satellites, drones, or submarines** automatically detect plastics and send results to the same web database.  

### 📊 Visualization  
- The dashboard displays:  
  - Detected plastic debris images  
  - Statistical graphs showing daily detection reports  

### 🧩 Restricted Upload Access  
- Only authenticated users (e.g., partner organizations or devices) can upload data.  

---

## 💡 Why It Matters  

This system not only **detects** plastics but also **empowers action**:  
- Provides **real-time monitoring** of marine pollution  
- Generates **data-driven insights** for cleanup missions  
- Encourages **public awareness** and behavioral change through visual impact  

---

## 🧰 Technology Stack  

| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML, CSS, Bootstrap |
| **Backend** | Django (Python) |
| **AI/ML** | YOLO Object Detection, OpenCV |
| **Database** | SQLite / PostgreSQL |
| **Visualization** | Matplotlib / Chart.js |

---

## ⚙️ How It Works  

### Method 1 – Satellite/Drone/Robot Integration  
1. Embedded computers run `ocean.py` to capture images/videos.  
2. AI detects plastics and automatically uploads the results to the server.  
3. Detected images appear on the web dashboard.

### Method 2 – Manual Video Upload  
1. Go to [https://oceanplastic.herokuapp.com/upload](https://oceanplastic.herokuapp.com/upload).  
2. Upload an ocean or river video (requires credentials).  
3. The system extracts frames, detects plastics, and stores the results in the database.  
4. Visit the dashboard to view the detected plastics and daily stats.

---
## 🧪 Local Setup (Developers)  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/gautamtata/DeepPlastic.git
   cd DeepPlastic/web
   ```
2. **Create a virtual environment**
  ```bash
  python -m venv venv
  source venv/bin/activate   # (Linux/Mac)
  venv\Scripts\activate      # (Windows)
  ```
3. **Install dependencies**
  ```bash
  pip install -r requirements.txt
  ```
4. **Run the server**
  ```bash
  python manage.py runserver
  ```
5. **Open in browser**
  ```bash
  http://127.0.0.1:8000/
  ```
