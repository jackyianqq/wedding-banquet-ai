# 💍 Wedding Banquet AI Recommender

This is a Flask-based AI web app that helps users find suitable wedding banquet venues in Singapore based on guest count, budget, and day of the week. The recommendation engine uses OpenAI GPT to suggest the best-fit venues from a local dataset.

## 🖥️ Features

- 💡 Smart recommendations powered by GPT-4.
- 📊 Venue data loaded from `venues.json`.
- 🔄 One-click "Update Venues" button to fetch the latest venue data.
- ✅ Clean UI with success alert feedback.
- 📁 Project structure for easy development.

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/jackyianqq/wedding-banquet-ai.git
cd wedding-banquet-ai

### 2. Set Up Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

### 3. Install Requirements
pip install -r requirements.txt

### 4. Set Your OpenAI API Key
export OPENAI_API_KEY=your_api_key_here
-> You can get your API key from https://platform.openai.com.

### 5. Run the App
python3 -m app.main
-> Then open your browser and go to http://127.0.0.1:5000

🗂️ Project Structure
wedding-banquet-ai/
├── app/
│   ├── main.py              # Flask app
│   ├── recommender.py       # AI recommendation logic
│   └── scraper.py           # Venue data scraping logic (optional)
├── templates/
│   └── index.html           # Web UI
├── data/
│   └── venues.json          # Venue dataset (auto-updated)
├── scripts/
│   └── update_venues.py     # Script to refresh venue data
├── requirements.txt
└── README.md

🔁 Updating Venue Data
Click the 🔄 Update Venues button on the website to automatically refresh venue data. The backend will run scripts/update_venues.py and update data/venues.json.

© 2025 Wedding Banquet AI | Built with ❤️ by Jacky


---

### ✅ To Use:

1. Save this as a file called `README.md` in your project folder.
2. Run the following to add and push it:

```bash
git add README.md
git commit -m "Add README with setup and usage guide"
git push

