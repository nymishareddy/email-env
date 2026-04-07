class EmailEnv:
    def __init__(self):
        self.emails = []

    def reset(self):
        self.emails = [
            {"text": "Meeting at 5pm", "label": "important"},
            {"text": "Win lottery now!!!", "label": "spam"},
            {"text": "Project deadline tomorrow", "label": "important"}
        ]
        self.current_index = 0
        self.total_reward = 0
        return self.emails

    def step(self, action):
        # If already finished
        if self.current_index >= len(self.emails):
            return self.emails, 0.0, True, {}

        email = self.emails[self.current_index]
        email_text = email["text"]
        correct_label = email["label"]

        # Reward logic
        if action.lower() == correct_label:
            reward = 1.0
            print(f"Email {self.current_index + 1}: Correct")

        elif "meeting" in email_text.lower() and "attend" in action.lower():
            reward = 0.8
            print(f"Email {self.current_index + 1}: Good reply")

        else:
            reward = -0.5
            print(f"Email {self.current_index + 1}: Wrong")

        # Update state
        self.total_reward += reward
        self.current_index += 1

        done = self.current_index >= len(self.emails)

        # FINAL SCORE 
        if done:
            final_score = self.total_reward / len(self.emails)
            final_score = max(0.0, min(final_score, 1.0))  # normalize 0–1
            return self.emails, final_score, True, {}
        else:
            return self.emails, reward, False, {}

    def state(self):
        return self.emails

if __name__ == "__main__":
    env = EmailEnv()
    env.reset()

    print(env.step("important"))
    print(env.step("spam"))
    print(env.step("important"))

    print("Total Reward:", env.total_reward)
