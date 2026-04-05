def grade(actions, emails):
    score = 0
    total = len(emails)

    for action in actions:
        email = next(e for e in emails if e.id == action["email_id"])

        if action["type"] == "classify" and action["label"] == email.true_label:
            score += 1

        elif action["type"] == "reply" and email.true_label == "urgent":
            score += 1

        elif action["type"] == "ignore" and email.true_label == "spam":
            score += 1

    return score / total