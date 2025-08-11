import json

def export_summary_to_csv(df, filename='weekly_summary.csv'):
    df.to_csv(filename, index=False)

def export_alerts_to_txt(df, filename='extreme_alerts.txt'):
    with open(filename, 'w') as f:
        for _, row in df.iterrows():
            f.write(f"Alert: {row['city']} on {row['log_date']} -> Temp: {row['temperature']}°C, Rain: {row['rainfall']}mm\n")

def export_backup_to_json(df, filename='weather_backup.json'):
    df['log_date'] = df['log_date'].astype(str)
    with open(filename, 'w') as f:
        json.dump(df.to_dict(orient='records'), f, indent=4)
