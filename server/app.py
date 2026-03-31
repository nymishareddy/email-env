from fastapi import FastAPI
from env import EmailEnv

app = FastAPI()

env = EmailEnv()

@app.get("/")
def home():
    return {"message": "Email Env Running"}

@app.post("/reset")
def reset():
    obs = env.reset()
    return {"observation": obs}

@app.post("/step")
def step(action: str):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return {"state": env.state()}

def main():
    return app


if __name__ == "__main__":
    main()



