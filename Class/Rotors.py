class Rotor:
    IC = 'DMTWSILRUYQNKFEJCAZBPGXOHV'
    IIC = 'HQZGPJTMOBLNCIFDYAWVEUSRKX'
    IIIC = 'UQNTLSZFMREHDPXKIBVYGJCWOA'
    I = 'JGDQOXUSCAMIFRVTPNEWKBLZYH'
    II = 'NTZPSFBOKMWRCJDIVLAEYUXHGQ'
    III = 'JVIUBHTCDYAKEQZPOSGXNRMWFL'
    IK = 'PEZUOHXSCVFMTBGLRINQJWAYDK'
    IIK = 'ZOUESYDKFWPCIQXHMVBLGNJRAT'
    IIIK = 'EHRVXGAOBQUSIMZFLYNWKTPDJC'
    I1930 = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
    II1930 = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
    III1930 = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
    IV1938 = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
    V1938 = 'VZBRGITYUPSDNHLXAWMJQOFECK'
    VI1939 = 'JPGVOUMFYQBENHZRDKASXLICTW'
    VII1939 = 'NZJHGRCXMYSWBOUFAIVLPEKQDT'
    VIII1939 = 'FKQHTLXOCBJSPDZRAMEWNIUYGV'

    @classmethod
    def get_rotor_list(self) -> tuple:
        return (
            self.IC,
            self.IIC,
            self.IIIC,
            self.I,
            self.II,
            self.III,
            self.IK,
            self.IIK,
            self.IIIK,
            self.I1930,
            self.II1930,
            self.III1930,
            self.IV1938,
            self.V1938,
            self.VI1939,
            self.VII1939,
            self.VIII1939,
        )


