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

```text
steam-price-tracker/
│── main.py          # CLI entrypoint
│── db.py            # Database operations
│── steam_api.py     # Steam API integration
│── tracker.py       # Price checking logic
│── alerts.py        # Desktop notifications
│── utils.py         # Helper functions
│── requirements.txt
│── README.md
```

---

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
