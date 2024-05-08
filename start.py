from   从 lingu    从语言进口国家import State


class   类 ListenState类ListenState(状态):(State):
       def __init__(自我):def __init__(self):
           超级（）.__init__（）super   __init__() 结束().__init__()
        self.   自我。Large_symbol = "👂"   “👂”large_symbol = "👂"   “👂”
        self.自我。Large_symbol_offset_x = 1large_symbol_offset_x = 1
        self.自我。Large_symbol_offset_y = 1large_symbol_offset_y = 1
        self.自我。Wake_word_activation_delay = 40wake_word_activation_delay = 40
        self.自我。End_of_speech_silence = 0.7end_of_speech_silence = 0.7
        self.   自我。is_mute = Falseis_muted = False   假
        self.   self   自我.language   语言 = “在”language = "en"   “en”
        self.Self   自我.interrupt_thresh = 20000interrupt_thresh = 20000


state =    状态 = ListenState（）ListenState()

