from env import EmailEnv
import time

#Simple agent
def simple_agent(email_text):
    if "lottery" in email_text.lower():
        return "spam"
    elif "meeting" in email_text.lower():
        return "important"
    elif "deadline" in email_text.lower():
        return "important"
    else:
        return "important"


#MAIN EXECUTION
def main():
    env = EmailEnv()
    env.reset()

    done = False
    total_reward = 0

    while not done:
        current_email = env.emails[env.current_index]["text"]

        action = simple_agent(current_email)
        print(f"\nAgent action: {action}")

        _, reward, done, _ = env.step(action)
        total_reward += reward

    print("\nFinal Score:", total_reward)


if __name__ == "__main__":
    print("Starting Email Environment...")

    main()

    print("Environment ran successfully...")

    import time
    while True:
        print("App alive...")
        time.sleep(30)