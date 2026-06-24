# 📚 NCERT Multi-Modal AI Tutor

A responsive, multi-modal web application engineered to provide personalized, step-by-step academic tutoring for Indian students from Class 8th to 12th. The platform accepts both natural language queries and image uploads (printed/handwritten textbook problems) to teach students core concepts using the NCERT curriculum framework.

---

## 🚀 Core Features

- **Multi-Modal Input Processing**: Students can type questions directly or upload photos/screenshots of problems from their textbooks.
- **Socratic Teaching Approach**: Instead of just giving flat answers, the AI is optimized to act as a supportive tutor, breaking down complex Physics, Chemistry, Biology, and Math problems into digestible, conceptual steps.
- **NCERT Curriculum Aligned**: Specifically tuned to understand the context, formatting, and pedagogical style of Indian secondary school education.
- **Intuitive Chat Interface**: Built with a clean, distraction-free user experience tailored for students.

---

## 🛠️ Tech Stack & Architecture

- **Language:** Python
- **Frontend UI:** Streamlit (Dynamic web framework for clean user interaction)
- **Core AI Engine:** Google Gemini API (`google-generativeai`)
- **Image Processing Engine:** Pillow (`PIL` for handling file uploads, rendering, and computer vision parsing)
- **Version Control:** GitHub

---

## 📂 Installation & Local Setup

To run this project locally on your machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd YOUR_REPOSITORY_NAME
   ```

2. **Install the required dependencies:**
   ```bash
   pip install streamlit google-generativeai pillow
   ```

3. **Set up your API Key:**
   Get a Gemini API key from Google AI Studio and configure it within your local environment or directly inside the app code.

4. **Launch the web application:**
   ```bash
   streamlit run app.py
   ```

---

## 💡 Motivation & Background

As a Class 12th student in the PCB (Physics, Chemistry, Biology) stream, I noticed a significant gap in accessible, high-quality, instant tutoring for students tackling rigorous NCERT exercises—especially when encountering cross-disciplinary analytical problems. 

Driven to solve this, I taught myself Python, frontend UI design with Streamlit, and API integration to build a free, scalable tool that acts as an on-demand personal academic mentor for peers across secondary education.
