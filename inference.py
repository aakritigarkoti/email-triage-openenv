import os
from src.env import EmailTriageEnv
from src.models import Action
from src.tasks import get_task
from src.grader import grade

# ENV VARIABLES (mandatory)
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

def run_task(task_name):
    print("[START]")
    print(f"task: {task_name}")

    env = EmailTriageEnv(task=task_name)
    obs = env.reset()

    actions = []

    for email in obs.emails:
        text = (email.subject + " " + email.body).lower()

        # ✅ FIXED INDENTATION
        if "urgent" in text or "asap" in text or "immediately" in text:
            action = Action(type="reply", email_id=email.id)

        elif "win" in text or "offer" in text or "prize" in text:
            action = Action(type="ignore", email_id=email.id)

        else:
            action = Action(type="classify", email_id=email.id, label="normal")

        print("[STEP]")
        print(f"action: {action.type} on email {email.id}")

        obs, reward, done, _ = env.step(action)

        actions.append({
            "type": action.type,
            "email_id": action.email_id,
            "label": action.label
        })

    # grading
    emails = get_task(task_name)
    score = grade(actions, emails)

    print("[END]")
    print(f"score: {score}")
    print("\n")

def main():
    for task in ["easy", "medium", "hard"]:
        run_task(task)

if __name__ == "__main__":
    main()