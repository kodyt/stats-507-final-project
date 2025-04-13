import evaluate
import matplotlib.pyplot as plt
import pandas as pd
from load_model import generate_full_explanation 

# Load metrics
rouge = evaluate.load("rouge")
bleu = evaluate.load("bleu")
bert_score = evaluate.load("bertscore")

# GPT-style "gold" explanation
examples = [
    {
        "code": "def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n - 1)",
        "question": "What does this function do?",
        "reference": """This function calculates the factorial of a non-negative integer n using recursion. 
The factorial of a number is the product of all positive integers up to that number (e.g., 5! = 5×4×3×2×1 = 120). 
The function has a base case where it returns 1 when n is 0, which mathematically defines 0! = 1. 
For all other values, it recursively multiplies n by the factorial of n - 1, building the result from the inside out. 
This is a classic example of recursive algorithm design."""
    },
    {
        "code": "def is_even(n):\n    return n % 2 == 0",
        "question": "How does this function work?",
        "reference": """This function checks whether a number n is even. It uses the modulo operator %, which returns the remainder after division. 
If n % 2 equals 0, that means n is divisible by 2 with no remainder, so the function returns True. 
Otherwise, it returns False. This is a simple, constant-time check (O(1)) that leverages mathematical properties for efficiency."""
    }
]

# Run model on each example
predictions = []
references = []

for ex in examples:
    model_output = generate_full_explanation(ex["code"], ex["question"])
    predictions.append(model_output)
    references.append(ex["reference"])

# Compute metrics
rouge_result = rouge.compute(predictions=predictions, references=references)
bleu_result = bleu.compute(predictions=predictions, references=references)
bert_result = bert_score.compute(predictions=predictions, references=references, lang="en")

# Format into DataFrame
score_data = {
    "ROUGE-1": rouge_result["rouge1"],
    "ROUGE-2": rouge_result["rouge2"],
    "ROUGE-L": rouge_result["rougeL"],
    "BLEU": bleu_result["bleu"],
    "BERTScore (F1)": sum(bert_result["f1"]) / len(bert_result["f1"]),
}
score_df = pd.DataFrame(list(score_data.items()), columns=["Metric", "Score"])

# Plot
plt.figure(figsize=(10, 6))
bars = plt.bar(score_df["Metric"], score_df["Score"], color="skyblue")
plt.ylim(0, 1)
plt.ylabel("Score")
plt.title("Evaluation Metrics for AI Coding Tutor")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.xticks(rotation=15)

# Label bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.01, f"{yval:.2f}", ha='center', va='bottom')

plt.tight_layout()
plt.show()
