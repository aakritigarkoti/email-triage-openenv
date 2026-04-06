from models import Email, Action, Observation
from tasks import get_task

class EmailTriageEnv:
    def __init__(self, task="easy"):
        self.task_name = task
        self.emails = []
        self.done = False
        self.processed = set()

    def reset(self):
        self.emails = get_task(self.task_name)
        self.done = False
        self.processed = set()
        return Observation(emails=self.emails)

    def step(self, action: Action):
        reward = 0

        email = next((e for e in self.emails if e.id == action.email_id), None)

        if not email:
            return Observation(emails=self.emails), -1, False, {"error": "invalid email"}

        if email.id in self.processed:
            return Observation(emails=self.emails), -0.5, False, {"error": "already processed"}

        # 🎯 REWARD LOGIC
        if action.type == "classify":
            if action.label == email.true_label:
                reward += 0.5
            else:
                reward -= 0.2

        elif action.type == "reply":
            if email.true_label == "urgent":
                reward += 0.5
            else:
                reward -= 0.3

        elif action.type == "ignore":
            if email.true_label == "spam":
                reward += 0.3
            elif email.true_label == "urgent":
                reward -= 0.5

        # ⭐ sender importance
        if "boss" in email.sender:
            reward += 0.2

        self.processed.add(email.id)

        # ✅ DONE CONDITION
        if len(self.processed) == len(self.emails):
            self.done = True
            reward += 1.0

        return Observation(emails=self.emails), reward, self.done, {}

    def state(self):
        return {
            "remaining": len(self.emails) - len(self.processed)
        }