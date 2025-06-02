# HTML Table to CSV Extractor 🧾

This project is a simple Python script that extracts data from an HTML table on a public webpage and saves it as a well-formatted CSV file.

## 🔧 Technologies Used
- Python 3.x
- `requests`
- `BeautifulSoup4`

## 📋 Features
- Extracts table rows and columns from any HTML page
- Saves data as a structured `.csv` file
- Lightweight (no Selenium or browser needed)
- Easy to adapt to other websites

## 🚀 How It Works

1. Sends a GET request to the target webpage
2. Parses the HTML using BeautifulSoup
3. Finds the first table in the page (can be customized)
4. Extracts headers and rows
5. Writes everything into a CSV file

## 📁 Example

**Source URL:**  
[W3Schools HTML Table Example](https://www.w3schools.com/html/html_tables.asp)

**Extracted Output (CSV):**

