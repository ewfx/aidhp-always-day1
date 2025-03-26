# 🚀AI-Driven Hyper-Personalization & Recommendations


## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
Develop a Gen-AI based solution, which gives highly personalized recommendations , by analyzing customer profile , social media activity, purchase history, sentiment data, etc.


## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:



## 💡 Inspiration
What inspired you to create this project? Describe the problem you're solving.

## ⚙️ What It Does
Explain the key features and functionalities of your project.

## 🛠️ How We Built It
2 offline models(downloaded and hosted in local host) and 5 online hosted models were analyzed and out of them 3 were chosen, based on their reasoning, ability to predict/recommend , as per the requirement of the project. parameter fine tunning was done, code was created to amke the API request, validation data was created, user data was created, created Prompt containing the guidelines, for the model to follow to, during the recommendation process. 

## 🚧 Challenges We Faced
Major challenege is rate-limit in using freely available models, osted on web. In case of local models, the major challnge was their size and their training/fine tunning.

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/ewfx/aidhp-always-day1.git
   ```
2. Install dependencies  
   ```sh
   pip install azure-core
   pip install csv
   pip install transformers
   pip install huggingface_hub
   ```
3. Run the project  
   ```sh
   cd code/src
   python main.py
   ```

## 🏗️ Tech Stack
- 🔹 Backend: python
- 🔹 Other: OpenAI API / Meta-Llama API / Phi-3 API

## 👥 Team
- **Darshan KUmar** 

