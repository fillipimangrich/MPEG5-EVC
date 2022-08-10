import subprocess

class evc_Encoder():

    def __init__(self,preset):
        self.__preset = preset


    def encode(self,input,output):

        process = subprocess.run(['xeve_app','-i',f'RAW_files/{input}','-v','3','--preset',self.__preset,'-o',f'encoded_files/{output}'],capture_output = True)

        stdout = process.stdout

        return stdout.decode('utf-8')