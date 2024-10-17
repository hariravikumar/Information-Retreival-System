# Information-Retreival-System

# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/hariravikumar/Information-Retreival-System
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n genai python=3.10 -y
```

```bash
conda activate genai
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your OPEN_API_KEY as follows:

```ini
OPENAI_API_KEY= "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# Finally run the following command
streamlit run app.py
```

Now,
```bash
open up : http://localhost:8501
```


### Techstack Used:

- Python
- LangChain
- Streamlit 
- OpenAI
- FAISS