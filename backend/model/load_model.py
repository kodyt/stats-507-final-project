import torch
from transformers import (
    T5ForConditionalGeneration,
    RobertaTokenizer,
    AutoTokenizer,
    AutoModelForCausalLM
)

code_model_name = "Salesforce/codet5-small"
code_tokenizer = RobertaTokenizer.from_pretrained(code_model_name)
code_model = T5ForConditionalGeneration.from_pretrained(code_model_name)
code_model.eval()

explanation_model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
chat_tokenizer = AutoTokenizer.from_pretrained(explanation_model_name, use_fast=True)
chat_model = AutoModelForCausalLM.from_pretrained(explanation_model_name)
chat_model.eval()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
code_model.to(device)
chat_model.to(device)

def summarize_code_with_codet5(code: str, max_tokens: int = 64) -> str:
    prompt = f"summarize: {code}"
    inputs = code_tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to(device)
    outputs = code_model.generate(
        **inputs,
        max_length=max_tokens,
        num_beams=4,
        early_stopping=True,
        no_repeat_ngram_size=2
    )
    return code_tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

def build_prompt(code: str, summary: str, question: str) -> str:
    return f"""### Instruction:
            You are an expert data structures and algorithms tutor. A user provides the following Python function and asks a question related to how it works.

            Code:
            {code}

            Summary:
            {summary}

            Question:
            {question}

            Please explain the code and answer the question in simple, beginner-friendly English.
            Avoid including raw code in your answer.

            ### Response:
            """

def generate_explanation_with_tinyllama(prompt: str, max_tokens: int = 256) -> str:
    inputs = chat_tokenizer(prompt, return_tensors="pt").to(device)
    outputs = chat_model.generate(
        **inputs,
        max_new_tokens=max_tokens,
        temperature=0.7,
        top_p=0.9,
        do_sample=True,
        pad_token_id=chat_tokenizer.eos_token_id
    )
    decoded = chat_tokenizer.decode(outputs[0], skip_special_tokens=False)
    return clean_response(decoded[len(prompt):].strip())

def clean_response(text: str) -> str:
    return (
        text.replace("se:", "")
            .replace("</s>", "")
            .strip()
    )

def generate_full_explanation(code: str, question: str) -> str:
    summary = summarize_code_with_codet5(code)
    prompt = build_prompt(code, summary, question)
    explanation = generate_explanation_with_tinyllama(prompt)
    return explanation


# code = """def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# """
# question = "What does this function do and why is recursion used?"

# answer = generate_full_explanation(code, question)
# print("💡 Final Explanation:\n", answer)