# 🧠 Text Summarizer (Learning Project)

This is a **small learning project** built to understand how Hugging Face models work, how to fine-tune them, and how to integrate them into a simple application.

The goal of this project is **learning and experimentation**, not production use.

---

## 🎯 Objective

* Understand **T5 (Text-to-Text Transformer)** model
* Learn **fine-tuning on a real dataset (SAMSum)**
* Practice **model inference**
* Integrate model with **FastAPI backend + simple UI**

---

## 🚀 What this project does

* Takes dialogue/text as input
* Generates a short summary using a trained T5 model
* Displays the result in a basic web interface

---

## 🏗️ Basic Flow

```id="flow1"
User Input → FastAPI → T5 Model → Summary → UI
```

---

## 📂 Project Structure

```id="flow2"
Text-Summarizer/
│
├── app.py                # FastAPI backend
├── summarizer.py         # Model loading + inference
├── index.html            # Simple frontend UI
├── saved_summary_model/  # Saved trained model
├── data/                 # Dataset (SAMSum)
└── results/              # Training outputs
```

---

## ⚙️ Setup

```bash id="flow3"
pip install fastapi uvicorn transformers torch sentencepiece protobuf
```

---

## ▶️ Run

```bash id="flow4"
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000
```

---

## 🧪 API

### POST `/summarize`

```json id="flow5"
{
  "dialogue": "Your text here"
}
```

---

## 📌 Notes

* This is a **beginner-level implementation**
* UI is intentionally simple
* Focus is on **understanding workflow**, not optimization
* Model performance is not heavily tuned

---

## 🧠 Key Learnings

* Hugging Face model usage
* Basic fine-tuning workflow
* Saving & loading models
* FastAPI integration
* Frontend → Backend → Model pipeline

---

## 📜 Disclaimer

This project is created **purely for learning purposes**.
