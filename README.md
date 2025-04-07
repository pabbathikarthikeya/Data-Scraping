# Lead Scraper using SerpAPI & Streamlit

## Overview

This project is a **LinkedIn lead scraper** that utilizes [SerpAPI](https://serpapi.com/) for Google search scraping, scores the leads based on relevant keywords, and displays the results using an interactive **Streamlit** dashboard. It also allows CSV download functionality for further use.

---

## Features

- 🔍 Scrapes LinkedIn profiles using Google Search via SerpAPI
- 📌 Filters results by **keyword**, **location**, and optionally **company**
- 📊 Scores leads based on a predefined keyword list
- 📁 Saves results as `leads.csv` and `scored_leads.csv`
- 🌐 Streamlit web app for uploading, viewing, and downloading scored leads

---

## Libraries and Dependencies

| Library     | Purpose                            |
| ----------- | ---------------------------------- |
| `requests`  | API communication with SerpAPI     |
| `pandas`    | Data manipulation and CSV handling |
| `streamlit` | Web application and UI display     |

Install them via pip:

```bash
pip install requests pandas streamlit
```

---

## How It Works

### 🔎 1. Scraping Leads

```python
query = f'site:linkedin.com/in/ "{keyword}" "{location}"'
```

The script builds a Google search query to find LinkedIn profiles with the specified `keyword` and `location`. Optionally, it includes a company name. The query is executed using SerpAPI.

### 📊 2. Scoring Leads

The results are analyzed and scored based on the presence of important keywords (e.g., `AI`, `ML`, `Recruiter`, `Data Scientist`). Each keyword match adds `+2` to the lead score.

### 💾 3. Saving Leads

Results are saved to:

- `leads.csv` (raw scraped leads)
- `scored_leads.csv` (scored and sorted leads)

### 🌐 4. Streamlit App

- Upload your `leads.csv`
- Visualize scored results with profile links
- Download the processed data as a CSV

To run the app:

```bash
streamlit run app.py
```

(Note: Save the Streamlit code in `app.py` or similar script)

---

## Technologies Used

- **Python 3**
- **SerpAPI** (for scraping Google Search)
- **Pandas** (for data manipulation)
- **Streamlit** (for dashboard interface)

---

## Deployment

This project can be deployed in multiple ways:

### 🧪 Local Deployment

```bash
streamlit run app.py
```

Make sure your terminal is in the correct directory and that all dependencies are installed.

### ☁️ Cloud Deployment (Optional)

You can deploy this Streamlit app using:

- [Streamlit Cloud](https://streamlit.io/cloud)

For deployment:

1. Push your code to GitHub
2. Add a `requirements.txt`
3. Connect your repo to the deployment platform

---

## Notes

- You **must** have a valid [SerpAPI API key](https://serpapi.com/manage-api-key)
- API key usage is subject to SerpAPI quota limits
- This tool scrapes publicly indexed profiles; ensure ethical and legal use

---

## Example Input

```python
keyword = "Machine Learning Engineer"
location = "India"
company = "Amazon"
```

## Example Output

| Name/Title         | LinkedIn URL        | Snippet                 | Lead Score |
| ------------------ | ------------------- | ----------------------- | ---------- |
| Senior ML Engineer | linkedin.com/in/... | Working on AI at Amazon | 12         |
| Data Scientist     | linkedin.com/in/... | Experience in ML & AI   | 10         |

---

## Author

**Pabbathi Venkata Karthikeya**\
Feel free to fork, contribute, and suggest improvements!

