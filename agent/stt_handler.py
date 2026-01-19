from agent.state import state
from agent.interrupt_logic import contains_interrupt_intent, is_passive_backchannel
from agent.tts_handler import stop_agent_audio

def on_stt_final(transcript: str):
    text = transcript.lower().strip()

    if state.agent_is_speaking and state.pending_interrupt:
        if contains_interrupt_intent(text):
            stop_agent_audio()
        elif is_passive_backchannel(text):
            pass
        state.pending_interrupt = False

    elif not state.agent_is_speaking:
        handle_user_input(text)

def handle_user_input(text: str):
    print(f"[USER INPUT ACCEPTED]: {text}")
