from config.settings import IGNORE_WORDS, INTERRUPT_WORDS

def contains_interrupt_intent(text: str) -> bool:
    for word in INTERRUPT_WORDS:
        if word in text:
            return True
    return False

def is_passive_backchannel(text: str) -> bool:
    return text.strip() in IGNORE_WORDS
