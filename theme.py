class Theme:
    Coral = [(112,162,163), (177,228,185)]
    Dusk = [(112,102,119), (204,183,174)]
    Marine = [(111,115,210), (157,172,255)]
    Wheat = [(187,190,100), (234,240,206)]
    Emerald = [(111,143,114), (173,189,143)]
    Sandcastle = [(184,139,74), (227,193,111)]
    DarkLight = [(232, 235, 239), (125, 135, 150)]
    

    num = 7

    @classmethod
    def get_theme(cls, i):
        return [cls.DarkLight, cls.Coral, cls.Dusk, cls.Marine, cls.Wheat, cls.Emerald, cls.Sandcastle][i]