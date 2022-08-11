import csv
import pandas as pd 
from evc import EVC

class ParserEvc():

    def __init__(self,path):
        self.__path = path


    def output_to_txt(self,output): 
        with open(f"TXTs/{self.__path}temp.txt", "w") as arquivo:
            arquivo.write(output)

    def get_parameters_from_txt(self):
        parameters_lines = []
        with open(f'TXTs/{self.__path}temp.txt') as temp:

            lines = temp.readlines()
            
            for line in range(len(lines)):
                if line > 21 and line < (len(lines)-13) and line%2 == 0 and lines[line].split()[0].isnumeric(): 
                    original_tuple = lines[line].split()
                    new_list = ([original_tuple[0]]+original_tuple[2:9])
                    parameters_lines.append((new_list))

        return parameters_lines

    def txt_to_csv(self,parameters):
        with open(f'CSVs/{self.__path}parameters_frames.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            for line in parameters:
                spamwriter.writerow(line)
        df = pd.read_csv(f'CSVs/{self.__path}parameters_frames.csv', header = None)
        df.to_csv(f'CSVs/{self.__path}parameters_frames.csv', header=['POC', 'Ftype', 'QP', 'PSNR-Y','PSNR-U','PSNR-V','Bits','EncT(ms)'],index=False)
        
out = EVC('fast').encode('carphone_qcif.y4m','carphone.evc')
n = ParserEvc(input('Digite o nome do arquivo:'))
n.output_to_txt(out)
a = n.get_parameters_from_txt()
n.txt_to_csv(a)




