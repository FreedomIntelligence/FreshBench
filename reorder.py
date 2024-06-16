

import re

def replace_llama(text):
    return re.sub(r'llama', 'LLaMA', text, flags=re.IGNORECASE)

# 示例文本
# input_text = "Llama, llamas, and LlaMa are all different cases of llama."

# output_text = replace_llama(input_text)
# print(output_text)


def reorder(to_order_sss=None):

    
    if to_order_sss is None:
        to_order_sss=r'''Falcon-rw-1B & 0.083 & -1.272 & -1.113 & -1.131 & -1.207 & -1.181 \\
Pythia-12B & 0.071 & -0.578 & -0.933 & -0.859 & -0.903 & -0.818 \\
OPT-2.7B & 0.082 & -0.658 & 0.024 & -0.528 & -0.915 & -0.519 \\
OPT-13B & 0.075 & -0.623 & 0.105 & -0.413 & -0.818 & -0.437 \\
Qwen-1.8B-Chat & 0.091 & -0.331 & -0.496 & - & - & -0.414 \\
TinyLLaMA-1.1B-Chat-v0.6 & 0.070 & -0.332 & -0.473 & - & - & -0.403 \\
InternLM-Chat-7B & 0.080 & -0.482 & -0.301 & -0.250 & - & -0.344 \\
Baichuan-7B-Chat & 0.064 & -0.032 & -0.424 & - & - & -0.228 \\
ChatGLM3-6B & 0.105 & -0.187 & -0.245 & - & - & -0.216 \\
Qwen-1.8B & 0.080 & -0.131 & -0.251 & - & - & -0.191 \\
Colossal-LLaMA-2-7B-Base & 0.065 & -0.042 & -0.199 & - & - & -0.121 \\
Phi-1.5 & 0.098 & 0.066 & -0.125 & -0.248 & - & -0.102 \\
LLaMA-2-7B-Chat & 0.060 & 0.132 & -0.186 & -0.093 & - & -0.049 \\
Zephyr-7B-beta & 0.059 & -0.049 & -0.033 & - & - & -0.041 \\
Phi-2 & 0.072 & -0.037 & - & - & - & -0.037 \\
Yi-6B & 0.058 & -0.071 & 0.022 & - & - & -0.024 \\
Yi-6B-Chat & 0.060 & -0.028 & 0.023 & - & - & -0.003 \\
Baichuan-13B-Chat & 0.058 & 0.019 & 0.124 & -0.125 & - & 0.006 \\
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
LLaMA-2-7B & 0.050 & 0.774 & 0.349 & 0.517 & - & 0.547 \\
Baichuan2-13B-Base & 0.053 & 1.019 & 0.797 & 0.900 & - & 0.905 \\
Qwen-14B-Chat & 0.049 & 1.301 & 1.939 & - & - & 1.620 \\
LLaMA-2-13B & 0.041 & 1.700 & 1.446 & 1.796 & - & 1.647 \\'''
    to_order_sss=replace_llama(to_order_sss)
    to_order_sss=to_order_sss.replace('LLaMA2-7B-Chat','LLaMA-2-7B-Chat')
    to_order_sss=to_order_sss.replace('Gemini','Gemini-pro')
    to_order_sss=to_order_sss.replace('TinyLlama-1.1B-Chat-v0.6','TinyLLaMA-1.1B-Chat-v0.6')

    to_order_list = to_order_sss.split('\n')

    sss=r'''OPT-13B  & May 2022 & -19.4 & 1689.0 & -30.2 \\
OPT-2.7B  & May 2022 & -18.8 & 1080.7 & -46.9 \\
LLaMA-7B  & Feb 2023 & -15.3 & 713.0 & 52.0 \\
Pythia-12B  & Mar 2023 & -8.1 & 802.7 & -11.1 \\
Falcon-rw-1B  & Apr 2023 & -26.8 & 607.4 & -47.7 \\
Baichuan-13B-Chat  & Jun 2023 & -11.7 & 685.7 & 4.8 \\
Baichuan-7B-Chat  & Jun 2023 & -14.6 & 726.6 & -16.5 \\
InternLM-Chat-7B  & Jun 2023 & -19.3 & 574.0 & -22.0 \\
GPT-3.5-turbo-0613 & ??? \\
GPT-3.5-turbo-230613 & ??? \\
GPT-4-230613 & ??? \\
LLaMA-2-13B  & Jul 2023 & -11.1 & 769.6 & 65.9 \\
LLaMA-2-7B  & Jul 2023 & -12.6 & 684.6 & 23.2 \\
LLaMA-2-7B-Chat  & Jul 2023 & ??? \\
Baichuan-13B-Chat  & Jul 2023 & -7.0 & 717.2 & 12.1 \\
Baichuan2-7B-Base  & Aug 2023 & -9.5 & 687.5 & 3.7 \\
Baichuan2-7B-Chat  & Aug 2023 & -8.4 & 781.8 & -11.6 \\
Baichuan2-13B-Base  & Aug 2023 & -9.1 & 747.9 & 15.8 \\
Baichuan2-13B-Chat  & Aug 2023 & -7.0 & 717.2 & 12.1 \\
Zhongjing-Base  & Sep 2023 & -15.0 & 759.7 & 56.9 \\
Mistral-7B-v0.1  & Sep 2023 & -15.1 & 756.8 & 10.4 \\
Phi-1.5  & Sep 2023 & -26.0 & 1212.9 & -60.7 \\
Colossal-LLaMA-2-7B-Base  & Sep 2023 & -21.2 & 696.3 & -36.2 \\
Qwen-14B-Chat  & Sep 2023 & -7.9 & 762.2 & 51.5 \\
Qwen-7B  & Sep 2023 & -11.7 & 662.4 & 7.4 \\
Qwen-7B-Chat  & Sep 2023 & -13.2 & 705.7 & -3.6 \\
Skywork-13B-Base  & Oct 2023 & -16.3 & 549.1 & 30.8 \\
ChatGLM3-6B  & Oct 2023 & -25.5 & 412.6 & -70.4 \\
Zephyr-7B-beta  & Oct 2023 & -21.1 & 506.9 & 3.7 \\
Yi-6B  & Nov 2023 & -9.4 & 451.7 & 24.6 \\
Yi-6B-Chat  & Nov 2023 & -9.4 & 506.5 & 20.2 \\
Qwen-1.8B  & Nov 2023 & -22.7 & 374.0 & -46.2 \\
Qwen-1.8B-Chat  & Nov 2023 & -25.3 & 426.8 & -50.3 \\
RWKV-v5-Eagle-7B  & Nov 2023 & -12.8 & 511.3 & 4.2 \\
GPT-4-231106 & ??? \\
GPT-4-1106 & ??? \\
TinyLLaMA-1.1B-Chat-v0.6 & Dec 2023 & -25.0 & 300.1 & -45.3 \\
Phi-2  & Dec 2023 & -21.2 & 669.3 & -44.7 \\
Gemini-pro & ??? \\
Command R+ & \\
Mixtral-8x22B-Instruct-v0.1 & \\
Phi-3-mini-4k-instruct & \\
Qwen1.5-110B-Chat & \\
    '''
    data = sss.split('\n')
    '''
GPT-4-1106 & 0.63 & 27.73 & 15.71 & 28.47 & 23.22 & 23.78 \\
TinyLlama-1.1B-Chat-v0.6 & 0.71 & 13.27 & -16.30 & - & - & -1.51 \\
Gemini-pro & 0.71 & -15.15 & -41.28 & - & - & -28.21 \\
    '''
    order_data_split = [(line.split(" & ")[0].strip(), line) for line in data]

    data_order_dict = {model: i for i,(model, line) in enumerate(order_data_split)}

    # breakpoint()

    to_order_data_dic = {line.split(" & ")[0].strip(): line for line in to_order_list}

    sorted_data = [to_order_data_dic[model] for model in data_order_dict if model in to_order_data_dic]

    if len(sorted_data) != len(to_order_list):
        print(f"Some data is missing, only {len(sorted_data)} out of {len(to_order_list)} found.")
        print(f"Missing data:")
        # for model in to_order_list:
        #     if model not in to_order_data_dic.values():
        #         print(model)
        for model in to_order_list:
            if model not in sorted_data :
                print(model)
     

    print(f'\n\n\n\n##############################################\n\n\n\n')

    print(f"Original data:{len(to_order_list)}, Sorted data:{len(sorted_data)}")
    set1=set(to_order_list)
    set2=set(sorted_data)
    print(f"set1-set2:{set1-set2}")
    for line in sorted_data:
        print(line)

    return '\n'.join(sorted_data)


'''
cd path_to/gpt4_distil/
python reorder.py
'''
table_past_bias=r'''Baichuan2-13B-Base & Nostalgia ** & Nostalgia *** & Nostalgia *** \\
Baichuan2-13B-Chat & Nostalgia * & Nostalgia *** & Nostalgia *** \\
Baichuan2-7B-Chat & Nostalgia ** & Balanced & Balanced \\
Colossal-LLaMA-2-7B-Base & Nostalgia ** & Balanced & Nostalgia * \\
RWKV-v5-Eagle-7B & Balanced & Balanced & Balanced \\
Llama-2-13B & Balanced & Nostalgia *** & Nostalgia *** \\
Llama-2-7B & Nostalgia *** & Nostalgia * & Balanced \\
Mixtral-8x22B-Instruct-v0.1 & Balanced & Nostalgia *** & Nostalgia *** \\
Phi-3-mini-4k-instruct & Balanced & Nostalgia *** & Nostalgia ** \\
Qwen-14B-Chat & Nostalgia ** & Nostalgia ** & Nostalgia *** \\
Qwen-1.8B & Balanced & Balanced & Nostalgia ** \\
Qwen-7B & Balanced & Balanced & Balanced \\
Qwen1.5-110B-Chat & Nostalgia * & Nostalgia *** & Nostalgia *** \\
Skywork-13B-Base & Balanced & Balanced & Balanced \\
Yi-6B & Balanced & Balanced & Balanced \\
Yi-6B-Chat & Nostalgia * & Nostalgia * & Nostalgia * \\
Baichuan-7B-Chat & Balanced & Balanced & Nostalgia * \\
Chatglm3-6B & Balanced & Balanced & Nostalgia *** \\
Command R+ & Nostalgia ** & Nostalgia *** & Nostalgia *** \\
Falcon-rw-1B & Balanced & Balanced & Balanced \\
GPT-4-230613 & Nostalgia *** & Nostalgia *** & Nostalgia *** \\
GPT-4-231106 & Nostalgia *** & Nostalgia *** & Nostalgia *** \\
GPT-3.5-turbo-230613 & Balanced & Nostalgia *** & Nostalgia *** \\
InternLM-Chat-7B & Nostalgia ** & Balanced & Balanced \\
LLaMA2-7B-Chat & Balanced & Nostalgia *** & Nostalgia *** \\
LLaMA-7B & Balanced & Nostalgia *** & Nostalgia ** \\
Mistral-7B-v0.1 & NeoPhilia * & Nostalgia ** & Nostalgia *** \\
OPT-13B & Balanced & Nostalgia *** & Nostalgia ** \\
OPT-2.7B & Balanced & NeoPhilia * & Balanced \\
Phi-1.5 & Nostalgia * & Nostalgia ** & Nostalgia *** \\
Phi-2 & Nostalgia ** & Balanced & Nostalgia * \\
Pythia-12B & NeoPhilia ** & Nostalgia *** & Nostalgia *** \\
Zephyr-7B-beta & Nostalgia * & Nostalgia *** & Nostalgia *** \\
Zhongjing-Base & Balanced & Balanced & Nostalgia *** \\'''



grey=r'''Baichuan2-13B-Base & \cellcolor{gray!25}0.5054 & \cellcolor{gray!25}0.3964 & 0.3191 & 0.4324 & 0.3582 \\
Baichuan2-13B-Chat & \cellcolor{gray!25}0.5168 & \cellcolor{gray!25}0.4234 & 0.3121 & 0.4162 & 0.2687 \\
Baichuan2-7B-Chat & \cellcolor{gray!25}0.3775 & \cellcolor{gray!25}0.3333 & 0.2340 & 0.3459 & 0.3955 \\
Colossal-LLaMA-2-7B-Base & \cellcolor{gray!25}0.4270 & \cellcolor{gray!25}0.4414 & \cellcolor{gray!25}0.3262 & 0.3892 & 0.3134 \\
RWKV-v5-Eagle-7B & \cellcolor{gray!25}0.2904 & \cellcolor{gray!25}0.2883 & \cellcolor{gray!25}0.2340 & 0.2919 & 0.2985 \\
Llama-2-13B & \cellcolor{gray!25}0.5281 & \cellcolor{gray!25}0.4775 & 0.3688 & 0.3946 & 0.3955 \\
Llama-2-7B & \cellcolor{gray!25}0.2816 & \cellcolor{gray!25}0.1802 & 0.1986 & 0.2324 & 0.3134 \\
Mixtral-8x22B-Instruct-v0.1 & \cellcolor{gray!25}0.1222 & \cellcolor{gray!25}0.1171 & \cellcolor{gray!25}0.0709 & \cellcolor{gray!25}0.0919 & 0.0373 \\
Phi-3-mini-4k-instruct & \cellcolor{gray!25}0.4048 & \cellcolor{gray!25}0.3333 & \cellcolor{gray!25}0.2553 & \cellcolor{gray!25}0.3081 & 0.2836 \\
Qwen-14B-Chat & \cellcolor{gray!25}0.4110 & \cellcolor{gray!25}0.3153 & \cellcolor{gray!25}0.2128 & 0.2378 & 0.2910 \\
Qwen-1.8B & \cellcolor{gray!25}0.3589 & \cellcolor{gray!25}0.2973 & \cellcolor{gray!25}0.2270 & 0.2541 & 0.3209 \\
Qwen-7B & \cellcolor{gray!25}0.3708 & \cellcolor{gray!25}0.3423 & \cellcolor{gray!25}0.2695 & 0.3189 & 0.2761 \\
Qwen1.5-110B-Chat & \cellcolor{gray!25}0.5936 & \cellcolor{gray!25}0.5225 & \cellcolor{gray!25}0.4184 & \cellcolor{gray!25}0.4486 & 0.4104 \\
Skywork-13B-Base & \cellcolor{gray!25}0.3739 & \cellcolor{gray!25}0.3063 & \cellcolor{gray!25}0.3333 & 0.3243 & 0.2836* \\
Yi-6B & \cellcolor{gray!25}0.2991 & \cellcolor{gray!25}0.2072 & \cellcolor{gray!25}0.2128 & 0.1892 & 0.2985 \\
Yi-6B-Chat & \cellcolor{gray!25}0.3925 & \cellcolor{gray!25}0.3694 & \cellcolor{gray!25}0.2695 & 0.2378 & 0.3657 \\
Baichuan-7B-Chat & \cellcolor{gray!25}0.3326 & \cellcolor{gray!25}0.1982 & \cellcolor{gray!25}0.2624 & 0.2000* & 0.2910 \\
ChatGLM3-6B & \cellcolor{gray!25}0.4363 & \cellcolor{gray!25}0.3964 & \cellcolor{gray!25}0.2624 & 0.3459 & 0.3134 \\
Command R+ & \cellcolor{gray!25}0.5797 & \cellcolor{gray!25}0.4234 & \cellcolor{gray!25}0.3617 & \cellcolor{gray!25}0.4216 & 0.3806 \\
Falcon-rw-1B & \cellcolor{gray!25}0.2223 & 0.1622 & 0.1844 & 0.2270 & 0.2239 \\
GPT-4-230613 & \cellcolor{gray!25}0.6168 & \cellcolor{gray!25}0.4144 & 0.4043 & 0.3838 & 0.4254 \\
GPT-4-231106 & \cellcolor{gray!25}0.6880 & \cellcolor{gray!25}0.6126 & \cellcolor{gray!25}0.4184 & 0.4649 & 0.3731 \\
GPT-3.5-turbo-230613 & \cellcolor{gray!25}0.5003 & \cellcolor{gray!25}0.3874 & 0.3191 & 0.4432 & 0.3209 \\
InternLM-Chat-7B & \cellcolor{gray!25}0.3553 & \cellcolor{gray!25}0.3604 & 0.2624 & 0.2865 & 0.3060 \\
LLaMA2-7B-Chat & \cellcolor{gray!25}0.4621 & \cellcolor{gray!25}0.3784 & 0.3262 & 0.3838 & 0.3731 \\
LLaMA-7B & \cellcolor{gray!25}0.3187 & 0.1892 & 0.1773 & 0.2324 & 0.2313 \\
Mistral-7B-v0.1 & \cellcolor{gray!25}0.4435 & \cellcolor{gray!25}0.4414 & \cellcolor{gray!25}0.3262 & 0.3622 & 0.3209 \\
OPT-13B & 0.4817 & 0.5135 & 0.3333 & 0.4865 & 0.3060 \\
OPT-2.7B & 0.2310* & 0.1892** & 0.1844** & 0.2270* & 0.2612 \\
Phi-1.5 & \cellcolor{gray!25}0.4116 & \cellcolor{gray!25}0.4685 & \cellcolor{gray!25}0.2908 & 0.3838 & 0.2687 \\
Phi-2 & \cellcolor{gray!25}0.3290 & \cellcolor{gray!25}0.2252 & \cellcolor{gray!25}0.2199 & 0.2432 & 0.2687 \\
Pythia-12B & \cellcolor{gray!25}0.4801 & 0.4955 & 0.3546** & 0.4162* & 0.3507** \\
Zephyr-7B-beta & \cellcolor{gray!25}0.4043 & \cellcolor{gray!25}0.4324 & \cellcolor{gray!25}0.3121 & 0.3135 & 0.2836 \\
Zhongjing-Base & \cellcolor{gray!25}0.3971 & \cellcolor{gray!25}0.3784 & 0.1844 & 0.3243 & 0.3433 \\'''

reorder(grey)