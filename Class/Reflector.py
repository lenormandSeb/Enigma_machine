class Reflector:
    UKW = 'QYHOGNECVPUZTFDJAXWMKISRBL'
    ETW = 'QWERTZUIOASDFGHJKPYXCVBNML'
    UKWK = 'IMETCGFRAYSQBZXWLHKDVUPOJN'
    ETWK = 'QWERTZUIOASDFGHJKPYXCVBNML'
    BETA = 'LEYJVCNIXWPBQMDRTAKZGFUHOS'
    GAMMA = 'FSOKANUERHMBTIYCWLQPZXVGJD'
    REFA = 'EJMZALYXVBWFCRQUONTSPIKHGD'
    REFB = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
    REFC = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'
    REFBTHIN = 'ENKQAUYWJICOPBLMDXZVFTHRGS'
    REFCTTHIN = 'RDOBJNTKVEHMLFCWZAXGYIPSUQ'
    REFETW = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    @classmethod
    def get_reflector_list(self) -> tuple:
        return (
            self.UKW,
            self.ETW,
            self.UKWK,
            self.ETWK,
            self.BETA,
            self.GAMMA,
            self.REFA,
            self.REFB,
            self.REFC,
            self.REFBTHIN,
            self.REFCTTHIN,
            self.REFETW,
        )

