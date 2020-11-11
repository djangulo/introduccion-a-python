#!/usr/bin/python3
import time
from tkinter import (
    Frame,
    Tk,
    StringVar,
    Label,
    X,
    NO,
    TOP,
    LEFT,
    Button,
)

class StopWatch(Frame):  
    """Implementación de un cronómetro."""                                                                
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()               
        self.make_widgets()      

    def make_widgets(self):                         
        """Crea el reloj."""
        l = Label(self, textvariable=self.timestr)
        self._set_time(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=2, padx=2)                      
    
    def _update(self): 
        """Actualiza el reloj con el tiempo."""
        self._elapsedtime = time.time() - self._start
        self._set_time(self._elapsedtime)
        self._timer = self.after(50, self._update)
    
    def _set_time(self, elap):
        """Se encarga de dar formato al reloj en minutors:segundos:cencesimas."""
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))
        
    def start(self):                                                     
        """Arranca el cronómetro."""
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1        
    
    def stop(self):                                    
        """Detiene el cronómetro."""
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._set_time(self._elapsedtime)
            self._running = 0
    
    def reset(self):                                  
        """Detiene el cronómetro."""
        self._start = time.time()         
        self._elapsedtime = 0.0    
        self._set_time(self._elapsedtime)
        
        
def main():
    root = Tk()
    sw = StopWatch(root)
    sw.pack(side=TOP)
    
    Button(root, text='Iniciar', command=sw.start).pack(side=LEFT)
    Button(root, text='Detener', command=sw.stop).pack(side=LEFT)
    Button(root, text='Reinicio', command=sw.reset).pack(side=LEFT)
    Button(root, text='Cerrar', command=root.quit).pack(side=LEFT)
    
    root.mainloop()

if __name__ == '__main__':
    main()
