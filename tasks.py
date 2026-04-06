from models import Email
def get_task(level="easy"):

    if level == "easy":
        return [
            Email(id="1", subject="Win money", body="Click now", sender="spam@x.com", true_label="spam"),
            Email(id="2", subject="Meeting now", body="Join asap", sender="boss@company.com", true_label="urgent"),
        ]

    elif level == "medium":
        return [
            Email(id="1", subject="Discount offer", body="Limited deal", sender="ads@shop.com", true_label="spam"),
            Email(id="2", subject="Project update", body="Check when free", sender="manager@company.com", true_label="normal"),
            Email(id="3", subject="Client issue", body="Need fix today", sender="client@mail.com", true_label="urgent"),
        ]

    elif level == "hard":
        return [
            Email(id="1", subject="Let's catch up", body="Today maybe?", sender="friend@mail.com", true_label="normal"),
            Email(id="2", subject="URGENT: Server down", body="Fix immediately", sender="boss@company.com", true_label="urgent"),
            Email(id="3", subject="You won!", body="Claim prize", sender="fake@spam.com", true_label="spam"),
            Email(id="4", subject="Reminder", body="Deadline approaching", sender="manager@company.com", true_label="urgent"),

            # ✅ NEW HARD EMAIL (correctly added inside list)
            Email(
                id="5",
                subject="Quick question",
                body="Can you look into this today?",
                sender="boss@company.com",
                true_label="urgent"
            ),
        ]