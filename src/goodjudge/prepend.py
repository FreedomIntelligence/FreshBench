

def prepend(file_up_path, file_down_path,file_final_path):
    with open(file_up_path, 'r') as f:
        content_up = f.read()
    with open(file_down_path, 'r') as f:
        content_down = f.read()
    with open(file_final_path, 'w') as f:
        if content_up[-1] != '\n':
            content_up += '\n'
        f.write(content_up + content_down)
    



import argparse

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_up_path', type=str, required=True)
    parser.add_argument('--file_down_path', type=str, required=True)
    parser.add_argument('--file_final_path', type=str, required=True)
    args = parser.parse_args()
    prepend(args.file_up_path, args.file_down_path,args.file_final_path)
    
