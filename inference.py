from env import EmailEnv

# Simple agent
def simple_agent(email_text):
    if "lottery" in email_text.lower():
        return "spam"
    elif "meeting" in email_text.lower():
        return "important"
    elif "deadline" in email_text.lower():
        return "important"
    else:
        return "important"


# MAIN EXECUTION
def main():
    try:
        env = EmailEnv()
        env.reset()

        done = False
        total_reward = 0

        while not done:
            
            if env.current_index >= len(env.emails):
                break

            current_email = env.emails[env.current_index]["text"]

            action = simple_agent(current_email)
            print(f"Agent action: {action}")

            _, reward, done, _ = env.step(action)
            total_reward += reward

        print("Final Score:", total_reward)

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
