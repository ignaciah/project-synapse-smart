# backend/app/agents/supervisor.py

import google.generativeai as genai
import os

# 1. You just paste the key you copied from AI Studio here
genai.configure(api_key=os.getenv("GEMINI_API_KEY")) 

class CrisisSupervisor:
    def __init__(self):
        # 2. Use the latest flash model (fast and free)
        self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    def decide(self, emergency_event):
        # 3. Your unified supervisor prompt goes here
        response = self.model.generate_content(YOUR_PROMPT)
        return response.text
