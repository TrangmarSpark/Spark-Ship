# Spark-Ship Main Entry Point
from controls import listen_for_voice

if __name__ == "__main__":
    print("=== Spark-Ship Hybrid Control System Starting ===")
    print("Offline voice mode: ON")
    print("Physical controls: ON")
    print("Touchscreen option: ready")
    listen_for_voice()  # This will run the voice loop
