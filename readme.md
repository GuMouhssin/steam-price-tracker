# 🎮 Steam Price Tracker

A Python-based price tracking system for Steam games that lets users monitor their favorite games, detect price changes, store price history, and receive desktop notifications for discounts or price increases.

Built with **Steam Store API**, **SQLite**, and **Plyer notifications**.

---

## ✨ Features

* 🔍 Search Steam games by name
* ➕ Add games to a persistent tracking list
* ❌ Remove tracked games
* 💾 Store tracked games in SQLite database
* 📉 Detect price drops
* 📈 Detect price increases
* 🕒 Save full price history with timestamps
* 🔔 Desktop notifications for price changes
* 📊 View historical price changes for each game
* ⚡ Fast API-based tracking using Steam AppIDs

---

## 🏗 Project Architecture

steam-price-tracker/
│── main.py          # Application entrypoint
│── cli.py           # Interactive command-line interface
│── config.py        # Global configuration/constants
│── db.py            # SQLite database operations (CRUD + history)
│── fetch.py         # Core HTTP request handling
│── search.py        # Steam game search API logic
│── parser.py        # Data normalization and parsing
│── tracker.py       # Price comparison & tracking engine
│── alerts.py        # Desktop notification system
│── worker.py        # Background/scheduled tracker execution
│── requirements.txt # Project dependencies
│── .gitignore       # Ignored files
│── README.md        # Documentation

## 🛠 Tech Stack

* **Python**
* **SQLite**
* **Steam Store API**
* **Requests**
* **Plyer**

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/steam-price-tracker.git
cd steam-price-tracker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the application:

```bash
python main.py
```

Main menu:

```text
1. Add a game to track
2. Show tracked games
3. Remove a tracked game
4. Check prices now
5. Show game history
6. Exit
```

---

## 📂 Database Design

### `games`

Stores current tracked games.

| Column     | Type                |
| ---------- | ------------------- |
| id         | INTEGER PRIMARY KEY |
| name       | TEXT                |
| init_price | INTEGER             |
| fin_price  | INTEGER             |
| discount   | INTEGER             |
| currency   | TEXT                |

---

### `price_history`

Stores all price change events.

| Column     | Type    |
| ---------- | ------- |
| game_id    | INTEGER |
| old_price  | INTEGER |
| new_price  | INTEGER |
| discount   | INTEGER |
| changed_at | TEXT    |

Compound Primary Key:

```text
(game_id, changed_at)
```

---

## 🔔 Notifications

Uses desktop notifications to alert users when:

* A tracked game price drops
* A tracked game price increases

Example:

```text
🔥 Steam Price Drop!
ELDEN RING
3999 → 2999
```

---

## 🔮 Future Improvements

* ⏰ Scheduled automatic checks
* 📧 Email alerts
* 💬 Discord webhook alerts
* 📉 Best historical price tracking
* 📤 Export history to CSV/JSON
* 🌐 Web dashboard

---

## 📌 Why this project?

This project demonstrates:

* API integration
* Database design
* CRUD operations
* Data persistence
* Event history modeling
* Notification systems
* CLI application architecture

---

## 📜 License

MIT License.
