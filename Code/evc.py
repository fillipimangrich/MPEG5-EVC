import os

class EVC():

    def __init__(self,preset):
        self.__preset = preset


    def encode(self,input,output):

        os.system(f'xeve_app -i RAW_files/{input} -v 3 --preset {self.__preset} -o encoded_files/{output} > TXTs/{input}temp.txt')


    def decode(self,input,output):
        
        os.system(f'xevd_app -i encoded_files/{input} -o decoded_files/{self.__preset}_{output}')

