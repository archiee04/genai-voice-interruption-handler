Gen-AI Voice Interruption Handler

Overview

Real-time voice agents often suffer from false interruptions because Voice Activity Detection (VAD) triggers before Speech-to-Text (STT) completes. Passive backchannels like “yeah” or “okay” unintentionally stop the agent mid-response.
This project implements semantic interruption handling by validating user intent after transcription instead of reacting immediately to sound detection.

Key Insight

1. VAD detects sound, not intent.
2. Interrupt decisions should be made only after semantic validation of the user’s speech.

Solution

The system introduces a lightweight interruption buffer:

1. VAD flags a potential interruption when user speech is detected  
2. Agent audio continues playing temporarily  
3. STT transcript is analyzed for semantic intent  
4. Agent speech is stopped only if an interrupt command is detected  

Passive backchannels are ignored.

Behavior

| Scenario | Result |
|--------|--------|
Agent speaking + “yeah” | Agent continues speaking |
Agent speaking + “stop” | Agent speech stops immediately |
Agent silent + user input | Input handled normally |

## Project Structure

agent/
├── state.py
├── vad_handler.py
├── stt_handler.py
├── interrupt_logic.py
├── tts_handler.py
config/
├── settings.py
main.py


Why This Approach Works
- Avoids modifying VAD or STT internals
- Adds no additional latency beyond STT processing
- Preserves natural conversational flow
- Clean separation of signal detection and semantic decision-making

Summary

This project demonstrates a practical Gen AI systems design approach to handle real time conversational interruptions using intent aware logic rather than raw signal detection.

Running the Demo

```bash
python main.py

Expected output:

[AGENT] Speaking...
[AGENT] Speech stopped.




