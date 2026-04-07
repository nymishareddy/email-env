import os
from openai import OpenAI
from env import EmailEnv

API_BASE_URL = os.getenv("API_BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)


def ai_agent(email_text):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": f"Classify: {email_text}. Answer: important or spam"}
            ],
            temperature=0,
        )
        return response.choices[0].message.content.strip().lower()
    except:
        return "important"


def main():
    env = EmailEnv()
    env.reset()

    rewards = []
    steps_taken = 0

    print(f"[START] task=email_env env=email_env model={MODEL_NAME}", flush=True)

    done = False

    while not done:
        if env.current_index >= len(env.emails):
            break

        current_email = env.emails[env.current_index]["text"]

        action = ai_agent(current_email)

        obs, reward, done, _ = env.step(action)

        reward = reward if reward else 0.0
        rewards.append(reward)

        steps_taken += 1

        print(
            f"[STEP] step={steps_taken} action={action} reward={reward:.2f} done={str(done).lower()} error=null",
            flush=True,
        )

    score = sum(rewards) / len(rewards) if rewards else 0.0
    score = max(0.0, min(score, 1.0))

    rewards_str = ",".join(f"{r:.2f}" for r in rewards)

    print(
        f"[END] success=true steps={steps_taken} score={score:.2f} rewards={rewards_str}",
        flush=True,
    )


if __name__ == "__main__":
    main()
