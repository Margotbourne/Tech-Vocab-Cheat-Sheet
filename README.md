# Tech Vocab Cheat Sheet

A custom flashcard application built using Python, Flask, and PostgreSQL to track, review, and deep-dive into complex technical terminology and engineering concepts.

---

## 🚀 Tech Stack

* **Backend:** Python, Flask
* **Database:** PostgreSQL
* **Testing:** Pytest (with Playwright for end-to-end testing)
* **Frontend:** HTML, CSS (Responsive Design)

---

## 🛠️ Features

* **Custom Flashcard Tracking:** Create, read, update, and delete technical vocabulary terms.
* **Deep Dive Notes:** Dedicated pages and structured notes for deeper architectural or programmatic context on each term.
* **Interactive Study Mode:** A built-in study interface to test and reinforce your retention of tech terms.

---

## ⚙️ Project Setup

Follow these steps to get the development environment running locally.

### 1. Environment & Dependencies
Set up your Python virtual environment and install the required packages:

```shell
# Create the virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate 

# Install dependencies
pip install -r requirements.txt

# Install the virtual browser used for integration testing
playwright install
```

### 2. Database Configuration
Create your local PostgreSQL development and testing databases:

```shell
createdb Vocab_Cheat_Sheet
createdb tVocab_Cheat_Sheet_Test
```

> ⚠️ **Important:** Open `lib/database_connection.py`

### 3. Database Seeding
Populate your database schema and initial flashcard seed data:

```shell
python seeds/seed_database.py
```

### 4. Running Tests
Run the test suite with verbose logging to ensure everything is configured correctly:

```shell
pytest -sv
```

### 5. Launch the Application
Fire up the local Flask server:

```shell
python app.py
```

Now, open your browser and navigate to **`http://localhost:5001/`** to start studying!