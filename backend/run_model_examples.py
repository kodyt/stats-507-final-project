from model.load_model import generate_full_explanation

# Example 1
example_1 = {
    "code": """def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)""",
    "question": "What does this function do?"
}

# Example 2
example_2 = {
    "code": """def is_even(n):
    return n % 2 == 0""",
    "question": "How does this function work?"
}

examples = [example_1, example_2]

results = []

print("🧠 Running model on examples...\n")

for idx, example in enumerate(examples, 1):
    print(f"🔹 Example {idx}")
    print("Code:\n", example["code"])
    print("Question:", example["question"])

    explanation = generate_full_explanation(example["code"], example["question"])
    results.append({
        "code": example["code"],
        "question": example["question"],
        "response": explanation
    })

    print("Response:\n", explanation)
    print("\n" + "="*50 + "\n")

# ✅ Save to output.txt
with open("output.txt", "w") as f:
    for idx, r in enumerate(results, 1):
        f.write(f"🔹 Example {idx}\n")
        f.write("Code:\n" + r["code"] + "\n")
        f.write("Question: " + r["question"] + "\n")
        f.write("Response:\n" + r["response"] + "\n")
        f.write("\n" + "="*70 + "\n")

print("📁 Output saved to output.txt")
