class EmailEnv:
    def __init__(self):
        self.emails = []
        self.current_index = 0
        self.total_reward = 0.0

    def reset(self):
        self.emails = [
            {"text": "Meeting at 5pm", "label": "important"},
            {"text": "Win lottery now!!!", "label": "spam"},
            {"text": "Project deadline tomorrow", "label": "important"}
        ]
        self.current_index = 0
        self.total_reward = 0.0
        return self.emails[self.current_index]

    def step(self, action):
        if not self.emails:
            raise RuntimeError("Call reset() before step()")

        if self.current_index >= len(self.emails):
            return None, 0.0, True, {"error": "Episode already done"}

        email = self.emails[self.current_index]
        email_text = email["text"]
        correct_label = email["label"]

        if action.lower() == correct_label:
            reward = 1.0
            print(f"Email {self.current_index + 1}: Correct")
        elif "meeting" in email_text.lower() and "attend" in action.lower():
            reward = 0.8
            print(f"Email {self.current_index + 1}: Good reply")
        else:
            reward = -0.5
            print(f"Email {self.current_index + 1}: Wrong")

        self.total_reward += reward
        self.current_index += 1
        done = self.current_index >= len(self.emails)

        if done:
            final_score = self.total_reward / len(self.emails)
            final_score = max(0.0, min(final_score, 1.0))
            return None, final_score, True, {"final_score": final_score}
        else:
            return self.emails[self.current_index], reward, False, {}

    def state(self):
        if self.current_index < len(self.emails):
            return self.emails[self.current_index]
        return None


if __name__ == "__main__":
    env = EmailEnv()
    env.reset()
    print(env.step("important"))
    print(env.step("spam"))
    print(env.step("important"))
    print("Total Reward:", env.total_reward)
