from utils.json_functions import get_settings

class TextEngine:
    def __init__(self, text:str):
        self._words = text.split()
        self._iterator: int = 0
        self._settings: dict = get_settings()
        
    def next(self) -> tuple[str, float]:
        word = self._words[self._iterator]
        word_dur = self._get_word_duration(word)
        
        self._iterator += 1 if self._iterator+1 < len(self._words) else -self._iterator#<- loop
        return (word, word_dur)

    def reset(self) -> None:
        self._iterator = 0
        new_settings = get_settings()
        if self._settings != new_settings:
            self._settings = new_settings

    def _get_word_duration(self, word) -> float:
        if '.' in word[-1]:
            return (self._settings['timeouts']['full_stop'])

        if ';' in word[-3:]:
            return (self._settings['timeouts']['semicolon'])

        elif ',' in word[-3:]:
            return (self._settings['timeouts']['comma'])

        elif ':' in word[-3:]:
            return (self._settings['timeouts']['colon'])

        elif '\n' in word[-3:]:
            return (self._settings['timeouts']['newline'])

        else:
            return (self._settings['timeouts']['default'])
