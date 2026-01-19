from agent.state import state

def start_agent_audio():
    state.agent_is_speaking = True
    print("[AGENT] Speaking...")

def stop_agent_audio():
    state.agent_is_speaking = False
    print("[AGENT] Speech stopped.")
