# this file is to filter the name of models in Freshbench, latex overleaf
import re
def parse_possible_name(given_name:str)->str:

    # breakpoint()

    # if a 'b' are following a number, uppercase it

    if 'b' in given_name:
        given_name = re.sub(r'(\d)b', r'\1B', given_name)
    if 'base' in given_name:
        given_name = given_name.replace('base','Base')
    if 'chat' in given_name:
        given_name = given_name.replace('chat','Chat')

    if r'\_' in given_name:
        given_name = given_name.replace(r'\_','_')

    if 'HF_RWKV_v5-Eagle-7B' in given_name:
        given_name = given_name.replace('HF_RWKV_v5-Eagle-7B','RWKV-v5-Eagle-7B')
    if 'hf' in given_name.lower():
        given_name = given_name.replace('-hf','')
        given_name = given_name.replace('_hf','')
        given_name = given_name.replace('HF_','')
    hf_dic={}
    if given_name in hf_dic.keys():
        given_name=given_name.replace(given_name,hf_dic[given_name])
    # if 'llama_hf_7b' in given_name:
    #     given_name=given_name.replace('llama_hf_7b','LlaMA-7B')
    
    given_name=given_name.replace('%',r'/%')

    if 'chatglm' in given_name:
        given_name=given_name.replace('chatglm','ChatGLM')
    if 'Chatglm' in given_name:
        given_name=given_name.replace('Chatglm','ChatGLM')
    if '1_8' in given_name:
        given_name=given_name.replace('1_8','1.8')
    if 'phi' in given_name:
        if 'phi-1_5' in given_name:
            given_name=given_name.replace('phi-1_5','Phi-1.5')
        given_name=given_name.replace('phi','Phi')
    if 'llama' in given_name.lower():
        if 'llama_hf_7b' in given_name:
            breakpoint()
            given_name=given_name.replace('llama_hf_7b','LLaMA-7B')
        given_name=given_name.replace('llama','LLaMA')
    if 'mistral' in given_name.lower():
        given_name=given_name.replace('mistral','Mistral')
    if 'baichuan' in given_name.lower():
        given_name=given_name.replace('baichuan','Baichuan')
    if 'zephyr' in given_name.lower():
        given_name=given_name.replace('zephyr','Zephyr')
    if 'internlm' in given_name.lower():
        given_name=given_name.replace('internlm','InternLM')
    if 'opt' in given_name.lower():
        given_name=given_name.replace('opt','OPT')
    if 'pythia' in given_name.lower():
        given_name=given_name.replace('pythia','Pythia')
    if 'mamba' in given_name.lower():
        given_name=given_name.replace('mamba','Mamba')
    if 'vicuna' in given_name.lower():
        given_name=given_name.replace('vicuna','Vicuna')
    if 'zhongjing' in given_name.lower():
        given_name=given_name.replace('zhongjing','Zhongjing')
    if 'falcon' in given_name.lower():
        given_name=given_name.replace('falcon','Falcon')
    if 'command-r-plus' in given_name:
        given_name=given_name.replace('command-r-plus','Command R+')
    if 'gpt4_0613' in given_name:
        given_name=given_name.replace('gpt4_0613','GPT-4-230613')
    if 'instruct' in given_name:
        given_name=given_name.replace('instruct','Instruct')

    



    # if 'RWKV-5-World-3B' in given_name:
    #     return 'RWKV-5-World-3B'
    # if 'RWKV-5-World-1B5' in given_name:
    #     return 'RWKV-5-World-1B5'
    
    if 'gpt' in given_name:
        if 'gpt_3.5_turbo_0613' in given_name:
            given_name=given_name.replace('gpt_3.5_turbo_0613','GPT-3.5-turbo-230613')
        if 'gpt4_1106' in given_name:
            given_name=given_name.replace('gpt4_1106','GPT-4-231106')
        # else:
            # raise ValueError(f'gpt model name not recognized {given_name}')
        # return given_name.replace('gpt','GPT')


    # breakpoint()
    if 'LLaMA_7B' in given_name:
        given_name=given_name.replace('LLaMA_7B','LLaMA-7B')
    
    return given_name


# import re

# def parse_possible_name(given_name: str) -> str:
#     original_name = given_name  # Store original name for comparison later

#     # Uppercase 'b' following a number
#     if 'b' in given_name:
#         given_name, num_subs = re.subn(r'(\d)b', r'\1B', given_name)
#         if num_subs > 0:
#             print(f"Replaced 'b' after number: {original_name} -> {given_name}")

#     # Replace 'base' with 'Base'
#     if 'base' in given_name:
#         given_name = given_name.replace('base', 'Base')
#         print(f"Replaced 'base' with 'Base': {original_name} -> {given_name}")

#     # Replace 'chat' with 'Chat', except when part of 'glm'
#     if 'chat' in given_name and 'glm' not in given_name.lower():
#         given_name = given_name.replace('chat', 'Chat')
#         print(f"Replaced 'chat' with 'Chat': {original_name} -> {given_name}")

#     # Specific replacements
#     if 'HF_RWKV_v5-Eagle-7B' == given_name:
#         return 'RWKV5-7B'

#     if 'hf' in given_name.lower():
#         given_name = re.sub(r'(-hf|_hf|HF_)', '', given_name)
#         print(f"Removed 'hf' from model name: {original_name} -> {given_name}")
#         return given_name

#     # Dictionary replacement
#     hf_dic = {}
#     if given_name in hf_dic:
#         return hf_dic[given_name]

#     # Other specific rules
#     patterns = {
#         'chatglm': 'ChatGLM',
#         'phi': 'Phi',
#         'llama': 'LLaMA',
#         'mistral': 'Mistral',
#         'baichuan': 'Baichuan',
#         'zephyr': 'Zephyr',
#         'internlm': 'InternLM',
#         'opt': 'OPT',
#         'pythia': 'Pythia',
#         'mamba': 'Mamba'
#     }
    
#     for pattern, replacement in patterns.items():
#         if pattern in given_name.lower():
#             given_name = re.sub(pattern, replacement, given_name, flags=re.IGNORECASE)
#             print(f"Replaced '{pattern}' with '{replacement}': {original_name} -> {given_name}")
#             return given_name

#     # RWKV model specific cases
#     if 'RWKV-5-World-3B' in given_name:
#         return 'RWKV-5-World-3B'
#     if 'RWKV-5-World-1B5' in given_name:
#         return 'RWKV-5-World-1B5'
    
#     # GPT models
#     if 'gpt' in given_name:
#         if 'gpt_3.5' in given_name:
#             return 'GPT-3.5'
#         if 'gpt4' in given_name:
#             given_name = 'GPT-4'
#             print(f"Replaced 'gpt4' with 'GPT-4': {original_name} -> {given_name}")
#             return given_name
#         raise ValueError(f'GPT model name not recognized: {given_name}')
    
#     return given_name

# # Example usage
# modified_name = parse_possible_name("gpt4_example_model")
# print("Final Modified Name:", modified_name)






sss=r'''\begin{tabular}{llllll}
\toprule
 & Base ppl & ppl Change at 3 months (%) & ppl Change at 6 months (%) & ppl Change at 9 months (%) & ppl Change at 12 months (%) \\
model &  &  &  &  &  \\
\midrule
Baichuan2-13B-Base & 0.875 & 0.463 & 1.302 & nan & nan \\
Baichuan2-13B-Chat & 0.998 & -0.392 & 0.214 & 0.101 & nan \\
Baichuan2-7B-Base & 0.902 & 0.097 & 1.017 & nan & nan \\
Baichuan2-7B-Chat & 1.058 & 0.207 & 0.162 & nan & nan \\
Colossal-LLaMA-2-7b-base & 1.073 & 0.780 & -1.428 & nan & nan \\
HF_RWKV_v5-Eagle-7B & 0.912 & 2.179 & nan & nan & nan \\
Llama-2-13b-hf & 0.784 & 0.544 & 1.132 & nan & nan \\
Llama-2-7b-hf & 0.821 & 0.415 & 0.960 & nan & nan \\
Qwen-14B-Chat & 0.933 & 0.372 & 4.205 & nan & nan \\
Qwen-1_8B & 1.164 & -0.742 & nan & nan & nan \\
Qwen-1_8B-Chat & 1.361 & -1.852 & nan & nan & nan \\
Qwen-7B & 0.953 & 0.759 & 3.508 & nan & nan \\
Qwen-7B-Chat & 1.014 & 0.859 & 4.069 & nan & nan \\
Skywork-13B-base & 0.831 & 0.390 & nan & nan & nan \\
TinyLlama-1.1B-Chat-v0.6 & 1.008 & -1.333 & nan & nan & nan \\
Yi-6B & 0.881 & 0.398 & nan & nan & nan \\
Yi-6B-Chat & 0.907 & 1.821 & nan & nan & nan \\
baichuan-13b-chat & 0.894 & 0.045 & -0.219 & 0.821 & nan \\
baichuan-7b-chat & 0.975 & -0.132 & 1.033 & nan & nan \\
chatglm3-6b & 1.458 & -1.149 & nan & nan & nan \\
falcon-rw-1b & 1.130 & -1.857 & -2.607 & -2.138 & nan \\
internlm-chat-7b & 1.100 & 0.192 & 0.310 & nan & nan \\
llama2-7b-chat-hf & 1.002 & 1.118 & 0.221 & nan & nan \\
llama_hf_7b & 0.848 & -0.090 & 0.013 & -0.013 & 0.823 \\
mistral-7b-v0.1 & 0.787 & 0.331 & 2.139 & nan & nan \\
opt-13b & 1.133 & nan & -1.089 & -2.021 & -5.130 \\
opt-2.7b & 1.226 & nan & -0.961 & -2.266 & -5.406 \\
phi-1_5 & 1.282 & -1.052 & -4.342 & nan & nan \\
phi-2 & 1.065 & -2.429 & nan & nan & nan \\
pythia-12b & 0.988 & -0.061 & 0.145 & 0.207 & 1.468 \\
vicuna-7b-v1.5 & 0.927 & 0.189 & 0.405 & nan & nan \\
zephyr-7b-beta & 0.881 & -0.009 & nan & nan & nan \\
zhongjing-base & 0.894 & 1.229 & 1.036 & nan & nan \\
\bottomrule
\end{tabular}'''



sss=r'''
\begin{tabular}{llllllllll}
\toprule
 & Base Accuracy & Mean Acc at 3 months & Acc Change at 3 months (\%) & Mean Acc at 6 months & Acc Change at 6 months (\%) & Mean Acc at 9 months & Acc Change at 9 months (\%) & Mean Acc at 12 months & Acc Change at 12 months (\%) \\
Model_x &  &  &  &  &  &  &  &  &  \\
\midrule
Baichuan2-13B-Base & 0.204 & 0.273 & 33.957 & 0.250 & 22.794 & nan & nan & nan & nan \\
Baichuan2-13B-Chat & 0.258 & 0.381 & 47.810 & 0.300 & 16.400 & nan & nan & nan & nan \\
Baichuan2-7B-Base & 0.240 & 0.182 & -24.091 & 0.500 & 108.750 & nan & nan & nan & nan \\
Baichuan2-7B-Chat & 0.234 & 0.364 & 55.711 & 0.500 & 114.103 & nan & nan & nan & nan \\
Colossal-LLaMA-2-7b-base & 0.309 & 0.375 & 21.467 & nan & nan & nan & nan & nan & nan \\
HF_RWKV_v5-Eagle-7B & 0.217 & 0.333 & 53.571 & nan & nan & nan & nan & nan & nan \\
Llama-2-13b-hf & 0.304 & 0.333 & 9.615 & 0.222 & -26.923 & nan & nan & nan & nan \\
Llama-2-7b-hf & 0.316 & 0.381 & 20.635 & 0.556 & 75.926 & nan & nan & nan & nan \\
Qwen-14B-Chat & 0.282 & 0.625 & 121.726 & nan & nan & nan & nan & nan & nan \\
Qwen-1_8B & 0.273 & 0.000 & -100.000 & nan & nan & nan & nan & nan & nan \\
Qwen-1_8B-Chat & 0.298 & 0.000 & -100.000 & nan & nan & nan & nan & nan & nan \\
Qwen-7B & 0.295 & 0.375 & 26.989 & nan & nan & nan & nan & nan & nan \\
Qwen-7B-Chat & 0.174 & 0.500 & 186.538 & nan & nan & nan & nan & nan & nan \\
Skywork-13B-base & 0.224 & 0.250 & 11.719 & nan & nan & nan & nan & nan & nan \\
TinyLlama-1.1B-Chat-v0.6 & 0.266 & 0.500 & 87.879 & nan & nan & nan & nan & nan & nan \\
Yi-6B & 0.246 & 0.000 & -100.000 & nan & nan & nan & nan & nan & nan \\
Yi-6B-Chat & 0.344 & 0.000 & -100.000 & nan & nan & nan & nan & nan & nan \\
baichuan-13b-chat & 0.294 & 0.381 & 29.657 & 0.500 & 70.175 & nan & nan & nan & nan \\
baichuan-7b-chat & 0.322 & 0.500 & 55.208 & nan & nan & nan & nan & nan & nan \\
chatglm3-6b & 0.288 & 0.000 & -100.000 & nan & nan & nan & nan & nan & nan \\
falcon-rw-1b & 0.296 & 0.179 & -39.665 & 0.273 & -7.851 & 0.273 & -7.851 & nan & nan \\
internlm-chat-7b & 0.370 & 0.409 & 10.455 & 0.444 & 20.000 & nan & nan & nan & nan \\
llama2-7b-chat-hf & 0.316 & 0.333 & 5.556 & 0.222 & -29.630 & nan & nan & nan & nan \\
llama_hf_7b & 0.330 & 0.303 & -8.283 & 0.172 & -47.816 & 0.231 & -30.154 & 0.167 & -49.556 \\
mistral-7b-v0.1 & 0.292 & 0.286 & -2.222 & nan & nan & nan & nan & nan & nan \\
opt-13b & 0.321 & 0.409 & 27.581 & 0.302 & -5.715 & 0.333 & 3.955 & 0.206 & -35.793 \\
opt-2.7b & 0.370 & 0.409 & 10.695 & 0.326 & -11.902 & 0.424 & 14.795 & 0.324 & -12.457 \\
phi-1_5 & 0.266 & 0.000 & -100.000 & nan & nan & nan & nan & nan & nan \\
phi-2 & 0.257 & nan & nan & nan & nan & nan & nan & nan & nan \\
pythia-12b & 0.288 & 0.409 & 42.266 & 0.294 & 2.283 & 0.714 & 148.401 & nan & nan \\
zephyr-7b-beta & 0.317 & 0.125 & -60.556 & nan & nan & nan & nan & nan & nan \\
zhongjing-base & 0.286 & 0.444 & 55.556 & 0.273 & -4.545 & nan & nan & nan & nan \\
\bottomrule
\end{tabular}
'''

sss=r'''\begin{tabular}{llllll}
\toprule
{} & Base ppl & acc Change at 3 months (\%) & acc Change at 6 months (\%) & acc Change at 9 months (\%) & acc Change at 12 months (\%) \\
model                    &          &                            &                            &                            &                             \\
\midrule
Baichuan2-13B-Base       &    0.875 &                      0.463 &                      1.302 &                        nan &                         nan \\
Baichuan2-13B-Chat       &    0.998 &                     -0.392 &                      0.214 &                      0.101 &                         nan \\
Baichuan2-7B-Base        &    0.902 &                      0.097 &                      1.017 &                        nan &                         nan \\
Baichuan2-7B-Chat        &    1.058 &                      0.207 &                      0.162 &                        nan &                         nan \\
Colossal-LLaMA-2-7b-base &    1.073 &                      0.780 &                     -1.428 &                        nan &                         nan \\
HF_RWKV_v5-Eagle-7B      &    0.912 &                      2.179 &                        nan &                        nan &                         nan \\
Llama-2-13b-hf           &    0.784 &                      0.544 &                      1.132 &                        nan &                         nan \\
Llama-2-7b-hf            &    0.821 &                      0.415 &                      0.960 &                        nan &                         nan \\
Qwen-14B-Chat            &    0.933 &                      0.372 &                      4.205 &                        nan &                         nan \\
Qwen-1_8B                &    1.164 &                     -0.742 &                        nan &                        nan &                         nan \\
Qwen-1_8B-Chat           &    1.361 &                     -1.852 &                        nan &                        nan &                         nan \\
Qwen-7B                  &    0.953 &                      0.759 &                      3.508 &                        nan &                         nan \\
Qwen-7B-Chat             &    1.014 &                      0.859 &                      4.069 &                        nan &                         nan \\
Skywork-13B-base         &    0.831 &                      0.390 &                        nan &                        nan &                         nan \\
TinyLlama-1.1B-Chat-v0.6 &    1.008 &                     -1.333 &                        nan &                        nan &                         nan \\
Yi-6B                    &    0.881 &                      0.398 &                        nan &                        nan &                         nan \\
Yi-6B-Chat               &    0.907 &                      1.821 &                        nan &                        nan &                         nan \\
baichuan-13b-chat        &    0.894 &                      0.045 &                     -0.219 &                      0.821 &                         nan \\
baichuan-7b-chat         &    0.975 &                     -0.132 &                      1.033 &                        nan &                         nan \\
chatglm3-6b              &    1.458 &                     -1.149 &                        nan &                        nan &                         nan \\
falcon-rw-1b             &    1.130 &                     -1.857 &                     -2.607 &                     -2.138 &                         nan \\
internlm-chat-7b         &    1.100 &                      0.192 &                      0.310 &                        nan &                         nan \\
llama2-7b-chat-hf        &    1.002 &                      1.118 &                      0.221 &                        nan &                         nan \\
llama_hf_7b              &    0.848 &                     -0.090 &                      0.013 &                     -0.013 &                       0.823 \\
mistral-7b-v0.1          &    0.787 &                      0.331 &                      2.139 &                        nan &                         nan \\
opt-13b                  &    1.133 &                        nan &                     -1.089 &                     -2.021 &                      -5.130 \\
opt-2.7b                 &    1.226 &                        nan &                     -0.961 &                     -2.266 &                      -5.406 \\
phi-1_5                  &    1.282 &                     -1.052 &                     -4.342 &                        nan &                         nan \\
phi-2                    &    1.065 &                     -2.429 &                        nan &                        nan &                         nan \\
pythia-12b               &    0.988 &                     -0.061 &                      0.145 &                      0.207 &                       1.468 \\
vicuna-7b-v1.5           &    0.927 &                      0.189 &                      0.405 &                        nan &                         nan \\
zephyr-7b-beta           &    0.881 &                     -0.009 &                        nan &                        nan &                         nan \\
zhongjing-base           &    0.894 &                      1.229 &                      1.036 &                        nan &                         nan \\
\bottomrule
\end{tabular}'''


# reall acc 
sss=r'''\begin{tabular}{llllll}
\toprule
 & Base ACC & ACC Change at 3 months (%) & ACC Change at 6 months (%) & ACC Change at 9 months (%) & ACC Change at 12 months (%) \\
Model &  &  &  &  &  \\
\midrule
Baichuan2-13B-Base & 0.245 & -9.297 & 19.048 & nan & nan \\
Baichuan2-13B-Chat & 0.284 & 41.053 & -12.930 & -100.000 & nan \\
Baichuan2-7B-Base & 0.270 & -27.984 & 23.457 & nan & nan \\
Baichuan2-7B-Chat & 0.275 & -19.192 & 36.364 & nan & nan \\
Colossal-LLaMA-2-7b-base & 0.321 & 15.226 & nan & nan & nan \\
HF_RWKV_v5-Eagle-7B & 0.263 & -36.594 & nan & nan & nan \\
Llama-2-13b-hf & 0.354 & -21.547 & -0.767 & nan & nan \\
Llama-2-7b-hf & 0.306 & 45.139 & 10.325 & nan & nan \\
Qwen-14B-Chat & 0.352 & 19.234 & nan & nan & nan \\
Qwen-1_8B & 0.236 & -50.205 & nan & nan & nan \\
Qwen-1_8B-Chat & 0.308 & -42.647 & nan & nan & nan \\
Qwen-7B & 0.327 & 2.083 & nan & nan & nan \\
Qwen-7B-Chat & 0.250 & -20.988 & nan & nan & nan \\
Skywork-13B-base & 0.267 & -18.696 & nan & nan & nan \\
TinyLlama-1.1B-Chat-v0.6 & 0.210 & 66.711 & nan & nan & nan \\
Yi-6B & 0.228 & -2.326 & nan & nan & nan \\
Yi-6B-Chat & 0.324 & -15.871 & nan & nan & nan \\
baichuan-13b-chat & 0.328 & 13.117 & 9.035 & -100.000 & nan \\
baichuan-7b-chat & 0.342 & 26.405 & nan & nan & nan \\
chatglm3-6b & 0.332 & -54.758 & nan & nan & nan \\
falcon-rw-1b & 0.326 & 45.306 & -29.210 & -84.662 & nan \\
internlm-chat-7b & 0.408 & -9.692 & -7.719 & nan & nan \\
llama2-7b-chat-hf & 0.282 & 57.439 & 19.675 & nan & nan \\
llama_hf_7b & 0.397 & -59.045 & -30.599 & -13.520 & 5.928 \\
mistral-7b-v0.1 & 0.352 & -11.844 & -48.353 & nan & nan \\
opt-13b & 0.344 & 1.759 & 23.992 & -22.469 & 3.166 \\
opt-2.7b & 0.395 & 13.952 & -10.626 & -49.355 & -34.651 \\
phi-1_5 & 0.296 & 4.875 & -69.279 & nan & nan \\
phi-2 & 0.319 & nan & nan & nan & nan \\
pythia-12b & 0.381 & -16.728 & 0.416 & -16.728 & -67.172 \\
zephyr-7b-beta & 0.353 & 35.507 & nan & nan & nan \\
zhongjing-base & 0.330 & 26.157 & -21.014 & nan & nan \\
\bottomrule
\end{tabular}'''


sss=r'''\begin{table}[htbp]
\centering
\begin{tabular}{lrrrl}
\toprule
\textbf{Model Name} & \textbf{Skewness} & \textbf{Bias Category} & \textbf{1} & \textbf{2} \\
\midrule
phi-1\_5 & 0.002 & Symmetrical & & \\
zhongjing-base & 0.108 & Symmetrical & & \\
TinyLlaMA-1.1B-Chat-v0.6 & 0.109 & Symmetrical & & \\
phi-2 & 0.119 & Symmetrical & & \\
opt-13b & 0.121 & Symmetrical & & \\
Skywork-13B-base & 0.132 & Symmetrical & & \\
baichuan-7b-chat & 0.133 & Symmetrical & & \\
LlaMA-2-7b-hf & 0.151 & Symmetrical & & \\
Yi-6B-Chat & 0.153 & Symmetrical & & \\
mistral-7b-v0.1 & 0.161 & Symmetrical & & \\
Qwen-7B & 0.164 & Symmetrical & & \\
Baichuan2-13B-Base & 0.175 & Symmetrical & & \\
Baichuan2-13B-Chat & 0.192 & Symmetrical & & \\
LlaMA-2-13b-hf & 0.193 & Symmetrical & & \\
falcon-rw-1b & 0.201 & Right-skewed & & \\
Qwen-1\_8B & 0.206 & Right-skewed & & \\
opt-2.7b & 0.210 & Right-skewed & & \\
Baichuan2-7B-Base & 0.227 & Right-skewed & & \\
baichuan-13b-chat & 0.233 & Right-skewed & & \\
Colossal-LlaMA-2-7b-base & 0.234 & Right-skewed & & \\
internlm-chat-7b & 0.239 & Right-skewed & & \\
pythia-12b & 0.239 & Right-skewed & & \\
zephyr-7b-beta & 0.241 & Right-skewed & & \\
Qwen-7B-Chat & 0.251 & Right-skewed & & \\
Qwen-14B-Chat & 0.252 & Right-skewed & & \\
Baichuan2-7B-Chat & 0.253 & Right-skewed & & \\
LlaMA\_hf\_7b & 0.289 & Right-skewed & & \\
LlaMA2-7b-chat-hf & 0.296 & Right-skewed & & \\
Qwen-1\_8B-Chat & 0.296 & Right-skewed & & \\
Yi-6B & 0.333 & Right-skewed & & \\
chatglm3-6b & 0.352 & Right-skewed & & \\
\bottomrule
\end{tabular}
}
\label{tab:model_bias}
\end{table}
'''

sss=r'''
this is bbc\begin{tabular}{lllllll}
\toprule
Model & Base Accuracy & Acc Change at 3 months (\%) & Acc Change at 6 months (\%) & Acc Change at 9 months (\%) & Acc Change at 12 months (\%) & mean \\
\midrule
Baichuan2-7B-Chat & 0.517 & -3.571 & -0.038 & -5.315 & nan & -2.975 \\
zhongjing-base & 0.465 & -8.488 & 2.662 & -1.290 & nan & -2.372 \\
Baichuan2-7B-Base & 0.451 & -3.059 & 0.595 & -4.649 & nan & -2.371 \\
Baichuan2-13B-Base & 0.439 & -2.943 & 0.882 & -4.390 & nan & -2.150 \\
pythia-12b & 0.480 & -0.233 & -3.888 & -2.612 & -1.012 & -1.936 \\
falcon-rw-1b & 0.510 & 0.459 & -7.814 & 1.201 & -1.474 & -1.907 \\
llama2-7b-chat-hf & 0.505 & -8.308 & 2.695 & 0.664 & nan & -1.650 \\
baichuan-13b-chat & 0.467 & -3.645 & -1.078 & 0.413 & nan & -1.436 \\
Baichuan2-13B-Chat & 0.495 & -3.541 & -0.995 & 0.232 & nan & -1.435 \\
internlm-chat-7b & 0.515 & -2.476 & -1.344 & 0.236 & nan & -1.195 \\
Llama-2-7b-hf & 0.434 & -7.314 & 3.092 & 1.279 & nan & -0.981 \\
phi-1_5 & 0.602 & -1.772 & 1.131 & -1.837 & nan & -0.826 \\
llama_hf_7b & 0.450 & 1.270 & 0.177 & -7.776 & 3.266 & -0.766 \\
Llama-2-13b-hf & 0.416 & -6.928 & 3.502 & 1.683 & nan & -0.581 \\
TinyLlama-1.1B-Chat-v0.6 & 0.513 & 2.539 & -3.678 & nan & nan & -0.569 \\
Qwen-1_8B-Chat & 0.599 & 1.635 & -2.033 & nan & nan & -0.199 \\
Qwen-1_8B & 0.520 & 1.899 & -2.082 & nan & nan & -0.091 \\
Yi-6B-Chat & 0.446 & 3.030 & -2.798 & nan & nan & 0.116 \\
opt-2.7b & 0.475 & 1.970 & -2.228 & 1.192 & 1.143 & 0.519 \\
opt-13b & 0.450 & 2.273 & -2.087 & 1.265 & 0.839 & 0.572 \\
phi-2 & 0.487 & 1.882 & nan & nan & nan & 1.882 \\
mistral-7b-v0.1 & 0.398 & 1.110 & 5.347 & -0.661 & nan & 1.932 \\
Qwen-7B-Chat & 0.466 & 1.809 & 3.606 & nan & nan & 2.708 \\
Qwen-7B & 0.441 & 1.892 & 3.689 & nan & nan & 2.791 \\
Colossal-LLaMA-2-7b-base & 0.618 & 2.825 & 3.715 & nan & nan & 3.270 \\
HF_RWKV_v5-Eagle-7B & 0.440 & 4.956 & 2.278 & nan & nan & 3.617 \\
chatglm3-6b & 0.832 & 5.567 & 1.684 & nan & nan & 3.626 \\
Qwen-14B-Chat & 0.445 & 2.682 & 4.847 & nan & nan & 3.764 \\
baichuan-7b-chat & 0.492 & 3.055 & 4.806 & nan & nan & 3.931 \\
Yi-6B & 0.427 & 6.478 & 3.144 & nan & nan & 4.811 \\
Skywork-13B-base & 0.429 & 7.163 & 3.261 & nan & nan & 5.212 \\
zephyr-7b-beta & 0.435 & 7.340 & 3.928 & nan & nan & 5.634 \\
\bottomrule
\end{tabular}'''


sss=r'''\begin{tabular}{llll}
\toprule
model_name & skewness & slope & bias_category \\
\midrule
phi-1_5 & 0.002 & -0.002 & Symmetrical \\
zhongjing-base & 0.108 & -0.004 & Symmetrical \\
TinyLlama-1.1B-Chat-v0.6 & 0.109 & -0.004 & Symmetrical \\
phi-2 & 0.119 & -0.007 & Symmetrical \\
opt-13b & 0.121 & -0.006 & Symmetrical \\
Skywork-13B-base & 0.132 & -0.005 & Symmetrical \\
baichuan-7b-chat & 0.133 & -0.007 & Symmetrical \\
Llama-2-7b-hf & 0.151 & -0.007 & Symmetrical \\
Yi-6B-Chat & 0.153 & -0.008 & Symmetrical \\
mistral-7b-v0.1 & 0.161 & -0.007 & Symmetrical \\
Qwen-7B & 0.164 & -0.006 & Symmetrical \\
Baichuan2-13B-Base & 0.175 & -0.007 & Symmetrical \\
Baichuan2-13B-Chat & 0.192 & -0.006 & Symmetrical \\
Llama-2-13b-hf & 0.193 & -0.007 & Symmetrical \\
falcon-rw-1b & 0.201 & -0.010 & Right-skewed \\
Qwen-1_8B & 0.206 & -0.009 & Right-skewed \\
opt-2.7b & 0.210 & -0.012 & Right-skewed \\
Baichuan2-7B-Base & 0.227 & -0.008 & Right-skewed \\
baichuan-13b-chat & 0.233 & -0.012 & Right-skewed \\
Colossal-LLaMA-2-7b-base & 0.234 & -0.010 & Right-skewed \\
internlm-chat-7b & 0.239 & -0.011 & Right-skewed \\
pythia-12b & 0.239 & -0.010 & Right-skewed \\
zephyr-7b-beta & 0.241 & -0.011 & Right-skewed \\
Qwen-7B-Chat & 0.251 & -0.007 & Right-skewed \\
Qwen-14B-Chat & 0.252 & -0.011 & Right-skewed \\
Baichuan2-7B-Chat & 0.253 & -0.011 & Right-skewed \\
llama_hf_7b & 0.289 & -0.012 & Right-skewed \\
llama2-7b-chat-hf & 0.296 & -0.011 & Right-skewed \\
Qwen-1_8B-Chat & 0.296 & -0.012 & Right-skewed \\
Yi-6B & 0.333 & -0.013 & Right-skewed \\
chatglm3-6b & 0.352 & -0.012 & Right-skewed \\
\bottomrule
\end{tabular}'''


sss=r'''\begin{tabular}{llllll}
\toprule
 & Base ACC & ACC Change at 3 months (%) & ACC Change at 6 months (%) & ACC Change at 9 months (%) & ACC Change at 12 months (%) \\
Model &  &  &  &  &  \\
\midrule
TinyLlama-1.1B-Chat-v0.6 & 0.210 & 4.557 & 66.711 & nan & nan \\
baichuan-7b-chat & 0.342 & 10.514 & 21.129 & nan & nan \\
Baichuan2-7B-Chat & 0.275 & 6.952 & 4.213 & 36.364 & nan \\
Qwen-14B-Chat & 0.352 & -2.158 & 15.399 & nan & nan \\
llama2-7b-chat-hf & 0.282 & 20.514 & 7.999 & 22.621 & nan \\
Colossal-LLaMA-2-7b-base & 0.321 & 3.704 & 14.236 & nan & nan \\
Llama-2-7b-hf & 0.306 & 27.932 & -4.421 & 25.601 & nan \\
Baichuan2-13B-Base & 0.245 & -10.821 & -0.448 & 19.048 & nan \\
Baichuan2-7B-Base & 0.270 & -3.517 & -5.149 & 23.457 & nan \\
HF_RWKV_v5-Eagle-7B & 0.263 & -21.129 & 1.449 & nan & nan \\
Qwen-7B & 0.327 & 0.382 & 0.488 & nan & nan \\
zephyr-7b-beta & 0.353 & 6.667 & -1.163 & nan & nan \\
zhongjing-base & 0.330 & 9.577 & -5.722 & 3.073 & nan \\
Skywork-13B-base & 0.267 & -19.857 & -4.511 & nan & nan \\
opt-13b & 0.344 & 3.166 & 3.521 & -8.353 & -14.624 \\
internlm-chat-7b & 0.408 & -8.346 & -8.881 & -7.307 & nan \\
Llama-2-13b-hf & 0.354 & -15.561 & -12.170 & -4.951 & nan \\
Yi-6B & 0.228 & 2.815 & -12.093 & nan & nan \\
opt-2.7b & 0.395 & -10.146 & -13.673 & -10.545 & -17.601 \\
falcon-rw-1b & 0.326 & -6.142 & -0.669 & -26.083 & -15.152 \\
pythia-12b & 0.381 & -28.526 & -10.269 & -24.130 & -8.386 \\
Qwen-7B-Chat & 0.250 & -17.778 & -18.750 & nan & nan \\
Yi-6B-Chat & 0.324 & 17.781 & -22.881 & nan & nan \\
mistral-7b-v0.1 & 0.352 & -7.568 & -1.672 & -48.353 & nan \\
llama_hf_7b & 0.397 & -21.275 & -30.534 & -22.077 & -24.833 \\
baichuan-13b-chat & 0.328 & -14.425 & 3.207 & 4.687 & -100.000 \\
Baichuan2-13B-Chat & 0.284 & 10.744 & -2.047 & -11.842 & -100.000 \\
phi-1_5 & 0.296 & -6.130 & -11.618 & -69.279 & nan \\
Qwen-1_8B-Chat & 0.308 & 4.905 & -42.647 & nan & nan \\
Qwen-1_8B & 0.236 & 7.153 & -50.205 & nan & nan \\
chatglm3-6b & 0.332 & -18.727 & -52.016 & nan & nan \\
phi-2 & 0.319 & 10.285 & nan & nan & nan \\
\bottomrule
\end{tabular}'''


wiki_ppl_0416=r'''\begin{tabular}{lllllll}
\toprule
Model & Base Accuracy & Acc Change at 3 months (%) & Acc Change at 6 months (%) & Acc Change at 9 months (%) & Acc Change at 12 months (%) & mean \\
\midrule
falcon-rw-1b & 0.083 & -1.272 & -1.113 & -1.131 & -1.207 & -1.181 \\
pythia-12b & 0.071 & -0.578 & -0.933 & -0.859 & -0.903 & -0.818 \\
opt-2.7b & 0.082 & -0.658 & 0.024 & -0.528 & -0.915 & -0.519 \\
opt-13b & 0.075 & -0.623 & 0.105 & -0.413 & -0.818 & -0.437 \\
Qwen-1_8B-Chat & 0.091 & -0.331 & -0.496 & nan & nan & -0.414 \\
TinyLlama-1.1B-Chat-v0.6 & 0.070 & -0.332 & -0.473 & nan & nan & -0.403 \\
internlm-chat-7b & 0.080 & -0.482 & -0.301 & -0.250 & nan & -0.344 \\
baichuan-7b-chat & 0.064 & -0.032 & -0.424 & nan & nan & -0.228 \\
chatglm3-6b & 0.105 & -0.187 & -0.245 & nan & nan & -0.216 \\
Qwen-1_8B & 0.080 & -0.131 & -0.251 & nan & nan & -0.191 \\
Colossal-LLaMA-2-7b-base & 0.065 & -0.042 & -0.199 & nan & nan & -0.121 \\
phi-1_5 & 0.098 & 0.066 & -0.125 & -0.248 & nan & -0.102 \\
llama2-7b-chat-hf & 0.060 & 0.132 & -0.186 & -0.093 & nan & -0.049 \\
zephyr-7b-beta & 0.059 & -0.049 & -0.033 & nan & nan & -0.041 \\
phi-2 & 0.072 & -0.037 & nan & nan & nan & -0.037 \\
Yi-6B & 0.058 & -0.071 & 0.022 & nan & nan & -0.024 \\
Yi-6B-Chat & 0.060 & -0.028 & 0.023 & nan & nan & -0.003 \\
baichuan-13b-chat & 0.058 & 0.019 & 0.124 & -0.125 & nan & 0.006 \\
llama_hf_7b & 0.052 & 0.214 & -0.425 & 0.379 & -0.067 & 0.025 \\
Baichuan2-7B-Chat & 0.068 & 0.343 & -0.035 & -0.073 & nan & 0.078 \\
mistral-7b-v0.1 & 0.053 & 0.381 & -0.028 & 0.018 & nan & 0.124 \\
Skywork-13B-base & 0.050 & 0.075 & 0.276 & nan & nan & 0.175 \\
HF_RWKV_v5-Eagle-7B & 0.065 & 0.149 & 0.220 & nan & nan & 0.184 \\
Qwen-7B-Chat & 0.065 & 0.302 & 0.226 & nan & nan & 0.264 \\
Baichuan2-7B-Base & 0.059 & 0.523 & 0.157 & 0.185 & nan & 0.289 \\
Qwen-7B & 0.061 & 0.428 & 0.430 & nan & nan & 0.429 \\
Baichuan2-13B-Chat & 0.062 & 0.299 & 0.628 & 0.512 & nan & 0.480 \\
zhongjing-base & 0.050 & 0.756 & 0.269 & 0.569 & nan & 0.531 \\
Llama-2-7b-hf & 0.050 & 0.774 & 0.349 & 0.517 & nan & 0.547 \\
Baichuan2-13B-Base & 0.053 & 1.019 & 0.797 & 0.900 & nan & 0.905 \\
Qwen-14B-Chat & 0.049 & 1.301 & 1.939 & nan & nan & 1.620 \\
Llama-2-13b-hf & 0.041 & 1.700 & 1.446 & 1.796 & nan & 1.647 \\
\bottomrule
\end{tabular}'''


time_diff_acc_skew_part=r'''gpt4_1106 & 0.057 & -0.001 & Symmetrical \\
phi-1_5 & 0.064 & -0.001 & Symmetrical \\
Yi-6B-Chat & 0.129 & -0.002 & Symmetrical \\
zhongjing-base & 0.141 & -0.002 & Symmetrical \\
Gemini & 0.146 & -0.002 & Symmetrical \\
phi-2 & 0.153 & -0.002 & Symmetrical \\
Baichuan2-13B-Chat & 0.164 & -0.003 & Symmetrical \\
Llama-2-7b-hf & 0.165 & -0.002 & Symmetrical \\
Baichuan2-7B-Chat & 0.167 & -0.003 & Symmetrical \\
mistral-7b-v0.1 & 0.169 & -0.002 & Symmetrical \\
baichuan-7b-chat & 0.173 & -0.002 & Symmetrical \\
gpt_3.5_turbo_0613 & 0.173 & -0.002 & Symmetrical \\
Qwen-7B & 0.179 & -0.002 & Symmetrical \\
falcon-rw-1b & 0.179 & -0.002 & Symmetrical \\
Llama-2-13b-hf & 0.181 & -0.002 & Symmetrical \\
opt-13b & 0.183 & -0.003 & Symmetrical \\
internlm-chat-7b & 0.184 & -0.002 & Symmetrical \\
opt-2.7b & 0.190 & -0.003 & Symmetrical \\
Skywork-13B-base & 0.190 & -0.003 & Symmetrical \\
baichuan-13b-chat & 0.192 & -0.003 & Symmetrical \\
Qwen-1_8B & 0.200 & -0.002 & Symmetrical \\
Baichuan2-13B-Base & 0.202 & -0.003 & Right-skewed \\
Baichuan2-7B-Base & 0.211 & -0.003 & Right-skewed \\
Qwen-14B-Chat & 0.213 & -0.002 & Right-skewed \\
zephyr-7b-beta & 0.220 & -0.003 & Right-skewed \\
pythia-12b & 0.223 & -0.004 & Right-skewed \\
Yi-6B & 0.226 & -0.004 & Right-skewed \\
llama2-7b-chat-hf & 0.231 & -0.003 & Right-skewed \\
Qwen-1_8B-Chat & 0.235 & -0.002 & Right-skewed \\
Colossal-LLaMA-2-7b-base & 0.236 & -0.003 & Right-skewed \\
Qwen-7B-Chat & 0.244 & -0.004 & Right-skewed \\
TinyLlama-1.1B-Chat-v0.6 & 0.244 & -0.003 & Right-skewed \\
llama_hf_7b & 0.281 & -0.003 & Right-skewed \\
chatglm3-6b & 0.313 & -0.003 & Right-skewed \\
'''



time_diff_acc_gen_part=r'''\midrule
TinyLlama-1.1B-Chat-v0.6 & 0.210 & 4.557 & 66.711 & nan & nan & 35.634 \\
llama2-7b-chat-hf & 0.282 & 20.514 & 7.999 & 22.621 & nan & 17.044 \\
Llama-2-7b-hf & 0.306 & 27.932 & -4.421 & 25.601 & nan & 16.371 \\
Baichuan2-7B-Chat & 0.275 & 6.952 & 4.213 & 36.364 & nan & 15.843 \\
baichuan-7b-chat & 0.342 & 10.514 & 21.129 & nan & nan & 15.821 \\
phi-2 & 0.319 & 10.285 & nan & nan & nan & 10.285 \\
Colossal-LLaMA-2-7b-base & 0.321 & 3.704 & 14.236 & nan & nan & 8.970 \\
Qwen-14B-Chat & 0.352 & -2.158 & 15.399 & nan & nan & 6.620 \\
Gemini & 0.397 & 5.326 & 7.834 & nan & nan & 6.580 \\
Baichuan2-7B-Base & 0.270 & -3.517 & -5.149 & 23.457 & nan & 4.930 \\
zephyr-7b-beta & 0.353 & 6.667 & -1.163 & nan & nan & 2.752 \\
Baichuan2-13B-Base & 0.245 & -10.821 & -0.448 & 19.048 & nan & 2.593 \\
zhongjing-base & 0.330 & 9.577 & -5.722 & 3.073 & nan & 2.309 \\
gpt_3.5_turbo_0613 & 0.385 & -20.175 & 15.556 & 10.909 & -2.500 & 0.947 \\
Qwen-7B & 0.327 & 0.382 & 0.488 & nan & nan & 0.435 \\
Yi-6B-Chat & 0.324 & 17.781 & -22.881 & nan & nan & -2.550 \\
opt-13b & 0.344 & 3.166 & 3.521 & -8.353 & -14.624 & -4.072 \\
Yi-6B & 0.228 & 2.815 & -12.093 & nan & nan & -4.639 \\
gpt4_1106 & 0.675 & -6.392 & 0.505 & -18.928 & -6.999 & -7.953 \\
internlm-chat-7b & 0.408 & -8.346 & -8.881 & -7.307 & nan & -8.178 \\
HF_RWKV_v5-Eagle-7B & 0.263 & -21.129 & 1.449 & nan & nan & -9.840 \\
Llama-2-13b-hf & 0.354 & -15.561 & -12.170 & -4.951 & nan & -10.894 \\
falcon-rw-1b & 0.326 & -6.142 & -0.669 & -26.083 & -15.152 & -12.011 \\
Skywork-13B-base & 0.267 & -19.857 & -4.511 & nan & nan & -12.184 \\
opt-2.7b & 0.395 & -10.146 & -13.673 & -10.545 & -17.601 & -12.991 \\
pythia-12b & 0.381 & -28.526 & -10.269 & -24.130 & -8.386 & -17.828 \\
Qwen-7B-Chat & 0.250 & -17.778 & -18.750 & nan & nan & -18.264 \\
Qwen-1_8B-Chat & 0.308 & 4.905 & -42.647 & nan & nan & -18.871 \\
mistral-7b-v0.1 & 0.352 & -7.568 & -1.672 & -48.353 & nan & -19.198 \\
Qwen-1_8B & 0.236 & 7.153 & -50.205 & nan & nan & -21.526 \\
llama_hf_7b & 0.397 & -21.275 & -30.534 & -22.077 & -24.833 & -24.680 \\
Baichuan2-13B-Chat & 0.284 & 10.744 & -2.047 & -11.842 & -100.000 & -25.786 \\
baichuan-13b-chat & 0.328 & -14.425 & 3.207 & 4.687 & -100.000 & -26.633 \\
phi-1_5 & 0.296 & -6.130 & -11.618 & -69.279 & nan & -29.009 \\
chatglm3-6b & 0.332 & -18.727 & -52.016 & nan & nan & -35.372 \\'''



sss=time_diff_acc_gen_part#time_diff_acc_skew_part#wiki_ppl_0416





three_type_ppl_slope_delete_skewness=r'''OPT-13b  & May 2022 & -19.4 & 1689.0 & -30.2 \\
OPT-2.7b  & May 2022 & -18.8 & 1080.7 & -46.9 \\
LLaMA\_hf\_7b  & Feb 2023 & -15.3 & 713.0 & 52.0 \\
pythia-12b  & Mar 2023 & -8.1 & 802.7 & -11.1 \\
falcon-rw-1b  & Apr 2023 & -26.8 & 607.4 & -47.7 \\
baichuan-13b-chat  & Jun 2023 & -11.7 & 685.7 & 4.8 \\
baichuan-7b-chat  & Jun 2023 & -14.6 & 726.6 & -16.5 \\
LLaMA-2-13b-hf  & Jul 2023 & -11.1 & 769.6 & 65.9 \\
LLaMA-2-7b-hf  & Jul 2023 & -12.6 & 684.6 & 23.2 \\
Baichuan-13B-Chat  & Jul 2023 & -7.0 & 717.2 & 12.1 \\
Baichuan-13B-Chat  & Jul 2023 & -7.0 & 717.2 & 12.1 \\
zhongjing-base  & Jul 2023 & -15.0 & 759.7 & 56.9 \\
internlm-chat-7b  & Jul 2023 & -19.3 & 574.0 & -22.0 \\
Baichuan2-7B-Base  & Aug 2023 & -9.5 & 687.5 & 3.7 \\
Baichuan2-7B-Chat  & Aug 2023 & -8.4 & 781.8 & -11.6 \\
Colossal-LLaMA-2-7b-base  & Sep 2023 & -21.2 & 696.3 & -36.2 \\
Qwen-14B-Chat  & Sep 2023 & -7.9 & 762.2 & 51.5 \\
Qwen-7B  & Sep 2023 & -11.7 & 662.4 & 7.4 \\
Qwen-7B-Chat  & Sep 2023 & -13.2 & 705.7 & -3.6 \\
Mistral-7B-v0.1  & Sep 2023 & -15.1 & 756.8 & 10.4 \\
phi-1\_5  & Sep 2023 & -26.0 & 1212.9 & -60.7 \\
Baichuan2-13B-Base  & Sep 2023 & -9.1 & 747.9 & 15.8 \\
Skywork-13B-base  & Oct 2023 & -16.3 & 549.1 & 30.8 \\
chatglm3-6b  & Oct 2023 & -25.5 & 412.6 & -70.4 \\
zephyr-7b-beta  & Oct 2023 & -21.1 & 506.9 & 3.7 \\
Yi-6B  & Nov 2023 & -9.4 & 451.7 & 24.6 \\
Yi-6B-Chat  & Nov 2023 & -9.4 & 506.5 & 20.2 \\
Qwen-1\_8B  & Nov 2023 & -22.7 & 374.0 & -46.2 \\
Qwen-1\_8B-Chat  & Nov 2023 & -25.3 & 426.8 & -50.3 \\
HF\_RWKV\_v5-Eagle-7B  & Nov 2023 & -12.8 & 511.3 & 4.2 \\
TinyLLaMA-1.1B-Chat-v0.6  & Dec 2023 & -25.0 & 300.1 & -45.3 \\
phi-2  & Dec 2023 & -21.2 & 669.3 & -44.7 \\'''


sss=three_type_ppl_slope_delete_skewness

gen_adjuested=r'''
Llama-2-7b-hf & 0.15 & 656.31 & 875.36 & 368.55 & nan & 633.41 \\
baichuan-7b-chat & 0.56 & 170.48 & 244.59 & nan & nan & 207.54 \\
Qwen-14B-Chat & 0.36 & 204.65 & 200.77 & nan & nan & 202.71 \\
Llama-2-13b-hf & 0.52 & 137.93 & 179.69 & 110.80 & nan & 142.81 \\
mistral-7b-v0.1 & 0.48 & 284.22 & 248.79 & -109.47 & nan & 141.18 \\
zephyr-7b-beta & 0.41 & 169.05 & 103.56 & nan & nan & 136.31 \\
Baichuan2-7B-Base & 0.45 & 102.81 & 257.95 & 23.19 & nan & 127.98 \\
gpt4_1106 & 0.79 & 235.82 & 35.01 & 105.40 & 102.89 & 119.78 \\
Colossal-LLaMA-2-7b-base & 0.45 & 159.16 & 74.07 & nan & nan & 116.61 \\
llama2-7b-chat-hf & 0.67 & 96.94 & 119.97 & 0.57 & nan & 72.49 \\
zhongjing-base & 0.70 & 84.39 & 112.54 & 2.96 & nan & 66.63 \\
Qwen-7B & 0.49 & 88.73 & 16.98 & nan & nan & 52.86 \\
Skywork-13B-base & 0.62 & 103.96 & 0.63 & nan & nan & 52.30 \\
Baichuan2-7B-Chat & 0.51 & 84.65 & 127.02 & -84.19 & nan & 42.49 \\
Baichuan2-13B-Chat & 0.54 & -0.79 & 69.44 & 68.82 & 24.11 & 40.39 \\
Baichuan2-13B-Base & 0.67 & 30.64 & 81.19 & 5.33 & nan & 39.05 \\
chatglm3-6b & 0.50 & 54.78 & 8.07 & nan & nan & 31.42 \\
phi-1_5 & 0.66 & 119.33 & 54.30 & -85.70 & nan & 29.31 \\
Yi-6B & 0.56 & 79.58 & -28.44 & nan & nan & 25.57 \\
internlm-chat-7b & 0.31 & -86.66 & 82.28 & 52.65 & nan & 16.09 \\
baichuan-13b-chat & 0.76 & -7.07 & 67.22 & 56.02 & -53.85 & 15.58 \\
phi-2 & 1.59 & 14.53 & nan & nan & nan & 14.53 \\
llama_hf_7b & 0.69 & 34.96 & -99.43 & 33.17 & 55.76 & 6.12 \\
gpt_3.5_turbo_0613 & 0.59 & -124.14 & 111.39 & 162.68 & -157.88 & -1.99 \\
TinyLlama-1.1B-Chat-v0.6 & 1.07 & 48.29 & -52.55 & nan & nan & -2.13 \\
Yi-6B-Chat & 0.87 & 26.12 & -33.72 & nan & nan & -3.80 \\
Qwen-1_8B-Chat & 1.16 & 27.52 & -52.97 & nan & nan & -12.73 \\
opt-13b & 1.82 & 8.22 & -53.69 & -54.69 & -36.17 & -34.08 \\
HF_RWKV_v5-Eagle-7B & 0.88 & -5.97 & -63.57 & nan & nan & -34.77 \\
falcon-rw-1b & 0.87 & -137.70 & -17.39 & 39.52 & -25.62 & -35.30 \\
opt-2.7b & 1.84 & 2.80 & -39.31 & -58.58 & -53.55 & -37.16 \\
pythia-12b & 1.52 & -68.78 & -73.54 & -23.19 & -19.41 & -46.23 \\
Qwen-1_8B & 1.08 & -18.40 & -117.46 & nan & nan & -67.93 \\
Gemini & 1.03 & -51.54 & -124.29 & nan & nan & -87.91 \\
Qwen-7B-Chat & -0.10 & -1363.23 & -1641.88 & nan & nan & -1502.56 \\
'''

sss=gen_adjuested



cdf_gen_acc=r'''Qwen-7B-Chat & 0.48 & 60.26 & 74.85 & nan & nan & 67.55 \\
Llama-2-13b-hf & 0.57 & 29.19 & 38.00 & 34.54 & nan & 33.91 \\
baichuan-7b-chat & 0.62 & 25.01 & 38.76 & nan & nan & 31.88 \\
Llama-2-7b-hf & 0.54 & 25.57 & 41.09 & 27.09 & nan & 31.25 \\
zhongjing-base & 0.59 & 25.16 & 37.70 & 14.65 & nan & 25.83 \\
gpt4_1106 & 0.63 & 27.73 & 15.71 & 28.47 & 23.22 & 23.78 \\
llama2-7b-chat-hf & 0.61 & 25.39 & 23.81 & 12.52 & nan & 20.58 \\
Baichuan2-7B-Base & 0.60 & 14.99 & 32.31 & 4.81 & nan & 17.37 \\
internlm-chat-7b & 0.48 & 3.43 & 25.13 & 21.65 & nan & 16.74 \\
zephyr-7b-beta & 0.61 & 14.33 & 18.22 & nan & nan & 16.28 \\
Qwen-14B-Chat & 0.59 & 14.68 & 14.30 & nan & nan & 14.49 \\
mistral-7b-v0.1 & 0.61 & 30.25 & 34.87 & -22.79 & nan & 14.11 \\
Skywork-13B-base & 0.61 & 20.20 & 5.04 & nan & nan & 12.62 \\
Baichuan2-13B-Base & 0.61 & 10.81 & 17.67 & 6.75 & nan & 11.75 \\
Baichuan2-13B-Chat & 0.61 & 0.45 & 9.02 & 10.67 & 21.68 & 10.46 \\
Colossal-LLaMA-2-7b-base & 0.58 & 15.99 & 3.33 & nan & nan & 9.66 \\
phi-2 & 0.81 & 7.11 & nan & nan & nan & 7.11 \\
Baichuan2-7B-Chat & 0.60 & 16.12 & 22.67 & -18.59 & nan & 6.73 \\
baichuan-13b-chat & 0.64 & 0.69 & 12.79 & 8.00 & 0.13 & 5.40 \\
chatglm3-6b & 0.60 & 3.24 & 6.29 & nan & nan & 4.76 \\
phi-1_5 & 0.65 & 19.30 & 10.78 & -17.57 & nan & 4.17 \\
Yi-6B-Chat & 0.67 & 13.11 & -6.19 & nan & nan & 3.46 \\
Qwen-7B & 0.62 & 7.45 & -7.31 & nan & nan & 0.07 \\
Yi-6B & 0.63 & 8.42 & -9.47 & nan & nan & -0.53 \\
llama_hf_7b & 0.66 & -0.31 & -20.59 & 5.09 & 9.89 & -1.48 \\
TinyLlama-1.1B-Chat-v0.6 & 0.71 & 13.27 & -16.30 & nan & nan & -1.51 \\
Qwen-1_8B-Chat & 0.73 & 4.74 & -8.91 & nan & nan & -2.08 \\
gpt_3.5_turbo_0613 & 0.65 & -29.81 & 16.71 & 26.91 & -39.69 & -6.47 \\
falcon-rw-1b & 0.69 & -34.51 & -8.30 & 7.15 & -4.52 & -10.04 \\
HF_RWKV_v5-Eagle-7B & 0.70 & -0.09 & -20.38 & nan & nan & -10.23 \\
opt-13b & 0.82 & 1.38 & -17.76 & -18.79 & -11.87 & -11.76 \\
opt-2.7b & 0.86 & 0.11 & -13.63 & -23.41 & -18.98 & -13.98 \\
pythia-12b & 0.77 & -27.68 & -24.85 & -6.22 & -3.68 & -15.61 \\
Qwen-1_8B & 0.68 & -6.93 & -33.98 & nan & nan & -20.46 \\
Gemini & 0.71 & -15.15 & -41.28 & nan & nan & -28.21 \\
'''



# sss=cdf_gen_acc
# # data=pd.read_csv('path_to/fresh_eval/vis/Z_score/Z_score_use_start_b4cutoff.csv',index_col=None)
# data=pd.read_csv('path_to/fresh_eval/vis/Z_score/Z_score_use_start_b4cutoff_cdf.csv',index_col=None)
# # breakpoint()
# data=data.iloc[:,1:]
# data['slope']=data['slope']*1000

def get_bias(data,pos_thres=1,neg_thres=-1):
    if data>pos_thres:
        return 'Neophilia'#new 
    elif data<neg_thres:
        return 'Nostalgia'
    else:
        return 'Symmetrical'
    
# data['bias category']=data['slope'].apply(lambda x: get_bias(x))
# data=data.apply(lambda x: x.apply(lambda y: f'{y:.2f}' if isinstance(y, float) else y))
# sss=data.to_latex(index=False)


# ----------------------

sss=r'''Qwen-7B-Chat & 0.48 & 60.26 & 74.85 & - & - & 67.55 \\
Llama-2-13B & 0.57 & 29.19 & 38.00 & 34.54 & - & 33.91 \\
Baichuan-7B-chat & 0.62 & 25.01 & 38.76 & - & - & 31.88 \\
Llama-2-7B & 0.54 & 25.57 & 41.09 & 27.09 & - & 31.25 \\
Zhongjing-Base & 0.59 & 25.16 & 37.70 & 14.65 & - & 25.83 \\
GPT-4-1106 & 0.63 & 27.73 & 15.71 & 28.47 & 23.22 & 23.78 \\
LLaMA2-7B-chat & 0.61 & 25.39 & 23.81 & 12.52 & - & 20.58 \\
Baichuan2-7B-Base & 0.60 & 14.99 & 32.31 & 4.81 & - & 17.37 \\
InternLM-chat-7B & 0.48 & 3.43 & 25.13 & 21.65 & - & 16.74 \\
Zephyr-7B-beta & 0.61 & 14.33 & 18.22 & - & - & 16.28 \\
Qwen-14B-Chat & 0.59 & 14.68 & 14.30 & - & - & 14.49 \\
Mistral-7B-v0.1 & 0.61 & 30.25 & 34.87 & -22.79 & - & 14.11 \\
Skywork-13B-Base & 0.61 & 20.20 & 5.04 & - & - & 12.62 \\
Baichuan2-13B-Base & 0.61 & 10.81 & 17.67 & 6.75 & - & 11.75 \\
Baichuan2-13B-Chat & 0.61 & 0.45 & 9.02 & 10.67 & 21.68 & 10.46 \\
Colossal-LLaMA-2-7B-Base & 0.58 & 15.99 & 3.33 & - & - & 9.66 \\
Phi-2 & 0.81 & 7.11 & - & - & - & 7.11 \\
Baichuan2-7B-Chat & 0.60 & 16.12 & 22.67 & -18.59 & - & 6.73 \\
Baichuan-13B-chat & 0.64 & 0.69 & 12.79 & 8.00 & 0.13 & 5.40 \\
ChatGLM3-6B & 0.60 & 3.24 & 6.29 & - & - & 4.76 \\
Phi-1.5 & 0.65 & 19.30 & 10.78 & -17.57 & - & 4.17 \\
Yi-6B-Chat & 0.67 & 13.11 & -6.19 & - & - & 3.46 \\
Qwen-7B & 0.62 & 7.45 & -7.31 & - & - & 0.07 \\
Yi-6B & 0.63 & 8.42 & -9.47 & - & - & -0.53 \\
LLaMA-7B & 0.66 & -0.31 & -20.59 & 5.09 & 9.89 & -1.48 \\
TinyLlama-1.1B-Chat-v0.6 & 0.71 & 13.27 & -16.30 & - & - & -1.51 \\
Qwen-1.8B-Chat & 0.73 & 4.74 & -8.91 & - & - & -2.08 \\
GPT-3.5-turbo-0613 & 0.65 & -29.81 & 16.71 & 26.91 & -39.69 & -6.47 \\
Falcon-rw-1B & 0.69 & -34.51 & -8.30 & 7.15 & -4.52 & -10.04 \\
RWKV-v5-Eagle-7B & 0.70 & -0.09 & -20.38 & - & - & -10.23 \\
OPT-13B & 0.82 & 1.38 & -17.76 & -18.79 & -11.87 & -11.76 \\
OPT-2.7B & 0.86 & 0.11 & -13.63 & -23.41 & -18.98 & -13.98 \\
Pythia-12B & 0.77 & -27.68 & -24.85 & -6.22 & -3.68 & -15.61 \\
Qwen-1.8B & 0.68 & -6.93 & -33.98 & - & - & -20.46 \\
Gemini & 0.71 & -15.15 & -41.28 & - & - & -28.21 \\'''

sss=r'''\midrule
GPT4-231106 & 794.275 \\
GPT4-230613 & 699.8 \\
Zephyr-7b-beta & 601.35 \\
InternLM-chat-7b & 592.15 \\
GPT3.5-turbo-230613 & 578.025 \\
Baichuan-13b-chat & 571.8 \\
Qwen-14B-Chat & 565.45 \\
OPT-2.7b & 547.375 \\
Yi-6B-Chat & 541.05 \\
Mistral-7b-v0.1 & 528.725 \\
Baichuan-7b-chat & 527.825 \\
LLaMA-7b & 524.075 \\
Baichuan2-7B-Chat & 517.725 \\
Pythia-12b & 513.375 \\
Colossal-LLaMA2-7b-base & 513.35 \\
LLaMA2-7b-chat & 508.4 \\
LLaMA2-13b & 508.15 \\
Qwen-7B & 506.7 \\
Qwen-1.8B-Chat & 505.225 \\
Phi-2 & 497.4 \\
Yi-6B & 496.15 \\
Zhongjing-base & 490.1 \\
LLaMA2-7b & 486.2 \\
falcon-rw-1b & 481.15 \\
ChatGLM3-6b & 479.8 \\
Baichuan2-7B-Base & 479.175 \\
Baichuan2-13B-Chat & 463.75 \\
OPT-13b & 453.075 \\
Baichuan2-13B-Base & 446.225 \\
Skywork-13B-base & 445.8 \\
Qwen-1 8B & 435.775 \\
RWKV v5-Eagle-7B & 408.425 \\
Qwen-7B-Chat & 394.9 \\
Phi-1.5 & 385.975 \\
TinyLLaMA-1.1B-Chat-v0.6 & 366.125 \\'''

sss=r'''Baichuan2-7B-Chat & 0.517 & -3.571 & -0.038 & -5.315 & - & -2.975 \\
Zhongjing-Base & 0.465 & -8.488 & 2.662 & -1.290 & - & -2.372 \\
Baichuan2-7B-Base & 0.451 & -3.059 & 0.595 & -4.649 & - & -2.371 \\
Baichuan2-13B-Base & 0.439 & -2.943 & 0.882 & -4.390 & - & -2.150 \\
Pythia-12B & 0.480 & -0.233 & -3.888 & -2.612 & -1.012 & -1.936 \\
Falcon-rw-1B & 0.510 & 0.459 & -7.814 & 1.201 & -1.474 & -1.907 \\
LLaMA2-7B-chat & 0.505 & -8.308 & 2.695 & 0.664 & - & -1.650 \\
Baichuan-13B-chat & 0.467 & -3.645 & -1.078 & 0.413 & - & -1.436 \\
Baichuan2-13B-Chat & 0.495 & -3.541 & -0.995 & 0.232 & - & -1.435 \\
InternLM-chat-7B & 0.515 & -2.476 & -1.344 & 0.236 & - & -1.195 \\
Llama-2-7B & 0.434 & -7.314 & 3.092 & 1.279 & - & -0.981 \\
Phi-1.5 & 0.602 & -1.772 & 1.131 & -1.837 & - & -0.826 \\
LLaMA-7B & 0.450 & 1.270 & 0.177 & -7.776 & 3.266 & -0.766 \\
LlaMA-2-13B & 0.416 & -6.928 & 3.502 & 1.683 & - & -0.581 \\
TinyLLaMA-1.1B-Chat-v0.6 & 0.513 & 2.539 & -3.678 & - & - & -0.569 \\
Qwen-1.8B-Chat & 0.599 & 1.635 & -2.033 & - & - & -0.199 \\
Qwen-.8B & 0.520 & 1.899 & -2.082 & - & - & -0.091 \\
Yi-6B-Chat & 0.446 & 3.030 & -2.798 & - & - & 0.116 \\
OPT-2.7B & 0.475 & 1.970 & -2.228 & 1.192 & 1.143 & 0.519 \\
OPT-13B & 0.450 & 2.273 & -2.087 & 1.265 & 0.839 & 0.572 \\
Phi-2 & 0.487 & 1.882 & - & - & - & 1.882 \\
Mistral-7B-v0.1 & 0.398 & 1.110 & 5.347 & -0.661 & - & 1.932 \\
Qwen-7B-Chat & 0.466 & 1.809 & 3.606 & - & - & 2.708 \\
Qwen-7B & 0.441 & 1.892 & 3.689 & - & - & 2.791 \\
Colossal-LLaMA-2-7B-Base & 0.618 & 2.825 & 3.715 & - & - & 3.270 \\
RWKV-v5-Eagle-7B & 0.440 & 4.956 & 2.278 & - & - & 3.617 \\
ChatGLM3-6B & 0.832 & 5.567 & 1.684 & - & - & 3.626 \\
Qwen-14B-Chat & 0.445 & 2.682 & 4.847 & - & - & 3.764 \\
Baichuan-7B-chat & 0.492 & 3.055 & 4.806 & - & - & 3.931 \\
Yi-6B & 0.427 & 6.478 & 3.144 & - & - & 4.811 \\
Skywork-13B-Base & 0.429 & 7.163 & 3.261 & - & - & 5.212 \\
Zephyr-7B-beta & 0.435 & 7.340 & 3.928 & - & - & 5.634 \\'''


sss=r'''Falcon-rw-1B & 0.083 & -1.272 & -1.113 & -1.131 & -1.207 & -1.181 \\
Pythia-12B & 0.071 & -0.578 & -0.933 & -0.859 & -0.903 & -0.818 \\
OPT-2.7B & 0.082 & -0.658 & 0.024 & -0.528 & -0.915 & -0.519 \\
OPT-13B & 0.075 & -0.623 & 0.105 & -0.413 & -0.818 & -0.437 \\
Qwen-1.8B-Chat & 0.091 & -0.331 & -0.496 & - & - & -0.414 \\
TinyLlama-1.1B-Chat-v0.6 & 0.070 & -0.332 & -0.473 & - & - & -0.403 \\
InternLM-chat-7B & 0.080 & -0.482 & -0.301 & -0.250 & - & -0.344 \\
Baichuan-7B-chat & 0.064 & -0.032 & -0.424 & - & - & -0.228 \\
ChatGLM3-6B & 0.105 & -0.187 & -0.245 & - & - & -0.216 \\
Qwen-1.8B & 0.080 & -0.131 & -0.251 & - & - & -0.191 \\
Colossal-LLaMA-2-7B-Base & 0.065 & -0.042 & -0.199 & - & - & -0.121 \\
Phi-1.5 & 0.098 & 0.066 & -0.125 & -0.248 & - & -0.102 \\
LLaMA2-7B-chat & 0.060 & 0.132 & -0.186 & -0.093 & - & -0.049 \\
Zephyr-7B-beta & 0.059 & -0.049 & -0.033 & - & - & -0.041 \\
Phi-2 & 0.072 & -0.037 & - & - & - & -0.037 \\
Yi-6B & 0.058 & -0.071 & 0.022 & - & - & -0.024 \\
Yi-6B-Chat & 0.060 & -0.028 & 0.023 & - & - & -0.003 \\
Baichuan-13B-chat & 0.058 & 0.019 & 0.124 & -0.125 & - & 0.006 \\
LLaMA-7B & 0.052 & 0.214 & -0.425 & 0.379 & -0.067 & 0.025 \\
Baichuan2-7B-Chat & 0.068 & 0.343 & -0.035 & -0.073 & - & 0.078 \\
Mistral-7B-v0.1 & 0.053 & 0.381 & -0.028 & 0.018 & - & 0.124 \\
Skywork-13B-Base & 0.050 & 0.075 & 0.276 & - & - & 0.175 \\
RWKV-v5-Eagle-7B & 0.065 & 0.149 & 0.220 & - & - & 0.184 \\
Qwen-7B-Chat & 0.065 & 0.302 & 0.226 & - & - & 0.264 \\
Baichuan2-7B-Base & 0.059 & 0.523 & 0.157 & 0.185 & - & 0.289 \\
Qwen-7B & 0.061 & 0.428 & 0.430 & - & - & 0.429 \\
Baichuan2-13B-Chat & 0.062 & 0.299 & 0.628 & 0.512 & - & 0.480 \\
Zhongjing-Base & 0.050 & 0.756 & 0.269 & 0.569 & - & 0.531 \\
Llama-2-7B & 0.050 & 0.774 & 0.349 & 0.517 & - & 0.547 \\
Baichuan2-13B-Base & 0.053 & 1.019 & 0.797 & 0.900 & - & 0.905 \\
Qwen-14B-Chat & 0.049 & 1.301 & 1.939 & - & - & 1.620 \\
Llama-2-13B & 0.041 & 1.700 & 1.446 & 1.796 & - & 1.647 \\'''




sss=r'''OPT-13B  & May 2022 & -19.4 & 1689.0 & -30.2 \\
OPT-2.7B  & May 2022 & -18.8 & 1080.7 & -46.9 \\
LLaMA-7B  & Feb 2023 & -15.3 & 713.0 & 52.0 \\
Pythia-12B  & Mar 2023 & -8.1 & 802.7 & -11.1 \\
Falcon-rw-1B  & Apr 2023 & -26.8 & 607.4 & -47.7 \\
Baichuan-13B-chat  & Jun 2023 & -11.7 & 685.7 & 4.8 \\
Baichuan-7B-chat  & Jun 2023 & -14.6 & 726.6 & -16.5 \\
LLaMA-2-13B  & Jul 2023 & -11.1 & 769.6 & 65.9 \\
LLaMA-2-7B  & Jul 2023 & -12.6 & 684.6 & 23.2 \\
Baichuan-13B-Chat  & Jul 2023 & -7.0 & 717.2 & 12.1 \\
Baichuan-13B-Chat  & Jul 2023 & -7.0 & 717.2 & 12.1 \\
Zhongjing-Base  & Jul 2023 & -15.0 & 759.7 & 56.9 \\
InternLM-chat-7B  & Jul 2023 & -19.3 & 574.0 & -22.0 \\
Baichuan2-7B-Base  & Aug 2023 & -9.5 & 687.5 & 3.7 \\
Baichuan2-7B-Chat  & Aug 2023 & -8.4 & 781.8 & -11.6 \\
Colossal-LLaMA-2-7B-Base  & Sep 2023 & -21.2 & 696.3 & -36.2 \\
Qwen-14B-Chat  & Sep 2023 & -7.9 & 762.2 & 51.5 \\
Qwen-7B  & Sep 2023 & -11.7 & 662.4 & 7.4 \\
Qwen-7B-Chat  & Sep 2023 & -13.2 & 705.7 & -3.6 \\
Mistral-7B-v0.1  & Sep 2023 & -15.1 & 756.8 & 10.4 \\
Phi-1.5  & Sep 2023 & -26.0 & 1212.9 & -60.7 \\
Baichuan2-13B-Base  & Sep 2023 & -9.1 & 747.9 & 15.8 \\
Skywork-13B-Base  & Oct 2023 & -16.3 & 549.1 & 30.8 \\
ChatGLM3-6B  & Oct 2023 & -25.5 & 412.6 & -70.4 \\
Zephyr-7B-beta  & Oct 2023 & -21.1 & 506.9 & 3.7 \\
Yi-6B  & Nov 2023 & -9.4 & 451.7 & 24.6 \\
Yi-6B-Chat  & Nov 2023 & -9.4 & 506.5 & 20.2 \\
Qwen-1.8B  & Nov 2023 & -22.7 & 374.0 & -46.2 \\
Qwen-1.8B-Chat  & Nov 2023 & -25.3 & 426.8 & -50.3 \\
RWKV-v5-Eagle-7B  & Nov 2023 & -12.8 & 511.3 & 4.2 \\
TinyLLaMA-1.1B-Chat-v0.6  & Dec 2023 & -25.0 & 300.1 & -45.3 \\
Phi-2  & Dec 2023 & -21.2 & 669.3 & -44.7 \\'''
# print(sss)


classify=r'''\begin{tabular}{llll}
\toprule
period & [(-40, -20), (-20, 0)] & [(-60, -40), (-20, 0)] & [(-80, -60), (-20, 0)] \\
model &  &  &  \\
\midrule
Baichuan2-13B-Base & Nostalgia ** & Nostalgia *** & Nostalgia *** \\
Baichuan2-13B-Chat & Nostalgia * & Nostalgia *** & Nostalgia *** \\
Baichuan2-7B-Chat & Nostalgia ** & Balanced & Balanced \\
Colossal-LLaMA-2-7b-base & Nostalgia ** & Balanced & Nostalgia * \\
HF_RWKV_v5-Eagle-7B & Balanced & Balanced & Balanced \\
Llama-2-13b-hf & Balanced & Nostalgia *** & Nostalgia *** \\
Llama-2-7b-hf & Nostalgia *** & Nostalgia * & Balanced \\
Mixtral-8x22B-Instruct-v0.1 & Balanced & Nostalgia *** & Nostalgia *** \\
Phi-3-mini-4k-instruct & Balanced & Nostalgia *** & Nostalgia ** \\
Qwen-14B-Chat & Nostalgia ** & Nostalgia ** & Nostalgia *** \\
Qwen-1_8B & Balanced & Balanced & Nostalgia ** \\
Qwen-7B & Balanced & Balanced & Balanced \\
Qwen1.5-110b-chat & Nostalgia * & Nostalgia *** & Nostalgia *** \\
Skywork-13B-base & Balanced & Balanced & Balanced \\
Yi-6B & Balanced & Balanced & Balanced \\
Yi-6B-Chat & Nostalgia * & Nostalgia * & Nostalgia * \\
baichuan-7b-chat & Balanced & Balanced & Nostalgia * \\
chatglm3-6b & Balanced & Balanced & Nostalgia *** \\
command-r-plus & Nostalgia ** & Nostalgia *** & Nostalgia *** \\
falcon-rw-1b & Balanced & Balanced & Balanced \\
gpt4_0613 & Nostalgia *** & Nostalgia *** & Nostalgia *** \\
gpt4_1106 & Nostalgia *** & Nostalgia *** & Nostalgia *** \\
gpt_3.5_turbo_0613 & Balanced & Nostalgia *** & Nostalgia *** \\
internlm-chat-7b & Nostalgia ** & Balanced & Balanced \\
llama2-7b-chat-hf & Balanced & Nostalgia *** & Nostalgia *** \\
llama_hf_7b & Balanced & Nostalgia *** & Nostalgia ** \\
mistral-7b-v0.1 & Neophilia * & Nostalgia ** & Nostalgia *** \\
opt-13b & Balanced & Nostalgia *** & Nostalgia ** \\
opt-2.7b & Balanced & Neophilia * & Balanced \\
phi-1_5 & Nostalgia * & Nostalgia ** & Nostalgia *** \\
phi-2 & Nostalgia ** & Balanced & Nostalgia * \\
pythia-12b & Neophilia ** & Nostalgia *** & Nostalgia *** \\
zephyr-7b-beta & Nostalgia * & Nostalgia *** & Nostalgia *** \\
zhongjing-base & Balanced & Balanced & Nostalgia *** \\
\bottomrule
\end{tabular}'''
sss=classify

# path_to/gpt4_distil/analysis/future_p1p2/classify_gen.py
classify_gen=r'''\begin{tabular}{lll}
\toprule
period & [(0,6), (-20, 0)] & [(6, 12), (-20, 0)] \\
model &  &  \\
\midrule
Baichuan2-7B-Chat & Balanced & Neophilia ** \\
Colossal-LLaMA-2-7b-base & Balanced & Balanced \\
HF_RWKV_v5-Eagle-7B & Balanced & Unknown \\
Mixtral-8x22B-Instruct-v0.1 & Balanced & Unknown \\
Qwen-14B-Chat & Nostalgia ** & Balanced \\
Qwen-1_8B & Balanced & Unknown \\
Qwen-7B & Balanced & Balanced \\
Qwen1.5-110b-chat & Balanced & Unknown \\
Skywork-13B-base & Nostalgia ** & Balanced \\
Yi-6B-Chat & Balanced & Unknown \\
baichuan-7b-chat & Balanced & Balanced \\
command-r-plus & Balanced & Unknown \\
falcon-rw-1b & Nostalgia * & Nostalgia * \\
gpt4_0613 & Balanced & Balanced \\
gpt4_1106 & Nostalgia ** & Nostalgia *** \\
gpt_3.5_turbo_0613 & Balanced & Balanced \\
internlm-chat-7b & Balanced & Balanced \\
opt-13b & Neophilia ** & Nostalgia ** \\
opt-2.7b & Neophilia * & Nostalgia ** \\
phi-2 & Nostalgia ** & Unknown \\
zhongjing-base & Balanced & Nostalgia * \\
\bottomrule
\end{tabular}'''

# sss=classify_gen.replace('Balanced' ,'Future Stable')\
#                 .replace('Nostalgia','Future Reduced')\
#                 .replace('Neophilia','Future Enhanced')


gray_time=r'''Baichuan2-13B-Base & \cellcolor{gray!25}0.5054 & \cellcolor{gray!25}0.3964 & 0.3191 & 0.4324 & 0.3582 \\
Baichuan2-13B-Chat & \cellcolor{gray!25}0.5168 & \cellcolor{gray!25}0.4234 & 0.3121 & 0.4162 & 0.2687 \\
Baichuan2-7B-Chat & \cellcolor{gray!25}0.3775 & \cellcolor{gray!25}0.3333 & 0.2340 & 0.3459 & 0.3955 \\
Colossal-LLaMA-2-7b-base & \cellcolor{gray!25}0.4270 & \cellcolor{gray!25}0.4414 & \cellcolor{gray!25}0.3262 & 0.3892 & 0.3134 \\
HF_RWKV_v5-Eagle-7B & \cellcolor{gray!25}0.2904 & \cellcolor{gray!25}0.2883 & \cellcolor{gray!25}0.2340 & 0.2919 & 0.2985 \\
Llama-2-13b-hf & \cellcolor{gray!25}0.5281 & \cellcolor{gray!25}0.4775 & 0.3688 & 0.3946 & 0.3955 \\
Llama-2-7b-hf & \cellcolor{gray!25}0.2816 & \cellcolor{gray!25}0.1802 & 0.1986 & 0.2324 & 0.3134 \\
Mixtral-8x22B-Instruct-v0.1 & \cellcolor{gray!25}0.1222 & \cellcolor{gray!25}0.1171 & \cellcolor{gray!25}0.0709 & \cellcolor{gray!25}0.0919 & 0.0373 \\
Phi-3-mini-4k-instruct & \cellcolor{gray!25}0.4048 & \cellcolor{gray!25}0.3333 & \cellcolor{gray!25}0.2553 & \cellcolor{gray!25}0.3081 & 0.2836 \\
Qwen-14B-Chat & \cellcolor{gray!25}0.4110 & \cellcolor{gray!25}0.3153 & \cellcolor{gray!25}0.2128 & 0.2378 & 0.2910 \\
Qwen-1_8B & \cellcolor{gray!25}0.3589 & \cellcolor{gray!25}0.2973 & \cellcolor{gray!25}0.2270 & 0.2541 & 0.3209 \\
Qwen-7B & \cellcolor{gray!25}0.3708 & \cellcolor{gray!25}0.3423 & \cellcolor{gray!25}0.2695 & 0.3189 & 0.2761 \\
Qwen1.5-110b-chat & \cellcolor{gray!25}0.5936 & \cellcolor{gray!25}0.5225 & \cellcolor{gray!25}0.4184 & \cellcolor{gray!25}0.4486 & 0.4104 \\
Skywork-13B-base & \cellcolor{gray!25}0.3739 & \cellcolor{gray!25}0.3063 & \cellcolor{gray!25}0.3333 & 0.3243 & 0.2836* \\
Yi-6B & \cellcolor{gray!25}0.2991 & \cellcolor{gray!25}0.2072 & \cellcolor{gray!25}0.2128 & 0.1892 & 0.2985 \\
Yi-6B-Chat & \cellcolor{gray!25}0.3925 & \cellcolor{gray!25}0.3694 & \cellcolor{gray!25}0.2695 & 0.2378 & 0.3657 \\
baichuan-7b-chat & \cellcolor{gray!25}0.3326 & \cellcolor{gray!25}0.1982 & \cellcolor{gray!25}0.2624 & 0.2000* & 0.2910 \\
chatglm3-6b & \cellcolor{gray!25}0.4363 & \cellcolor{gray!25}0.3964 & \cellcolor{gray!25}0.2624 & 0.3459 & 0.3134 \\
command-r-plus & \cellcolor{gray!25}0.5797 & \cellcolor{gray!25}0.4234 & \cellcolor{gray!25}0.3617 & \cellcolor{gray!25}0.4216 & 0.3806 \\
falcon-rw-1b & \cellcolor{gray!25}0.2223 & 0.1622 & 0.1844 & 0.2270 & 0.2239 \\
gpt4_0613 & \cellcolor{gray!25}0.6168 & \cellcolor{gray!25}0.4144 & 0.4043 & 0.3838 & 0.4254 \\
gpt4_1106 & \cellcolor{gray!25}0.6880 & \cellcolor{gray!25}0.6126 & \cellcolor{gray!25}0.4184 & 0.4649 & 0.3731 \\
gpt_3.5_turbo_0613 & \cellcolor{gray!25}0.5003 & \cellcolor{gray!25}0.3874 & 0.3191 & 0.4432 & 0.3209 \\
internlm-chat-7b & \cellcolor{gray!25}0.3553 & \cellcolor{gray!25}0.3604 & 0.2624 & 0.2865 & 0.3060 \\
llama2-7b-chat-hf & \cellcolor{gray!25}0.4621 & \cellcolor{gray!25}0.3784 & 0.3262 & 0.3838 & 0.3731 \\
llama_hf_7b & \cellcolor{gray!25}0.3187 & 0.1892 & 0.1773 & 0.2324 & 0.2313 \\
mistral-7b-v0.1 & \cellcolor{gray!25}0.4435 & \cellcolor{gray!25}0.4414 & \cellcolor{gray!25}0.3262 & 0.3622 & 0.3209 \\
opt-13b & 0.4817 & 0.5135 & 0.3333 & 0.4865 & 0.3060 \\
opt-2.7b & 0.2310* & 0.1892** & 0.1844** & 0.2270* & 0.2612 \\
phi-1_5 & \cellcolor{gray!25}0.4116 & \cellcolor{gray!25}0.4685 & \cellcolor{gray!25}0.2908 & 0.3838 & 0.2687 \\
phi-2 & \cellcolor{gray!25}0.3290 & \cellcolor{gray!25}0.2252 & \cellcolor{gray!25}0.2199 & 0.2432 & 0.2687 \\
pythia-12b & \cellcolor{gray!25}0.4801 & 0.4955 & 0.3546** & 0.4162* & 0.3507** \\
zephyr-7b-beta & \cellcolor{gray!25}0.4043 & \cellcolor{gray!25}0.4324 & \cellcolor{gray!25}0.3121 & 0.3135 & 0.2836 \\
zhongjing-base & \cellcolor{gray!25}0.3971 & \cellcolor{gray!25}0.3784 & 0.1844 & 0.3243 & 0.3433 \\'''

# sss=gray_time
# print('to return!!!!!!!!!!!!!!')
# print(parse_possible_name(sss.replace('nan','-')))

'''
python path_to/gpt4_distil/standard_name.py
'''