from fastapi import FastAPI
from env import EmailTriageEnv
from models import Action

app = FastAPI()

env = EmailTriageEnv()

@app.get("/")
def root():
    return {"status": "running"}

# ✅ IMPORTANT: reset returns observation only
@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "observation": {
            "emails": [e.dict() for e in obs.emails]
        }
    }

# ✅ IMPORTANT: exact OpenEnv format
from typing import Optional

@app.post("/step")
def step(action: Optional[dict] = None):
    # handle empty body (IMPORTANT)
    if action is None:
        action = {}

    try:
        act = Action(**action)
    except:
        return {
            "observation": {"emails": []},
            "reward": 0.0,
            "done": False,
            "info": {"error": "invalid action"}
        }

    obs, reward, done, info = env.step(act)

    return {
        "observation": {
            "emails": [e.dict() for e in obs.emails]
        },
        "reward": float(reward),
        "done": bool(done),
        "info": info if info else {}
    }
@app.get("/state")
def state():
    return {
        "state": env.state()
    }