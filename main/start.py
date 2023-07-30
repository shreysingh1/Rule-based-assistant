from process_module import process
from output_module import output
import os
from input_module import take_input
from welcome import wishme
os.system("cls")
wishme()

while(True):
    i = take_input()
    o = process(i)
    output(o)




