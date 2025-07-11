# 🧠 ScrappyTheRobby — Local LLM-Powered News Research Tool 🗞️

ScrappyTheRobby is a fully **local AI-powered news research assistant** that helps you analyze and summarize news articles without relying on external APIs like OpenAI or Google. Designed to work offline and preserve privacy, it uses a combination of **Local LLMs**, **Web scraping**, and **Vector search** to give you contextual and concise insights.

## 🚀 Features

- 🔍 **Web Scraping**: Extracts real-time articles from popular news sources.
- 🧠 **Local Language Model**: Uses a local LLM to summarize and answer questions.
- 📚 **Vector Search**: Embeds articles and allows semantic search using your queries.
- 🛡️ **No API Needed**: 100% local — no OpenAI key or internet dependency after scraping.
- 🖥️ **Clean Streamlit UI**: Interactive frontend for smooth user experience.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** — for UI
- **BeautifulSoup / Requests** — for scraping
- **SentenceTransformers / FAISS** — for embeddings and semantic search
- **Local LLM (GGUF / llama.cpp / HuggingFace models)**

---

## 🧑‍💻 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/ShubhamJadhav03/NewsReseachTool.git
cd NewsReseachTool


2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

3. Download Local LLM
You can download a model like llama-2-7b.gguf and place it in a models/ directory.

Tip: Use tools like llama.cpp or transformers to run it.

4. Run the App
bash
Copy
Edit
streamlit run main.py


<img width="1918" height="960" alt="Fianl image 2" src="https://github.com/user-attachments/assets/2f11c86d-fbbf-44dd-a3a6-f1610e1f892e" />

🔮 Use Cases
Research assistant for journalists and students

Private AI tool for sensitive news analysis

Local LLM playground with real-world use

🧱 Future Improvements
Support for multiple LLMs (Mistral, Phi, etc.)

PDF export of summaries

Schedule-based daily scrapes and reports

Topic-based clustering and insights

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.

📄 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Shubham Jadhav
LinkedIn • GitHub


