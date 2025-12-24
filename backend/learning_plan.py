# learning_plan.py

def generate_7_day_plan(missing_skills):
    plan = {}
    day = 1

    for skill in missing_skills:
        if day > 7:
            break

        plan[f"Day {day}"] = f"Learn basics of {skill}"
        day += 1

        if day > 7:
            break

        plan[f"Day {day}"] = f"Practice {skill} with examples"
        day += 1

    return plan


if __name__ == "__main__":
    missing = ['sql', 'excel', 'power bi']
    plan = generate_7_day_plan(missing)

    for day, task in plan.items():
        print(day, "→", task)
