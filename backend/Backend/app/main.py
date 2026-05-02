from agents.supervisor import CrisisSupervisor
import random

# Initialize your AI supervisor
supervisor = CrisisSupervisor()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    # Simulated data (in real hackathon, this comes from sensors)
    traffic_data = {"congestion_zones": ["Zone_A"], "avg_speed": 45}
    grid_data = {"load_percentage": 72, "hospitals_online": 3}
    
    while True:
        # Simulate an emergency event
        emergency = {
            "type": random.choice(["fire", "accident", "earthquake"]),
            "location": "Downtown",
            "severity": "high",
            "description": "Multi-vehicle collision on Main Street"
        }
        
        # 🚀 THIS IS WHERE YOU USE THE UNIFIED PROMPT
        ai_decision = supervisor.decide(
            emergency_event=emergency,
            traffic_data=traffic_data,
            grid_data=grid_data
        )
        
        # Send decision to frontend
        await websocket.send_json({
            "type": "ai_decision",
            "decision": ai_decision
        })
        
        await asyncio.sleep(10)  # Check every 10 seconds
