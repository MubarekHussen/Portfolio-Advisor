# Portfolio Advisor

## Overview

The Portfolio Advisor is a Python application designed to provide personalized portfolio management advice based on financial news articles and predefined stock holdings. It scrapes specified financial news articles, connects to the ChatGPT API for generating advice, and analyzes user-defined stock holdings to suggest adjustments.

## Task Overview

The task involves writing Python code to perform the following steps:

1. **Web Scraping:** Scrape the specified financial news article [here](https://finance.yahoo.com/news/inflation-comes-in-hotter-than-expected-in-march-123324666.html) to extract relevant content.

2. **OpenAI Integration:** Connect to the ChatGPT API to generate personalized portfolio advice based on the extracted content.

3. **Portfolio Analysis:** Assuming the user's holdings are 20% TSLA, 20% NVDA, 20% AAPL, 20% GOOG, and 20% US government bonds, analyze the content and suggest changes to the portfolio.

## Code Components

- **`scraper.py`:** Contains functions to scrape the specified financial news article and extract relevant content using BeautifulSoup.

- **`historical_data.py`:** Fetches historical stock data using the Yahoo Finance API and calculates price changes and weighted portfolio changes.

- **`portfolio_suggestion.py`:** Integrates with the OpenAI ChatGPT API to generate personalized portfolio advice based on the scraped content and historical stock data.

- **`requirements.txt`:** A text file containing a list of Python libraries required by the project. These libraries can be installed using the command `pip install -r requirements.txt`.

- **`Makefile`:** A Makefile providing commands for common tasks such as installing dependencies and running the project. Commonly used commands include:
  - `make install`: Installs project dependencies listed in `requirements.txt`.
  - `make run`: Executes the `portfolio_suggestion.py` script to generate personalized portfolio advice.

When you run `make`, it executes both `make install` and `make run`, ensuring that dependencies are installed and the project is executed seamlessly.

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/MubarekHussen/Portfolio-Advisor.git
   cd Portfolio-Advisor
   ```

2. **Replace OpenAI API Key:**

   Replace `'PUT YOUR API KEY HERE'` with your OpenAI API key inside the `.env` file.

3. **Install Dependencies and Run:**

   Create a Virtual Environment:

   You can create a virtual environment using the following commands:

   - For Windows:

   ```bash
   python -m venv venv
   ```

   - For macOS and Linux:

   ```bash
   python3 -m venv venv
   ```

   Activate the Virtual Environment:

   - For Windows:

   ```bash
   venv\Scripts\activate
   ```

   - For macOS and Linux:

   ```bash
   source venv/bin/activate
   ```

   Install Dependencies:

   If it's your first time using the project or if dependencies have changed, you should install them using the following command:

   ```bash
   make install
   ```

   Run the Project:

   After installing dependencies, you can run the project to generate personalized portfolio advice. Simply execute:

   ```bash
   make run
   ```

   This command will execute the portfolio_suggestion.py script and provide you with portfolio suggestions based on the scraped content and historical stock data.
