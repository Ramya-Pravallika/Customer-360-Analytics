import pandas as pd, joblib, os

def score(model_path='ml/model/churn.joblib', features='data/features_churn.csv'):
    model = joblib.load(model_path)
    df = pd.read_csv(features)
    ids = df['account_id']
    X = df.drop(columns=['account_id','churn'])
    preds = model.predict_proba(X)[:,1]
    out = pd.DataFrame({'account_id': ids, 'churn_prob': preds})
    os.makedirs('ml', exist_ok=True)
    out.to_csv('ml/scores.csv', index=False)
    print('Wrote ml/scores.csv')

if __name__=='__main__':
    score()
