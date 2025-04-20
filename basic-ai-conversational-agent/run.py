# run.py

from ai_agent import get_best_answer

print("Hello! Ask me something about AI.\n(Type 'exit' to quit.)")
while True:
    user_input = input("You: ")
    if user_input.lower() in ("exit", "quit"):
        print("Goodbye!")
        break
    response = get_best_answer(user_input)
    print("Bot:", response)