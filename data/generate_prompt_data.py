import pandas as pd
import random

def convert_to_prompt(rules_list, path, name):
    df = pd.read_csv(path)
    data = pd.DataFrame(columns=["rule", "entry", "label"])
    prompts = []
    
    for index, row in df.iterrows():
        prompt = ' '.join([f"{column} is {row[column]}" for column in df.columns if column != 'Compliant'])
        prompts.append(prompt)

    rules = []
    for _ in range(len(prompts)):
        chosen_rule = random.choice(rules_list)
        rules.append(chosen_rule)

    data['rule'] = rules
    data['entry'] = prompts
    data['label'] = df['Compliant']
    data['label'] = data['label'].astype(int)
    
    csv_file_path = 'data/prompted_data/' + name + '.csv'
    data.to_csv(csv_file_path, index=False)