from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load model and tokenizer
t5_tokenizer = T5Tokenizer.from_pretrained("./Localmodels/T5_small")
t5_model = T5ForConditionalGeneration.from_pretrained("./Localmodels/T5_small")

# Example input text
input_text = "question: What is the capital of France? Answer in a single word."

# Tokenize
inputs = t5_tokenizer(input_text, return_tensors="pt")

# Generate output
output_ids = t5_model.generate(**inputs, max_length=500)

# Decode and print
output_text = t5_tokenizer.decode(output_ids[0], skip_special_tokens=True)
print("T5-small output:", output_text)
