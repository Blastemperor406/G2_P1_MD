import pandas as pd
from data_storage.kafka import Kafka

class DataProcessor:
    def __init__(self, kafka_hosts):
        self.kafka = Kafka(hosts=kafka_hosts)

    def load_csv_file(self, csv_file_path):
        try:
            df = pd.read_csv(csv_file_path)
            print("CSV file loaded successfully.")
            return df
        except FileNotFoundError:
            print("Error: File not found.")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

    def process_data_and_insert_to_kafka(self, df):
        if df is not None:
            for index, row in df.iterrows():
                data_dict = {
                    "Name": row["name"],
                    "Description": row["description"],
                    "Website": row["website"]
                }
                self.kafka.insert_products(data_dict)  # Assuming kafka.insert_data() is a valid function

    def main(self):
        csv_file_path = "/home/monish/Documents/G2_P1_MD/data_collectors/products.csv"
        df = self.load_csv_file(csv_file_path)
        if df is not None:
            self.process_data_and_insert_to_kafka(df)

if __name__ == "__main__":
    kafka_hosts = ["0.0.0.0:9093", "0.0.0.0:9092", "0.0.0.0:9094"]
    data_processor = DataProcessor(kafka_hosts)
    data_processor.main()
