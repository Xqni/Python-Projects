# 🔄 Unit Converter CLI

A beginner–friendly but feature-rich **command-line Unit Converter** built with Python.  
Supports both **currency conversion** (via an external API) and **unit conversion** (via the `pint` package).  
Designed with **two usage modes**:  
- ⚡ `argparse` for power users  
- 🎛️ `questionary` for an interactive CLI experience  

---

## ✨ Features

- 🌍 **Currency conversion** using a [live external API](https://apiplugin.com/currency-exchange)
- 📏 **Unit conversion** for temperature, length, angles, and measurements via [pint](https://pint.readthedocs.io/)  
- 🧩 **Custom helpers package** for cleaner project structure  
- 🖥️ **Dual interface**: command-line arguments *or* interactive prompts  
- 🧪 **Tests included** (both currency and unit conversion) with `pytest`  
- 🔑 **Secure API keys** handled via `.env` and [python-dotenv](https://pypi.org/project/python-dotenv/)  

---

## 🚀 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/Xqni/Python-Projects.git
cd "Python Projects"
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

Create a .env file in the project root and add your API key:
```bash
API_KEY=your_api_key_here
```

## 🛠 Usage
CLI Mode (with ```argparse```)
```python
# Convert currencies
python -m convproj.converter 100 usd cad

# Convert units
python -m convproj.converter 100 degC degF
```
Interactive Mode (with ```questionary```)
```python
# Convert currencies
python -m convproj.converter
```
You’ll be guided through a simple text-based interface:
```
? What would you like to convert today? :)
>> Currency
   Units
```
```text
NOTE: if you are using interactive mode, you must enter a value for each of the questions.
The program will not proceed until you do.
```

## 🧪 Running Tests

Tests are written using pytest. Run them with:
```python
pytest tests/

# or

cd test
pytest test_convert.py
```

## 📂 Project Structure
```bash
# Python Projects/
# ├───Beginner Projects/
# |   |
# |   ├───convproj/
# |   │   └───tests/
# |   │   
# |   └───helpers
# └───.env      <--- put your env vars here
```

## 🧑‍💻 Author
Built with ❤️ and Python by [Xani](https://github.com/Xqni).
