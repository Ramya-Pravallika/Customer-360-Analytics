import pandas as pd
from xgboost import XGBClassifier
import joblib

def train(input_csv='data/features_churn.csv', out='ml/model'):
    df = pd.read_csv(input_csv)
    if 'churn' not in df.columns:
        raise Exception('features file must contain churn column')
    X = df.drop(columns=['account_id','churn'])
    y = df['churn']
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X, y)
    joblib.dump(model, out + '/churn.joblib')
    print('Model saved to', out)

if __name__=='__main__':
    train()
