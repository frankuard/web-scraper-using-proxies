<<<<<<< HEAD
# 🔍 Python Web Scraper with Proxy Rotation

A beginner‑friendly Python web scraping project that demonstrates a clean and safe scraping workflow using proxy rotation and HTML file parsing.

---

## 📌 What This Project Does

This project is split into **three stages**:

1. **Proxy validation**
2. **HTML fetching**
3. **Data extraction**

Each stage is handled in a **separate Python file** which makes the project easy to understand, debug, and extend.

---

## 📁 Project Structure

project/
│
├── proxies/
│   ├── all-proxies.txt        → Raw proxy list
│   └── valid_proxies.txt      → Working proxies from all-proxies.txt
│
├── html_page/
│   └── html_page.html         → Saved HTML content
│
├── check_proxies.py           → Validates proxies
├── fetch_page.py              → Fetches webpage HTML
├── main.py                    → Content parsing and extraction from the saved HTML 
└── README.md

---

## 🧠 How the Project Works 

### 1️⃣ Proxy Validation

- Reads proxies from a text file
- Tests each proxy by making a simple request
- Uses multiple threads to speed up the process
- Saves only working proxies for later use

---

### 2️⃣ HTML Fetching

- Uses **one target URL**
- Rotates proxies automatically
- If one proxy fails, the next proxy is used
- Stops as soon as a successful proxy is used
- Saves the raw HTML into a local `.html` file

---

### 3️⃣ Data Extraction

- Opens the saved HTML file
- Uses BeautifulSoup to extract data
- Optional use of pandas for structuring data

---

## ✅ Why This Design Is Good Practice

- Avoids repeated requests to the website
- Reduces IP ban risk
- Allows offline testing
- Easy to scale later

---

## 🚫 What This Project Does NOT Do

- No automatic crawling
- No scraping multiple pages at once
- No JavaScript rendering
- No database storage (yet)

---

## ⚠️ Important Notes

- Always respect websites’ robots.txt rules
- Do not scrape private or restricted content
- Use this project only for educational purposes

---

## 👤 Author

Roshan Karki  
Python & Web Scraping Learner

---

⭐ This project is designed for learning and portfolio use.

