import openai
import json
import requests
import urllib3

# Disable warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class PostRobot:
    def __init__(self):
        self.api_key = None
        self.proxy = None
        self.model_name = "gpt-4-turbo"
        self.role = None
        self.base_url = "https://api.ai-gaochao.cn/v1/chat/completions"
        # self.base_url = "https://openrouter.ai/api/v1",
        self.org = None # should be a list of "org-name"
        self.time_out = 20
        self.temperature = 0

    def set_role(self, role):
        if self.role is None:
            self.role = {
                "role": "system",
                "content": role,
            }

    def set_thinking_engine(self, openai_key=None, proxy=None, org=None):
        self.set_openai_key(openai_key)
        self.set_proxy(proxy)
        self.set_org(org)
    
    def set_org(self, org):
        self.org = org

    def set_openai_key(self, apikey):
        self.api_key = apikey

    def set_proxy(self, proxy):
        self.proxy = proxy

    def request_chatgpt(self, parameters):
        openai.api_key = self.api_key
        openai.api_base = self.base_url

        headers = {
        # "Content-Type": "application/json",
        "Authorization": f"Bearer {self.api_key}",
        }

        try:
            # breakpoint()
            raw_response = requests.post(url=self.base_url, headers=headers, json=parameters, verify=False, timeout=self.time_out)
        except:
            # print("request timeout")
            return None
        
        try:
            response = json.loads(raw_response.content.decode("utf-8"))
        except:
            print("response decode error")
            # breakpoint()
            return None
        # breakpoint()
        print('response:', response)
        try:
            content = response["choices"][0]["message"]["content"]
        except:
            if "error" in response.keys() and "code" in response["error"].keys():
                content = response["error"]["code"]
                print(f"api key: {self.api_key}, org: {self.org}, error code: {content}")
            else:
                print(f"response not have error")
                print(f'api key: {self.api_key}, org: {self.org}, response: {response}')

        if content is None:
            print("content is None")
            return None
        elif type(content) == int:
            print(f"error code: {content}")
            return None
        elif 'insufficient_quota' in content:
            print(f"quota insufficient for key: {self.api_key} and org: {self.org}")
            return None
        elif 'account_deactivated' in content:
            print(f"account deactivated: {self.api_key} and org: {self.org}")
            return None
        elif "billing_not_active" in content:
            print(f"billing_not_active: {self.api_key} and org: {self.org}")
            return None
        elif "model_not_found" in content:
            print(f"model_not_found: {self.api_key} and org: {self.org}")
            return None
        elif "invalid_organization" in content:
            print(f"invalid_organization: {self.api_key} and org: {self.org}")
            return None
        return content

    def get_prompt(self, sample):
        text = ""
        if 'instruction' not in sample.keys() and 'input' not in sample.keys() and 'text' in sample.keys():
            print('text as prompt')
            text = sample["text"]
            return text
        if len(sample["instruction"]) > 0 and len(sample["input"]) > 0:
            text = sample["instruction"] + "\n" + sample["input"]
        elif len(sample["instruction"]) > 0 and len(sample["input"]) == 0:
            text = sample["instruction"]
        elif len(sample["instruction"]) == 0 and len(sample["input"]) > 0:
            text = sample["input"]
        return text

    def generate(self, new_message):
        messages = []
        if self.role is not None:
            messages.append(self.role)
        messages.append({"role": "user", "content": new_message})
        parameters = {
            "model": self.model_name,
            "messages": messages,
            "temperature": 0,
        }
        response = self.request_chatgpt(parameters)
        return True, response
