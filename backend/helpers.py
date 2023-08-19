import pandas as pd
from transformers import AutoTokenizer

def convert_to_prompt(rules, df):
    data = pd.DataFrame(columns=["rule", "entry", "label"])
    prompts = []
    
    for _, row in df.iterrows():
        prompt = ' '.join([f"{column} is {row[column]}" for column in df.columns if column != 'Compliant'])
        prompts.append(prompt)

    data['rule'] = rules*len(prompts)
    data['entry'] = prompts
    data['label'] = df['Compliant']
    data['label'] = data['label'].astype(int)
    
    return data

def load_rules(filename):
    with open(filename, 'r') as file:
        rules = file.read()  # Read the entire content as a single string
    return rules

tokenizer = AutoTokenizer.from_pretrained("model/tokenizer")
task_to_keys = {
    "rte": ("rule", "entry")
}
rule, entry = task_to_keys['rte']

def preprocess_function(param):
    return tokenizer(param[rule], param[entry], truncation=True)