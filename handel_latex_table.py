
from reorder import reorder
from standard_name import parse_possible_name



import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--txt_path', type=str, default='path_to/gpt4_distil/analysis/complex_acc_latex/latex_gray.txt')
args=parser.parse_args()
txt_path=args.txt_path
# txt_path='path_to/gpt4_distil/analysis/complex_acc_latex/latex_gray.txt'

with open(txt_path,'r') as f:
    sss=f.read()
    sss_list=sss.split('\n')

    std_name=parse_possible_name(sss.replace('nan','-'))
    std_list=std_name.split('\n')

    print(len(sss_list),len(std_list),len(std_list[2:-3]))
    content='\n'.join(std_list[4:-3])
    content_ordered=reorder(std_name)
    cc=content_ordered.split('\n')
    whole=std_list[0]+'\n'+std_list[1]+'\n'+std_list[2]+'\n'+std_list[3]+'\n'+content_ordered+'\n'+std_list[-3]+'\n'+std_list[-2]+'\n'+std_list[-1]
    print(whole)
    with open(txt_path,'w') as f:
        f.write(whole)


'''


'''