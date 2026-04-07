from env import EmailEnv

TASK_NAME = "email_env"
BENCHMARK = "email_env"
MODEL_NAME = "simple-agent"


def simple_agent(email_text):
    if "lottery" in email_text.lower():
        return "spam"
    elif "meeting" in email_text.lower():
        return "important"
    elif "deadline" in email_text.lower():
        return "important"
    else:
        return "important"


def main():
    try:
        env = EmailEnv()
        env.reset()

        rewards = []
        steps_taken = 0

        # START
        print(f"[START] task={TASK_NAME} env={BENCHMARK} model={MODEL_NAME}", flush=True)

        done = False

        while not done:
            if env.current_index >= len(env.emails):
                break

            current_email = env.emails[env.current_index]["text"]

            action = simple_agent(current_email)

            obs, reward, done, _ = env.step(action)

            reward = reward if reward is not None else 0.0
            rewards.append(reward)

            steps_taken += 1

            # STEP
            print(
                f"[STEP] step={steps_taken} action={action} reward={reward:.2f} done={str(done).lower()} error=null",
                flush=True,
            )

        # SCORE NORMALIZATION 
        total_reward = sum(rewards)
        max_possible = len(rewards) * 1.0 if rewards else 1.0
        score = total_reward / max_possible
        score = max(0.0, min(score, 1.0))

        success = score > 0

        rewards_str = ",".join(f"{r:.2f}" for r in rewards)

        # END
        print(
            f"[END] success={str(success).lower()} steps={steps_taken} score={score:.2f} rewards={rewards_str}",
            flush=True,
        )

    except Exception as e:
        print(
            f"[END] success=false steps=0 score=0.00 rewards= error={str(e)}",
            flush=True,
        )


if __name__ == "__main__":
    main()
