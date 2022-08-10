import subprocess


class evc_Decoder():

    def __init__(self):
        pass

    def decode(self,arquivo,saida):
        
        subprocess.run(['xevd_app','-i',f'encoded_files/{arquivo}','-o',f'decoded_files/{saida}'])