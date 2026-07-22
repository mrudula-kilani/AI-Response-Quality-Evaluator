# 🤖 AI Response Quality Evaluator

**Infosys Springboard Internship Project**

An AI-powered evaluation system that analyzes the quality of AI-generated responses using multiple intelligent evaluation agents. The system measures relevance, accuracy, hallucinations, completeness, and generates an overall quality verdict.

---

# 📌 Project Overview

Large Language Models (LLMs) generate responses that may be relevant but incomplete, inaccurate, or hallucinated.

This project evaluates AI-generated responses using multiple independent judge agents and provides a detailed quality assessment.

The application supports:

- ✅ Single Response Evaluation
- ✅ Batch CSV Evaluation
- ✅ Interactive Dashboard
- ✅ CSV Export
- ✅ Visual Analytics

---

# 🎯 Objectives

- Evaluate AI-generated responses.
- Measure response relevance.
- Verify factual accuracy.
- Detect hallucinated content.
- Check response completeness.
- Generate an overall quality verdict.
- Evaluate multiple responses simultaneously using CSV files.

---

# 🧠 Evaluation Agents

## 1. Relevance Judge Agent

Measures how relevant the AI response is to the user's question using Sentence Transformers and cosine similarity.

**Output**

- Relevance Score
- Reason

---

## 2. Accuracy Judge Agent

Compares the AI response with the reference answer and evaluates factual correctness.

**Output**

- Accuracy Score
- Evidence

---

## 3. Hallucination Detection Agent

Identifies unsupported or potentially hallucinated responses by comparing the response with the reference answer.

**Output**

- Hallucination Status
- Reason

---

## 4. Completeness Judge Agent

Determines whether all important aspects of the question have been answered.

**Output**

- Completeness Score
- Missing Points
- Feedback

---

## 5. Verdict Agent

Combines all evaluation scores using a weighted scoring model.

### Weights

| Metric | Weight |
|---------|--------|
| Accuracy | 40% |
| Relevance | 30% |
| Completeness | 20% |
| Hallucination | 10% |

**Output**

- Overall Score
- Verdict
- Consolidated Reasoning

---

# 📊 Features

### Single Response Evaluation

- Evaluate one AI response.
- Detailed reasoning.
- Missing point detection.
- Overall verdict.

---

### Batch Evaluation

Upload a CSV containing:

| Question | Reference | Response |
|----------|-----------|----------|

The application automatically:

- Evaluates every response
- Generates scores
- Displays a dashboard
- Exports results as CSV

---

### Dashboard

Displays

- Average Overall Score
- Average Relevance
- Average Accuracy
- Average Completeness
- Hallucinations Detected

---

### Visual Analytics

Includes

- 📊 Average Evaluation Score Bar Chart
- 🥧 Verdict Distribution Pie Chart

---

# 📂 Project Structure

```text
AI-Response-Quality-Evaluator
│
├── agents/
│   ├── accuracy_agent.py
│   ├── completeness_agent.py
│   ├── hallucination_agent.py
│   ├── model_loader.py
│   ├── relevance_agent.py
│   └── verdict_agent.py
│
├── data/
│   ├── benchmark.csv
│   └── sample_batch.csv
│
├── tests/
│   └── validate_agents.py
│
├── batch_evaluator.py
├── app.py
├── requirements.txt
└── README.md
```

---

# 🛠️ Technologies Used

- Python
- Streamlit
- Sentence Transformers
- Scikit-Learn
- Pandas
- Matplotlib
- FAISS
- Git
- GitHub

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Response-Quality-Evaluator.git
```

Move into the project

```bash
cd AI-Response-Quality-Evaluator
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📈 Current Progress

## ✅ Milestone 1

- Project Planning
- System Design
- Evaluation Architecture
- Input Module

---

## ✅ Milestone 2

- Relevance Judge Agent
- Accuracy Judge Agent
- Hallucination Detection Agent
- Benchmark Dataset
- Validation Module

---

## ✅ Milestone 3

- Completeness Judge Agent
- Verdict Agent
- Batch Evaluation
- Dashboard
- Visual Analytics
- CSV Export

---

# 🚀 Future Enhancements

- RAG-based document retrieval
- LLM-assisted hallucination verification
- PDF report generation
- Deployment on Streamlit Community Cloud
- Authentication and user history
- Advanced evaluation metrics

---

# 👩‍💻 Author

**Mrudula Kilani**

B.Tech – Artificial Intelligence & Data Science

Velagapudi Ramakrishna Siddhartha Engineering College

Infosys Springboard Internship Project