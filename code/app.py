from evc import EVC
import os
from Parser import ParserEvc
from Editor import Editor

preset = 'fast'
codec = EVC(preset)
parser = ParserEvc('carphone')
editor = Editor()

for root, dirs, files in os.walk("RAW_files"):
    for file in files:
        parser.path= file

        out = codec.encode(file,f'{file[:-3]}.evc')

        codec.decode(f'{file[:-3]}.evc',file)

        parser.output_to_txt(out)

        a = parser.get_parameters_from_txt()

        parser.txt_to_csv(a)

        a_frames = editor.get_frames(f'RAW_files/{file}',[0,10,20,30,40,50,60])
        b_frames = editor.get_frames(f'decoded_files/{preset}_{file}',[0,10,20,30,40,50,60])

        for i in range(len(a_frames)):
            a = editor.add_border_and_text(a_frames[i],'Original')
            b = editor.add_border_and_text(b_frames[i],'Compressed')
            concatenated_image = editor.concatenate(a,b)
            editor.save(concatenated_image,f'{file}',f'{file[:-3]}_{i}')