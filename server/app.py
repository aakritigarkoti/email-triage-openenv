from fastapi import FastAPI
from env import EmailTriageEnv
from models import Action

app = FastAPI()

env = EmailTriageEnv()

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/reset")
def reset():
    obs = env.reset()
    return {"observation": {"emails": [e.dict() for e in obs.emails]}}

@app.post("/step")
def step(action: dict = {}):
    act = Action(**action)
    obs, reward, done, info = env.step(act)

    return {
        "observation": {"emails": [e.dict() for e in obs.emails]},
        "reward": float(reward),
        "done": bool(done),
        "info": info if info else {}
    }

@app.get("/state")
def main():
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()