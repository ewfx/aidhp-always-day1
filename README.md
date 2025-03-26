# 🚀AI-Driven Hyper-Personalization & Recommendations


## 📌 Table of Contents
- [Introduction](#introduction)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
Develop a Gen-AI based solution, which gives highly personalized recommendations , by analyzing customer profile , social media activity, purchase history, sentiment data, etc.Also decides on whether it will be safe to offer a credit option, for the product the user wants, by analysing the annual income, recent purchase history, sentiment of the user-based on their social media posts.


## 💡 Inspiration
AI models can be used for providing highly personalized recommendations , by analyzing customer profile , social media activity, purchase history, sentiment data, etc. The aim of this project is to create a basic working setup, to demonstrate , how freely available, online hosted models can be used, for this purpose.

## ⚙️ What It Does
for any recent user activity( social media post, product like , recent purchase ) API call is made to model, with detailed guidelines in prompt, to enable the model to wisely use the colllected info, to make recommendations for next products/services to ensure personelized customer engagement, and also to interpret the sentiment, intent of the social media posts, to prodivde business insights on reviews of existing products, etc. The model is also made to suggest, for which users, a credit optinons can be given , based on their dream products and thier annual income.

## 🛠️ How We Built It
2 offline models(downloaded and hosted in local host) and 5 online hosted models were analyzed and out of them 3 were chosen, based on their reasoning, ability to predict/recommend , as per the requirement of the project. parameter fine tunning was done, code was created to make the API request, validation data was created, user data was created, created Prompt containing the guidelines, for the model to follow to, for the recommendation process. 

## 🚧 Challenges We Faced
Major challenege is rate-limit in using freely available models, hosted on web. In case of offline models(meant to be downloaded and hosted locally), the major challenge was their download size and their training/fine tunning.

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
   note: GitHub token needs to be set as a  environment variables, before starting the program execution.more details here: https://github.com/marketplace
   cd code/src
   python main.py
   ```

## 🏗️ Tech Stack
- 🔹 Backend: python
- 🔹 Other: OpenAI API / Meta-Llama API / Phi-3 API

## 👥 Team
- **Darshan Kumar** 

