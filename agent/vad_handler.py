import threading
from agent.state import state
from config.settings import INTERRUPT_DECISION_DELAY_MS

def on_user_speech_start():
    if state.agent_is_speaking:
        state.pending_interrupt = True
        threading.Timer(
            INTERRUPT_DECISION_DELAY_MS / 1000,
            clear_pending_if_unused
        ).start()

def clear_pending_if_unused():
    if state.pending_interrupt:
        state.pending_interrupt = False
