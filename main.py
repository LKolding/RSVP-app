import sys  #for sys.argv

from GUI import Application
from text_engine import TextEngine


def main():
    global timeout
    timeout = 1.0  #seconds
    
    TEXT:str
    
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
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
    
    
    def logic() -> None:
        global timeout
        
        update_progress_bar()
        
        # Reset
        if app._app_window.should_reset:
            engine.reset()
            timeout = update_word_and_get_timeout()
            update_progress_bar()
            app._app_window.should_reset = not app._app_window.should_reset
        
        # Pause/unpause
        if not app._app_window.isPaused:
            timeout = update_word_and_get_timeout()
            app._app_window._wordDisplay.after( int(timeout*1000), logic)
        
        
    logic()
    app.mainloop()
        

if __name__=="__main__":
    main()  #entrypoint