class Adler32:
    def adler32(self, text_input: str) -> int:
        
        MOD_ADLER = 65521
        a = 1
        b = 0
        for input_chr in text_input:
            a = (a + ord(input_chr)) % MOD_ADLER
            b = (b + a) % MOD_ADLER
        
        return (b << 16) | a

