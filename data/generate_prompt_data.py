import pandas as pd

def convert_to_prompt(rules,path,name):
    df = pd.read_csv(path)
    data = pd.DataFrame(columns=["rule","entry","label"])
    prompts = []
    for index, row in df.iterrows():
        prompt = ' '.join([f"{column} is {row[column]}" for column in df.columns if column != 'Compliant'])
        prompts.append(prompt)

    data['rule'] = [rules]*len(prompts)
    data['entry'] = prompts
    data['label'] = df['Compliant']
    data['label']=data['label'].astype(int)
    csv_file_path = 'data/prompted_data/'+name+'.csv'
    data.to_csv(csv_file_path, index=False)
