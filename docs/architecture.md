# System Architecture

## Modules

### 1. Evaluation Input Module

Accepts:

- Question
- AI Response
- Reference Answer

### 2. Reference Knowledge Base

Uses:

- TruthfulQA
- SQuAD Dataset

Stores:

- Chunks
- Embeddings
- Vector Index

### 3. Multi Agent Evaluation

Agents:

- Relevance Judge Agent
- Accuracy Judge Agent
- Hallucination Detection Agent
- Completeness Judge Agent
- Verdict Agent

### 4. Scoring Dashboard

Displays:

- Scores
- Reasoning
- Final Verdict

### 5. Analytics Module

Tracks evaluation quality over time.