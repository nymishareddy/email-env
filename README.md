# Email Management OpenEnv

## Description
This environment simulates an email management system where an AI agent classifies and responds to emails.

## Tasks
- Easy: classify email as important or spam
- Medium: generate appropriate reply
- Hard: process multiple emails sequentially

## Action Space
String (classification or reply)

## Observation Space
List of emails with text and labels

## Reward
- Correct classification: +1
- Good reply: +0.8
- Wrong: -0.5

## How to Run

```bash
python env.py
python inference.py