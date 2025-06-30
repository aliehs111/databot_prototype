# Final Capstone Project Plan Proposal
## Integrate a tutor style Chatbot teaching Data Analysis and Machine Learning concepts in a React App

## Overview

This chatbot, named **Databot**, will guide users through the process of cleaning and preparing datasets. It will help them understand:

- How to handle missing values
- When and how to normalize or standardize data
- How to encode categorical features and which methods to choose
- Which features to select or drop based on analysis goals
- The nuances of data cleaning and feature engineering asd how it affects ML model output
- Users upload the dataset and save it.  Once they have processed theh dataset, they save a "cleaned" version of it.  The cleaned version can be run through machine learning models.  Use

Unlike generic chatbots, **Databot** will use metadata and summaries from the user's actual uploaded dataset to generate responses that are customized and relevant.  Databot will even keep track of what the user does to the datasets before they save the cleaned version that will be run through the ML models.

---

## Tools and Libraries

| Layer       | Technology               | Purpose                                                       |
|-------------|--------------------------|---------------------------------------------------------------|
| Frontend    | React                    | User interface for uploading datasets and chatting.           |
| Backend     | FastAPI                  | Processes CSVs and serves Pandas/Numpy outputs via API.       |
| Database    | MySQL                    | Stores metadata from uploaded CSV files.                      |
| Storage     | AWS S3                   | Stores uploaded CSV files for processing.                     |
| LLM Layer   | LangChain                | Handles prompt templates, context injection, and chaining.    |
| Model API   | OpenAI GPT-4o            | Provides inference at scale with solved compute constraints.  |
| Token Usage | `get_openai_callback()`  | Tracks token usage and cost during development.               |
| Secrets     | `python-dotenv`          | Loads and manages API keys securely.                          |

---

## Why GPT-4o?

- **No compute constraints**  This is by far the biggest reason. My local machine has GPU, but Heroku where the app is deployed does not offer GPU so it's not going to be able to handle the chat model.  My other option if I were to pick an open source pretrained LLM was to use AWS Sagemaker to run the chatbot in the app.  It was too risky with additional CI/CD complexity to manage in time for the presentation.  
- **Cost-effective**: GPT-4o seemed like the best over all for speed, context length, and quality.  But I want to test out other gpt models too.
- **Integrated tracking**: I'm using callback utilities to monitor token usage and cost in real time.

- I plan to build a **second chatbot** using a different architecture but don't think I can get this done before presentation time so I'm not committing to this for my final capstone.  This is what I want to set up mostly as an experiment for my own curiosity:

    - Fine-tune or deploy a smaller open-source model (e.g., Mistral or Falcon)
    - Host it on **AWS SageMaker** for full control of the model runtime
    - Let users compare both bots — one using OpenAI, one using custom logic — within the same app


## This is not just a UI shell on top of ChatGPT

It's a **learning tool** that covers parts of our class syllabus.  Users can chat with Databot as they look at before and after stats to fully understand how their data cleaning steps affected the dataset and influenced the outcome of the ML models.  Then the LLM helps the user in a fully contextualized way:

- Built-in **dataset context** from uploaded files
- Custom **prompt templates** tuned to data cleaning workflows
- Opportunities to compare LLM-guided vs. manual cleaning results

The chatbot helps users understand **why** each cleaning step matters — not just what to do next.

The chatbot can be fed specific, structured context from:

-  **Uploaded CSVs** (user-provided datasets)
-  **Metadata** like column names, data types, missing values
-  **User selections** like target columns, scaling choices, and cleaning strategies

This gives the chatbot a deep understanding of what the user is working on.

> **Example prompt context**:  
> “The user uploaded a dataset with 8,000 rows, selected `Sales` as the target column, and clicked to begin normalization. Guide them through next steps.”


## How I plan to do this:

 - The app is already 70% developed and deployed.  I have enough content to work from to start working on Databot anytime now.  We haven't covered all this in class yet.  So I don't want to get too far ahead on this before we cover LangChain in class.
 - I will prototype Databot in Jupyter Notebook. This way I can do all the testing and not dealing with endpoints and API calls for now.  I just want to be fully immersed in the model so I know all the ins and outs of it before I integrate it.
 - I am going to use the exact same functions and variables in this notebook that I am using in my app's backend.  This will make it easier when I am ready to integrate it.
 - The functions are in regular python files so I can import them as needed in my notebooks and that almost simulates the webdev feel of having the client and server directories and separation of concerns keeping my code as clean as possible.
 - I've set up a .env file in the directory with my API key and have made my first few chats come to life with the context of an uploaded csv file.  That was one of the coolest things ever.  Databot actually commented on the file and asked the user questions about it.  That was cool.

 - I've set up a project directory like this to start:
```
.
├── data
│   ├── FloridaBikeRentals.csv
│   ├── Iris.csv
│   └── housing_data.csv
├── docs
├── notebooks
│   ├── 01_load_clean_dataset.ipynb
│   ├── 02_generate_context.ipynb
│   └── 03_user_questions.ipynb
├── notes.md
├── requirements.txt
├── src
│   ├── __pycache__
│   ├── cleaning.py
│   └── context.py
└── untitled.md
```














