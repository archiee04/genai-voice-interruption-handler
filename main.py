from agent.tts_handler import start_agent_audio
from agent.vad_handler import on_user_speech_start
from agent.stt_handler import on_stt_final

start_agent_audio()
on_user_speech_start()
on_stt_final("yeah")
on_user_speech_start()
on_stt_final("stop")
