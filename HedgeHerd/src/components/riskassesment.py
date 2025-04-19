def run_risk_assessment():
    questions = [
        {
            "question": "1. What is your investment time horizon?",
            "options": {
                "a": "Less than 1 year",
                "b": "1-5 years",
                "c": "More than 5 years"
            },
            "scores": {
                "a": 1,
                "b": 2,
                "c": 3
            }
        },
        {
            "question": "2. How would you feel if your portfolio dropped 20% in a month?",
            "options": {
                "a": "Panic and sell everything",
                "b": "Feel uneasy but stay invested",
                "c": "Buy more while it's cheap"
            },
            "scores": {
                "a": 1,
                "b": 2,
                "c": 3
            }
        },
        {
            "question": "3. What is your primary investment goal?",
            "options": {
                "a": "Capital preservation",
                "b": "Growth and income",
                "c": "Aggressive growth"
            },
            "scores": {
                "a": 1,
                "b": 2,
                "c": 3
            }
        }
    ]

    print("📊 Welcome to the Risk Assessment Quiz!\n")
    total_score = 0

    for q in questions:
        print(q["question"])
        for key, val in q["options"].items():
            print(f"   {key}) {val}")
        while True:
            answer = input("Your choice (a/b/c): ").lower()
            if answer in q["scores"]:
                total_score += q["scores"][answer]
                print()  # Empty line between questions
                break
            else:
                print("❌ Invalid input. Please choose a, b, or c.\n")

    # Determine risk profile
    if total_score <= 4:
        risk_profile = "🟦 Conservative"
    elif total_score <= 6:
        risk_profile = "🟨 Moderate"
    else:
        risk_profile = "🟥 Aggressive"

    print("✅ Quiz complete!")
    print(f"Your Risk Profile: {risk_profile}")


if __name__ == "__main__":
    run_risk_assessment()
