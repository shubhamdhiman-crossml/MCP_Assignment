# 🏥 Hospital Database (MCP + LangChain AI Agent)

This project demonstrates how to build an **AI-powered hospital assistant** using:

* **Model Context Protocol (MCP)** for secure tool access
* **LangChain Agents** for reasoning and tool orchestration
* **Google Gemini (Generative AI)** for natural language understanding
* **FastMCP Server** for exposing hospital data tools

The AI agent can:

* Fetch patient records
* Retrieve billing information
* List all registered patients
* Respond in natural, human-like language

---


## 🚀 Features

* 🔌 **MCP Server Integration** — Secure tool-based access to hospital data
* 🤖 **LLM Agent Reasoning** — Decides which tool to call based on user intent
* 🧠 **Natural Language Interface** — Chat like a hospital front-desk assistant
* 🛠️ **Tool-Based Architecture** — Clean separation of AI and backend logic
* 🔒 **Environment-Based API Key Management**

---

## ⚙️ Prerequisites

Make sure you have:

* **Python 3.10+** installed
* A **Google Generative AI API Key**
* Virtual environment (recommended)

---

## 📦 Installation

### 1️⃣ Clone or Download the Project

```bash
git clone https://github.com/shubhamdhiman-crossml/MCP_Assignment.git
cd MCP_Assignment
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**Windows:**

```bash
.venv\Scripts\activate
```



### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your_google_api_key_here
```

> ⚠️ Never commit `.env` files to GitHub

---

## 🏥 Running the MCP Server

The MCP server exposes hospital tools for the AI agent.

In one terminal, run:

```bash
python mcp_server.py
```

You should see:

```
Starting Hospital MCP Server...
```

---

## 🤖 Running the AI Agent

Open a **new terminal** and run:

```bash
python agent.py
```

You should see:

```
Hospital AI Agent Ready!
```

---

## 💬 Example Queries

Try asking:

```
Show me patient P001 details
What is the bill for P002?
List all patients
Who is the doctor for Amit Sharma?
```

The agent will:

1. Understand your intent
2. Select the correct MCP tool
3. Call the backend server
4. Respond in natural language

---

## 🛠️ MCP Tools Available

| Tool Name            | Description                   |
| -------------------- | ----------------------------- |
| `get_patient_record` | Fetch patient medical details |
| `get_patient_bill`   | Retrieve billing information  |
| `list_all_patients`  | List all registered patients  |
| `health_check`       | Server status and tool list   |

---

## 🧠 System Prompt

The agent behavior is controlled by `prompt.py`. This allows you to:

* Enforce safety rules
* Define response style
* Control tool usage behavior

---

## 🔐 Security Notes

* API keys are loaded using `dotenv`
* MCP server restricts access to only approved tools
* Input validation prevents unsafe tool calls

---

## 🧪 Sample Data

All hospital data is stored in:

```
data.py
```

You can modify or connect it to a real database (MySQL, PostgreSQL, MongoDB) for production use.

---

## 🌱 Future Enhancements

* 🗄️ Database integration (SQL / NoSQL)
* 👤 Role-based access (Admin / Doctor / Staff)
* 🧾 PDF bill generation
* 🌐 Web UI (React / Streamlit)
* 🔐 Authentication for MCP server

---

## 📚 Learning Objectives

This project helps you understand:

* Model Context Protocol (MCP)
* LangChain agent architecture
* Tool-based AI design
* Secure API integration
* AI-driven backend systems

---

## 🧑‍💻 Author

**Shubham Dhiman**


---


