# 🤖 Multi-Agent Workflow: Sequential Task Execution

**A Python implementation of a Multi-Agent Workflow using the Sequential Handoff (Planner-Worker-Critic) pattern. Features structured JSON handoffs, specialized agent roles, and a simulated "Smart" Validation Guardrail.**
---

This project implements a **Sequential Handoff** pattern using three specialized AI agents. It demonstrates how to decompose complex tasks into structured sub-steps and apply autonomous quality control.

## 🚀 Key Feature: The "Smart Critic"
Unlike a basic chatbot, this system includes a **Validation Guardrail**. The Critic agent extracts the core topic from the worker's report and applies a logical threshold (Topic length > 20 characters) to ensure the input is substantial enough for a high-quality result.

## 🏗️ Architecture
I chose the **Sequential Handoff** pattern to ensure a clear "Chain of Responsibility":
1. **Planner Agent (🔍):** Breaks the user's topic into a 2-step strategic plan.
2. **Worker Agent (🛠️):** Parses the plan via JSON and simulates the execution of tasks.
3. **Critic Agent (⚖️):** Acts as the Quality Gate, providing a final score and approval status.



## 🛡️ Technical Highlights
- **Strict Data Contracts:** Used **Pydantic** to enforce schemas (`AgentPlan`, `TaskStep`, `CriticReview`), preventing data corruption between agents.
- **Data Extraction:** Implemented string parsing in the Critic to isolate user intent from execution logs.
- **Interactive Flow:** Built with a "Human-in-the-Loop" start, allowing users to provide dynamic topics via terminal input.

## 💻 Installation & Usage
This project uses **[uv](https://astral.sh/uv/)** for fast, reproducible Python environments.

### 1. Clone the repository

```bash
git clone https://github.com/LAjoyan/AI-agent-patterns-python.git
cd AI-agent-patterns-python
```

### 2. Prerequisites
- Python 3.12 or higher

- uv installed

### 3. Setup & Run

```bash
# Install dependencies and sync the environment
uv sync

# Run the multi-agent workflow
uv run python main.py
```

### 📊 Agent Workflow Visualization



```mermaid
graph TD
    User([👤 User]) -->|Topic| P(🔍 Planner)
    P -->|Plan| W(🛠️ Worker)
    W -->|Result| C(⚖️ Critic)
    
    C -->|Feedback| Decision{Approved?}
    
    Decision -- No --> P
    Decision -- Yes --> End([✅ Success])

    subgraph "Iteration Loop (Max 3)"
    P
    W
    C
    Decision
    end