from weather_logger.logger import log_weather
from weather_logger.analyzer import fetch_data, generate_weekly_summary, detect_anomalies
from weather_logger.exporter import export_summary_to_csv, export_alerts_to_txt, export_backup_to_json
from weather_logger.db import create_tables

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Localized Weather Logger CLI (SQLAlchemy)")
    parser.add_argument("--init-db", action="store_true", help="Initialize database schema")
    parser.add_argument("--log", nargs=4, metavar=("CITY", "TEMP", "HUMID", "RAIN"), help="Log a weather entry")
    parser.add_argument("--analyze", action="store_true", help="Analyze and export summaries")

    args = parser.parse_args()

    if args.init_db:
        create_tables()
        print("Database initialized.")

    if args.log:
        city, temp, humid, rain = args.log
        log_weather(city, float(temp), float(humid), float(rain))
        print("Weather logged.")

    if args.analyze:
        df = fetch_data()
        if df.empty:
            print("No data available for analysis.")
            return
        summary = generate_weekly_summary(df)
        alerts = detect_anomalies(df)
        export_summary_to_csv(summary)
        export_alerts_to_txt(alerts)
        export_backup_to_json(df)
        print("Analysis and exports complete.")

if __name__ == "__main__":
    main()
