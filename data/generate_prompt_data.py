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



rules_list = [
    "Acceptable actions include ['Login', 'View', 'Access']. Users can choose resources from the list: ['Dashboard', 'Reports', 'Documents']. The status must not be Unauthorized.",
    "Authorized actions consist of ['Login', 'View', 'Access']. Available resources to select are ['Dashboard', 'Reports', 'Documents']. The status is not allowed to be Unauthorized.",
    "Permitted actions are ['Login', 'View', 'Access']. Resources can be selected from ['Dashboard', 'Reports', 'Documents']. Unauthorized status is not permissible.",
    "Users can perform actions such as ['Login', 'View', 'Access']. Allowed resource choices encompass ['Dashboard', 'Reports', 'Documents']. The status should not be Unauthorized.",
    "The following actions are valid: ['Login', 'View', 'Access']. Users have the option to select resources from ['Dashboard', 'Reports', 'Documents']. Unauthorized status is disallowed."
]

convert_to_prompt(rules_list,"data/generated_data/user_actions.csv","user_actions_prompted")