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
        if self.current_index >= len(self.emails):
            return self.emails, self.total_reward, True, {}

        email = self.emails[self.current_index]
        email_text = email["text"]
        correct_label = email["label"]

        if action.lower() == correct_label:
            reward = 1.0
            print(f"Email {self.current_index + 1}: Correct ✅")

        elif "meeting" in email_text.lower() and "attend" in action.lower():
            reward = 0.8
            print(f"Email {self.current_index + 1}: Good reply ✉️")

        else:
            reward = -0.5
            print(f"Email {self.current_index + 1}: Wrong ❌")

        self.total_reward += reward
        self.current_index += 1

        done = self.current_index >= len(self.emails)

        return self.emails, reward, done, {}

    def state(self):
        return self.emails


# Testing
if __name__ == "__main__":
    env = EmailEnv()
    env.reset()

    print(env.step("important"))
    print(env.step("spam"))
    print(env.step("important"))

    print("Total Reward:", env.total_reward)