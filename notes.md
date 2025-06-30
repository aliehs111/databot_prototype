#  Databot Notebook – Notes & Setup

## ✅ Project Summary

This notebook project sets up a custom chatbot ("Databot") using OpenAI’s `gpt-4o` model via LangChain. It analyzes datasets, answers user questions, and tracks token usage and cost.

---

## 🔧 Environment Setup

### 1. Folder Structure
```
project/
├── data/
├── notebooks/
│   └── 03_user_questions.ipynb
├── src/
├── .env
└── notes.md
```

### 2. Python Environment
- Environment: `nlp-dev` (created with `conda`)
- Python version: 3.11
- Key packages:
  - `langchain`
  - `langchain-openai`
  - `langchain-community`
  - `python-dotenv`
  - `openai`

Install with:
```bash
pip install -U langchain langchain-openai langchain-community openai python-dotenv
```

---

## 🔐 API Key Setup

`.env` file at project root:
```env
OPENAI_API_KEY=sk-xxxxxxx
```

Loaded in notebook with:
```python
from dotenv import load_dotenv
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
```

---

## 🤖 Model Configuration

Using **`gpt-4o`** with cost tracking:
```python
from langchain_openai import ChatOpenAI
from langchain.callbacks import get_openai_callback

llm = ChatOpenAI(model="gpt-4o", temperature=0, openai_api_key=openai_key)
```

---

## 💸 Cost Tracking

Wrapped inside a context manager:
```python
with get_openai_callback() as cb:
    response = chain.invoke({"summary": context_summary})
    print("🤖 Databot says:\n", response)
    print("\n--- Cost Summary ---")
    print(f"Tokens used: {cb.total_tokens}")
    print(f"Total cost: ${cb.total_cost:.6f}")
```

---

## 📊 Sample Output

> **Tokens used**: 1345  
> **Total cost**: $0.007142  
> **Model**: `gpt-4o`


## Databot Prototype Goals (Pre-integration Phase)

Core objectives for the Databot prototype before integrating it into the df.jsx app.

---

### ✅ 1. Core Prompting Functionality

- [x] Load a dataset (e.g., FloridaBikeRentals.csv).
- [x] Pass in a **context summary** of the dataset (shape, column names, missing values, etc.).
- [x] Receive a natural language response from the LLM.
- [ ] Experiment with different **prompt templates**:
  - Dataset summary
  - Exploratory suggestions
  - Direct user questions
- [ ] Add a user prompt input to allow interactive questioning.

---

### 💰 2. Cost and Token Tracking

- [x] Use `get_openai_callback()` to track tokens and costs per interaction.
- [ ] Optionally log or display **running total** of session cost.
- [ ] (Optional) Write logs to file (`databot_logs.txt`) for transparency.

---

### 🧱 3. Context Management Strategy

- [ ] Try using other context types:
  - `df.describe()`
  - `df.info()`
  - `df.dtypes`
  - Column value counts, cardinality, etc.
- [ ] Combine multiple context sources into a single input block.
- [ ] Begin mimicking how `df.jsx` stores context:
  - `target_column`, `excluded_columns`, `has_missing_values`, `feature_engineering_notes`, etc.

---

### 🔄 4. Chat Loop or Q&A Mode

- [ ] Build a simple memory loop (store question-answer pairs in a variable).
- [ ] Ask targeted data-related questions:
  - What would be a good target variable?
  - Should I normalize this dataset?
  - Which features have high correlation?

---

### 📝 5. Export to Markdown / Notes

- [x] Maintain a `notes.md` file with key takeaways from LLM output.
- [ ] Let Databot generate markdown-formatted summaries.
- [ ] Optionally include charts, stats, or preprocessing logs.

---

### 🔜 Next Steps

- Add a cell to allow `question = "..."` input and feed to LLM alongside context.
- Start drafting a few specific question prompts to test.
- Try combining `df.describe()`, `df.dtypes`, and custom metadata in one context block.


