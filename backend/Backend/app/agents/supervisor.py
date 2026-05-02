Import google.generativeai as genai
import os
import json
from typing import Dict, List
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class CrisisSupervisor:
    def __init__(self):
        # Use Gemini 2.0 Flash or Pro
        self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
    def decide(self, emergency_event: Dict, traffic_data: Dict, grid_data: Dict) -> Dict:
        """The MAIN function where your prompt goes"""
        
        # 👇 YOUR UNIFIED SUPERVISOR PROMPT - This is where it lives!
        supervisor_prompt = f"""
You are the Crisis Supervisor AI for a smart city. You have authority over:
- Traffic Agent (controls intersections, reroutes vehicles)
- Grid Agent (manages power distribution)
- Emergency Services (coordinates response)

CURRENT CITY STATE:
Traffic Data: {json.dumps(traffic_data, indent=2)}
Grid Data: {json.dumps(grid_data, indent=2)}
Active Alerts: {emergency_event.get('description', 'None')}

INPUT: {json.dumps(emergency_event, indent=2)}

Your task: Output a JSON decision with these fields:
{{
    "emergency_type": "string",
    "severity": "critical|high|medium|low",
    "affected_zones": ["zone1", "zone2"],
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
- If uncertain, escalate to human operator by setting "uncertain": true

Respond with ONLY valid JSON. No explanations outside JSON.
"""
        
        # Send prompt to Gemini
        response = self.model.generate_content(supervisor_prompt)
        
        # Parse Gemini's response
        try:
            # Clean response (remove markdown code blocks if present)
            clean_response = response.text.replace('```json', '').replace('```', '').strip()
            decision = json.loads(clean_response)
            return decision
        except json.JSONDecodeError:
            # Fallback if Gemini gives bad JSON
            return {
                "emergency_type": "unknown",
                "severity": "high",
                "immediate_action": {"traffic": "hold_all", "power": "maintain"},
                "reasoning": "AI response parsing failed, using safe defaults",
                "uncertain": True
            }
