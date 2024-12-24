# Medical-RAG

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-green?logo=flask&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-orange?logo=chainlink&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue)

[![Watch the video](https://img.youtube.com/vi/M-jtiz8eRJM/maxresdefault.jpg)](https://youtu.be/M-jtiz8eRJM)


> **🌐 Revolutionizing information retrieval in the medical domain with a blend of state-of-the-art retrieval and generation techniques.**

## 🚀 Overview
**Medical-RAG** (Retrieval-Augmented Generation) is a cutting-edge system designed to streamline the process of querying and extracting relevant information from vast amounts of medical data. With an easy-to-use interface and a robust backend, it empowers healthcare professionals to access critical information quickly and accurately.

### Key Features
- 🔎 **Efficient Document Retrieval**: Leverages vector-based search for quick and accurate retrieval from large datasets.
- 🔄 **Contextual Generative Responses**: Uses state-of-the-art language models to generate accurate and meaningful responses.
- 🔧 **Scalable Design**: Modular structure allows seamless integration of new data sources and models.
- 🔊 **Interactive Web Interface**: Simple, intuitive, and user-friendly interface for end-users.

---

## 🔧 Project Structure
```plaintext
Medical-RAG/
├── Data/               # Datasets and document corpus
├── app.py              # Main application script 
├── .gitignore          # Files to ignore in version control
├── research/           # Experimental notebooks for RAG development
│   ├── Trial.ipynb     # Initial experiments
│   ├── rag_demo.ipynb  # Demo implementation
│   └── demo.ipynb      # End-to-end prototype
├── requirements.txt    # Python dependencies
├── vector_store.py     # Vector store for document embeddings
├── setup.py            # Installation script for the project
├── template.py         # Prompt templates and boilerplate code
├── README.md           # Project documentation (this file!)
├── templates/          # HTML templates for the web app
│   └── index.html      # Main webpage
├── src/                # Core source code
│   ├── __init__.py     # Package initializer
│   ├── prompt.py       # Prompt generation logic
│   └── helper.py       # Utility functions
└── static/             # Static assets for the web app
    └── style.css       # Styling for the interface
```

---

## 📚 Requirements
- Python 3.8+
- Dependencies (install via `requirements.txt`):
  ```bash
  pip install -r requirements.txt
  ```

---

## 🚪 Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/Medical-RAG.git
   cd Medical-RAG
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Vector Store**:
   - Prepare your dataset and place it in the `Data/` folder.
   - Run `vector_store.py` to generate document embeddings.

4. **Run the Application**:
   ```bash
   python app.py
   ```
   The application will be accessible at `http://localhost:5000`.

---

## 🔁 Workflow
1. **Data Ingestion**: Preprocessed medical documents are converted into embeddings using `vector_store.py`.
2. **Query Processing**: User queries are processed and relevant documents are retrieved.
3. **Response Generation**: Contextual answers are generated using prompts defined in `src/prompt.py`.
4. **Web Display**: Results are presented via the interactive web interface.

---

## 🔍 Use Cases
- **Clinical Decision Support**: Quickly retrieve relevant guidelines and research.
- **Medical Research**: Summarize and extract key information from studies.
- **Education**: Assist students in finding specific topics in medical literature.

---

## 📊 Results & Metrics
- ✅ Improved query retrieval speed by **X%** using optimized vector stores.
- ✅ Achieved high accuracy in response generation with domain-specific tuning.
- ✅ Reduced user research time by **Y%** through concise and context-aware answers.

---

## 🙏 Acknowledgments
Special thanks to the open-source tools and frameworks that made this project possible:
- **[LangChain](https://github.com/hwchase17/langchain)**
- **[Groq APIs](https://groq.com/)**
- **[Flask](https://flask.palletsprojects.com/)**

---

🎥 [Watch the Demo!](https://youtu.be/M-jtiz8eRJM)



---

## 🎨 Contributing
Contributions are welcome! Feel free to:
1. Fork this repository.
2. Create a new branch.
3. Submit a pull request with detailed information.

---

## 🛠️ License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 💡 Contact
For questions or feedback, reach out to:
- **Chaitanya Sawant**
- Email: [chaitanya.aiwork@gmail.com](mailto:chaitanya.aiwork@gmail.com)
- Twitter: [@chaitanya_42](https://x.com/chaitanya_42)
- GitHub: [@chaitanya-24](https://github.com/chaitanya-24)

