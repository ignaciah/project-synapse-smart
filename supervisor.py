# backend/app/agents/supervisor.py

import google.generativeai as genai
import os

# 1. You just paste the key you copied from AI Studio here
genai.configure(api_key=os.getenv( AIzaSyCZU5AMGAceTklXuS94whygBPZMwls45vY)) 

class CrisisSupervisor:
    def __init__(self):
        # 2. Use the latest flash model (fast and free)
        self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    def decide(self, emergency_event):
        # 3. Your unified supervisor prompt goes here
        response = self.model.generate_content(SUPERVISOR_PROMPT = """
You are the Crisis Supervisor AI for a smart city. You have authority over:
- Traffic Agent (controls intersections, reroutes vehicles)
- Grid Agent (manages power distribution)
- Emergency Services (coordinates response)

CURRENT CITY STATE:
{traffic_data}
{grid_data}
{active_alerts}

INPUT: {emergency_event}

Your task: Output a JSON decision with these fields:
{{
    "emergency_type": "string",
    "severity": "critical|high|medium|low",
    "immediate_action": {{
        "traffic": "clear_route|hold_all|reroute_around",
        "power": "surge_hospitals|maintain|reduce_noncritical",
        "evacuation_zones": ["zone1", "zone2"]
    }},
    "reasoning": "Step-by-step explanation",
    "revert_after_minutes": 10
}}

ETHICAL CONSTRAINTS:
- NEVER depower hospitals to save energy
- Always prioritize human life over traffic efficiency
- If uncertain, escalate to human operator

Respond with ONLY valid JSON.
"""
)
        return response.text
