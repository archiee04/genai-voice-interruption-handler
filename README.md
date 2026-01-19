# Gen-AI Voice Interruption Handler

## Overview
Real-time Gen-AI voice agents often suffer from false interruptions because Voice Activity Detection (VAD) triggers before Speech-to-Text (STT) processing completes. Passive backchannels like “yeah” or “okay” unintentionally interrupt the agent mid-response.

This project demonstrates an **intent-aware interruption handling mechanism** that validates user intent after transcription instead of reacting immediately to sound detection.

---

## Core Insight
VAD detects **sound**, not **intent**.

Interruption decisions should be made only after semantic validation of the user’s speech.

---

## Solution Approach
The system introduces a lightweight **interruption buffer**:

1. VAD flags a *potential* interruption when user speech is detected  
2. Agent audio continues playing temporarily  
3. STT transcript is analyzed for semantic intent  
4. Agent speech is stopped **only** if an interrupt command is detected  

Passive backchannels are ignored.

---

## Expected Behavior

| Scenario | Result |
|--------|--------|
Agent speaking + “yeah” | Agent continues speaking |
Agent speaking + “stop” | Agent speech stops immediately |
Agent silent + user input | Input handled normally |

---

## Project Structure
```
agent/
├── state.py            # Tracks agent speaking state
├── vad_handler.py      # Handles VAD events
├── stt_handler.py      # Processes STT results
├── interrupt_logic.py  # Semantic intent detection
├── tts_handler.py      # Agent audio control
config/
├── settings.py         # Configurable parameters
main.py                 # Demo entry point
```

## Why This Approach Works
- Avoids modifying VAD or STT internals
- Adds no additional latency beyond STT processing
- Preserves natural conversational flow
- Clean separation of signal detection and semantic decision-making

---

## Running the Demo
```bash
python main.py
[AGENT] Speaking...
[AGENT] Speech stopped.

