# System-Design-End-Term
```markdown
# Rate Limiting Microservice with FastAPI 🚦

This microservice implements a basic rate-limiting mechanism using Python and FastAPI to protect APIs from excessive request bursts and ensure stable performance.

## 📌 Features

- Rate limiting by **client IP**
- Simple **Fixed Window Counter** algorithm
- Configurable request limit and window size
- Returns `429 Too Many Requests` when limit exceeded

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- `pip` for installing packages

### Installation

1. Clone the repo (or create your project folder)
2. Create and activate a virtual environment:

```bash
python -m venv venv
# On Windows PowerShell:
.\venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install fastapi uvicorn
```

4. Run the API server:

```bash
uvicorn main:app --reload
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

### 📬 API Endpoints

- `GET /` — A test endpoint with rate limiting.

### 🔐 Rate Limiting Configuration

The rate limit is defined as:

- **Max Requests**: `100`
- **Time Window**: `60` seconds
- **Scoped by**: client IP address

These values can be adjusted in `main.py`:

```python
RATE_LIMIT = 100
WINDOW_SIZE = 60
```

### ❗ Exceeding the Limit

If a client exceeds the allowed number of requests in the time window, they'll receive:

```json
{
  "detail": "Rate limit exceeded"
}
```

With HTTP status: `429 Too Many Requests`

---

## 📚 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

---

## 🧠 Algorithm Choice: Fixed Window Counter

We use the **Fixed Window Counter** method due to its simplicity and suitability for scenarios where precise rate smoothing isn't critical. It's easy to implement and works well for low to moderate traffic APIs.

---

## 📂 Project Structure

```
Limit/
├── main.py
├── README.md
└── venv/ (virtual environment)
```

---

## 📬 Contact

Made by **Sayed Yusuf Masood** for System Design End Term 🚀
```
