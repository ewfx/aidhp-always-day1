import os
#import json
import requests
from azure.core.credentials import AzureKeyCredential
from validationData import validationData
from users import userData
import csv
from time import sleep
#set GITHUB_TOKEN=""

# Load the GitHub token from environment variables
os.environ["GITHUB_TOKEN"] = "#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"
token = os.getenv("GITHUB_TOKEN")
endpoint = "https://models.inference.ai.azure.com"
#model_name = "jais-30b-chat"
#model_name="mistral-small-2503"
#model_name = "Meta-Llama-3-8B-Instruct"
#model_name = "gpt-4o"
#model_name = "Phi-3-mini-4k-instruct"
def createPromt(recentActivity,userData):
    cur_prompt='''you will have to recommend products, based on the interest, income ,recent activities(recentPurchase/productLike/socialMediaComment) of the user ,recent social media posts,
 details of which I am giving below:
person details:
annual Income : ##annualIncome##
interests:  ##interests##
recent Activity:
##recentActivity##


strictly recommend those products, which could be purchased from 10 percent of the annual income.while giving answer, do not mention company name example: "The Platinum Card® from American Express" , instead mention "premium credit card".
if "interests" include products, costiler than 5 percent of annual income, than suggest credit, loan options.
also think of, any add ons for recent purchases example: "car cover" if recent purchase/interest is "car".
note: please do not give any explanation in you answer, just give the top 5 recommendations.
if social media comment has a positive sentiment, and the intent is a product, then that should get preference over other "user interest"
you answer should not have any extra words, other than the top 5 recommendations.'''
    for i,j in userData.items():
        cur_prompt=cur_prompt.replace(f"##{i}##",j)
    #print(cur_prompt)
    recent_acvty=f""
    for i,j in recentActivity.items():
        if(len(j)==0):
            continue
        if(i=='socialMediaComment'):
            recent_acvty+=f"recent social Media comment: {j}\n"
        elif(i=='productLike'):
            recent_acvty+=f"recently Liked product: {j}\n"
        elif(i=='recentPurchase'):
            recent_acvty+=f"recently purchased: {j}\n"
    cur_prompt=cur_prompt.replace(f"##recentActivity##",recent_acvty)
    print(cur_prompt)
    print('')
    return cur_prompt
    


    

def main(promptt,cur_model):
    if token is None:
        print("GITHUB_TOKEN is not set.")
        exit(0)
    else:
        print(f"Token Loaded: {token[:5]}...")  # Print the first 5 characters of the token for debugging
    # Prepare the request headers
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Prepare the request body
    body = {
        "messages": [
            #{"role": "system", "content": "You are a helpful assistant.strictly limit answers to 1 word only"},
            {"role": "system", "content": '''You are a helpful assistant.try to answer in minimum possible words, and don't give explanations at all'''},
            {"role": "user", "content": promptt}
        ],
        "temperature": 1.0,
        "top_p": 1.0,
        "max_tokens": 1000,
        "model": cur_model
    }

    # Send the POST request
    response = requests.post(f"{endpoint}/chat/completions", headers=headers, json=body)

    # Check for unexpected response
    if response.status_code != 200:
        print(f"Error: {response.status_code}, {response.text}")
        if("RateLimitReached" in str(response.status_code)):
            sleep(60) 
        return 'error'

    # Parse and print the response content
    response_data = response.json()
    print(response_data['choices'][0]['message']['content'])
    return response_data['choices'][0]['message']['content']

if __name__ == "__main__":
    models=["Meta-Llama-3-8B-Instruct","gpt-4o","Phi-3-mini-4k-instruct"]
    output=[['details','recommendation by Meta-Llama','recommendation by gpt-4o','recommendation by Phi-3-mini']]
    requestsMade=0
    try:        
        for validationRow in validationData:
            requestsMade+=1
            promptt=createPromt(validationRow['recentActivity'],userData[validationRow['Name']])
            row=[str(validationRow)+'\n'+str(userData[validationRow['Name']])]
            for cur_model in models:
                row.append(main(promptt,cur_model))                
            output.append(row)
            if(requestsMade%6==0):
                sleep(60)

    except Exception as err:
        print(f"The sample encountered an error: {err}")
    with open('./validation_results.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerows(output)
