```
# 🛠️ Prebuilt Python Logger

A lightweight, plug-and-play `logger.py` you can copy into any Python project.  
It supports colorized terminal output, rotating file logs, and is easy to configure using `.env`.

---

## 📦 Features

- 🟢 Colored logs in the console
- 📁 File logging with rotation (5MB x 5 backups)
- ⚙️ Configurable via `.env`
- ✅ Simple usage: `from logger import get_logger`

---

## 🚀 Quick Start

### 1. Clone this repo or copy `logger.py` into your project

```bash
git clone https://github.com/yourusername/prebuilt-logger.git
cd prebuilt-logger
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment config

```bash
cp .env.example .env
```

Edit `.env` to set your desired logging level:

```
LOG_LEVEL=DEBUG
ENV=development
```

### 4. Run the example

```bash
python example.py
```

---

## 🧪 Usage in Your Code

```python
from logger import get_logger

logger = get_logger(__name__)

logger.info("Logger is working!")
logger.error("Something went wrong!")
```

---

## 📁 Logs

All logs are written to `logs/app.log`. The directory is auto-created if it doesn't exist.

---

## 📜 Requirements

- `colorlog`
- `python-dotenv`

(Already included in `requirements.txt`)

---

## 📝 License

MIT – use freely and customize as needed.
```
