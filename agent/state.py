class AgentState:
    def __init__(self):
        self.agent_is_speaking = False
        self.pending_interrupt = False

state = AgentState()
