
from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    model = IsolationForest(contamination=0.03)
    df['anomaly'] = model.fit_predict(df[['Sales']])
    return df

if __name__ == "__main__":
    print("Anomaly Detection Ready")
