

def prepend(file_up_path, file_down_path,file_final_path,specific_strategy=None):
    with open(file_up_path, 'r',encoding='utf-8') as f:
        content_up = f.read()
    with open(file_down_path, 'r',encoding='utf-8') as f:
        # breakpoint()
        
        if specific_strategy == 'del_down_first_line':
            breakpoint()
            content_down = f.read().split('\n',1)[1]
        else:
            content_down = f.read()
    with open(file_final_path, 'w',encoding='utf-8') as f:
        if content_up[-1] != '\n':
            content_up += '\n'
        f.write(content_up + content_down)
    



import argparse

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_up_path', type=str, required=True)
    parser.add_argument('--file_down_path', type=str, required=True)
    parser.add_argument('--file_final_path', type=str, required=True)
    parser.add_argument('--specific_strategy', type=str, default=None)
    args = parser.parse_args()
    prepend(args.file_up_path, args.file_down_path,args.file_final_path,args.specific_strategy)
    
