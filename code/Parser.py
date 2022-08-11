import csv
from pickletools import read_long1
import pandas as pd 
import re
class ParserEvc():

    def __init__(self,path):
        self.__path = path

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self,path):
        self.__path = path

    def regex_find(self,input):
        pattern = re.compile(r"\d+\s+\d{0,4}\s+\([IB]\)\s+\d+\s+\d+\.\d+\s+\d+\.\d+\s+\d+\.\d+\s+\d+\s+\d+")
        return pattern.findall(input)

    def output_to_txt(self,output): 
        with open(f"TXTs/{self.__path}temp.txt", "w") as arquivo:
            arquivo.write(output)

    def get_parameters_from_txt(self):
        parameters_lines = []
        with open(f'TXTs/{self.__path}temp.txt') as temp:
            text = temp.read()
            re_list = self.regex_find(text)
            for line in range(len(re_list)):
                    original_tuple = re_list[line].split()
                    new_list = ([int(original_tuple[0])]+[original_tuple[2][1]]+original_tuple[3:9])
                    parameters_lines.append((new_list))

        return sorted(parameters_lines)

    def txt_to_csv(self,parameters):
        with open(f'CSVs/{self.__path}parameters_frames.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            for line in parameters:
                spamwriter.writerow(line)
        df = pd.read_csv(f'CSVs/{self.__path}parameters_frames.csv', header = None)
        df.to_csv(f'CSVs/{self.__path}parameters_frames.csv', header=['POC', 'Ftype', 'QP', 'PSNR-Y','PSNR-U','PSNR-V','Bits','EncT(ms)'],index=False)
        





