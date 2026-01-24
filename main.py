import sys  #for sys.argv

from gui.GUI import Application
from text_engine import TextEngine


def main():

    global _timeout
    _timeout = 1.0  # seconds
    
    # WPM calculation variables
    global _total_timeout
    _total_timeout = 0
    global _words_amount
    _words_amount = 0

    TEXT:str
    
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding="utf-8") as f:
            TEXT = f.read()
    else:
        TEXT = 'the quick brown fox jumps over the lazy dog'
    
    
    app = Application()
    engine = TextEngine(TEXT)
    
    
    # Pause on <space>
    def pause_event_handler(_):
        app._app_window._togglePause()
        logic()
    app.bind("<space>", pause_event_handler)
    
    
    def update_word_and_get_timeout() -> float:

        word, timeout = engine.next()
        app._app_window._wordDisplay.set_word(word)
        return timeout
    
    
    def update_progress_bar() -> None:

        app._app_window._progressIntVar.set(round(engine._iterator / len(engine._words)*100 ))
    
    
    def calculate_wpm(timeout:float) -> int:

        global _total_timeout  # float: in seconds
        global _words_amount   # int: amount of words

        _total_timeout += timeout
        _words_amount  += 1

        wpm = (_words_amount / _total_timeout) * 60
        return int(wpm)


    def logic() -> None:

        global _timeout
        
        # Reset
        if app._app_window._should_reset:

            engine.reset()
            _timeout = update_word_and_get_timeout()
            update_progress_bar()
            app._app_window._should_reset = not app._app_window._should_reset
        
        # Pause/unpause
        if not app._app_window._isPaused:

            # Get new word and timeout
            _timeout = update_word_and_get_timeout()
            app._app_window._wordDisplay.after( int(_timeout*1000), logic)
            
            # Calculate wpm and update IntVar
            wpm:int = calculate_wpm(_timeout)
            app._app_window._current_wpm.set(f'WPM: {wpm}')

            update_progress_bar()
        
        
    logic()
    app.mainloop()
        

if __name__=="__main__":
    main()  #entrypoint