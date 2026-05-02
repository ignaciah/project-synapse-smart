# project-synapse-smart
Project Synapse is an Autonomous Urban Operating System that turns a city into a living organism. When emergencies happen (earthquake, fire, accident), AI agents instantly coordinate traffic, power grid, and emergency services across departmental silos.
## 🏗️ Architecture

```

┌─────────────────────────────────────────────────────────┐
│                    Frontend (Next.js + Mapbox)          │
│                  Real-time Digital Twin                 │
└─────────────────────────────────────────────────────────┘
▲
│ WebSocket (Real-time)
▼
┌─────────────────────────────────────────────────────────┐
│              FastAPI Backend + LangGraph                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │ Traffic  │  │   Grid   │  │  Crisis  │              │
│  │  Agent   │◄─►│  Agent   │◄─►│ Supervisor│             │
│  └──────────┘  └──────────┘  └──────────┘              │
└─────────────────────────────────────────────────────────┘
▲
│
┌─────────────────────────────────────────────────────────┐
│              Simulated IoT Data (100 virtual sensors)   │
└─────────────────────────────────────────────────────────┘

├── backend/
│   ├── app/
│   │   ├── agents/          # LangGraph AI agents
│   │   ├── sim/             # Fake IoT data generator
│   │   ├── routes/          # API endpoints
│   │   └── main.py          # FastAPI entry point
│   └── requirements.txt
├── frontend/
│   ├── pages/               # Next.js routes
│   ├── components/          # React components
│   └── package.json
└── demo/                    # Screen recordings
```

🔑 Environment Variables

Copy .env.example to .env and fill in:

```env
GOOGLE_MAPS_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
MAPBOX_TOKEN=your_token_here
```
