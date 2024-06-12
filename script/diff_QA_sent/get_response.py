    
import os
def merge_files(result_output_dir,output_file_name=None):
    files = os.listdir(result_output_dir)
    files = [file for file in files if file.endswith('.json')]
    filenames = sorted(files,key=lambda x:int(x.split('.')[0]))
    # breakpoint()
    generated_instructions = [open(os.path.join(result_output_dir, filename), encoding="utf-8").read() for
                                filename
                                in filenames]
    texts = "\n".join(generated_instructions)
    # if output_file_name is None:
    #     if self.end is None:
    #         output_file_name = str(start) + "_" + str(len(self.sample_list) - self.start) + ".jsonl"
    #     else:
    #         output_file_name = str(self.start) + "_" + str(self.end) + ".jsonl"
    with open(output_file_name, "w", encoding="utf-8") as f:
        f.write(texts)
result_output_dir = "test/20240526/gjo_gpt_answer/mistralai/mixtral-8x22b-instruct/gjo_transformed_questions_no_output"
output_file_name = "test/20240526/gjo_gpt_answer/mistralai/mixtral-8x22b-instruct/response/gjo_with_output.json"

merge_files(result_output_dir,output_file_name)