# Gemini SQL Query Generator

## Overview
The **Gemini SQL Query Generator** is a Streamlit application that converts natural language questions into SQL queries. Utilizing Google's Generative AI model, this app generates SQL commands based on user queries and retrieves data from a SQLite database.

## Features
- Converts English questions into SQL queries.
- Executes generated SQL queries against a SQLite database.
- Displays results in a user-friendly interface.
- Built with Streamlit for a seamless web experience.
- Uses Google Generative AI for intelligent SQL query generation.

## Requirements
- Python 3.7 or higher
- Streamlit
- Google Generative AI SDK
- SQLite3
- Python-dotenv

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/gemini-sql-query-generator.git
   cd gemini-sql-query-generator

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**: Create a `.env` file and add your Google API key:
   ```plaintext
   GOOGLE_API_KEY=your_google_api_key
   ```

5. **Prepare the SQLite Database**: Ensure you have a SQLite database named `student.db` with a table named `STUDENT` containing the columns `NAME`, `CLASS`, and `SECTION`.

## Usage
1. Run the application:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and go to `http://localhost:8501`.

3. Enter your question in the input field and click the "Ask the question" button.

4. The application will generate the corresponding SQL query and display the results.

## Example Queries
- How many entries of records are present?
- Tell me all the students studying in Data Science class?

## Contribution
Contributions are welcome! Please feel free to submit a pull request or open an issue for bugs or suggestions.

## License
This project is licensed under the MIT License.

## Acknowledgments
- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://cloud.google.com/generative-ai)
```

### Key Features of This Markdown
- The README is organized with headings for clarity.
- Essential information about installation, usage, and contribution is included.
- Example queries demonstrate how to interact with the application.
- Links are provided for easy navigation to relevant resources. 

Feel free to modify any sections to better match your project's specifics!
