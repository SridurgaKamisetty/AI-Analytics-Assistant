from ai.llm import ask_ai

print("=" * 50)
print("Enterprise AI Chat Assistant")
print("=" * 50)

while True:

    question = input("\nYou : ")

    if question.lower() == "exit":
        break

    answer = ask_ai(question)

    print("\nAI :")
    print(answer)