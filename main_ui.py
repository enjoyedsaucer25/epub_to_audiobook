import os
import argparse

from audiobook_generator.config.ui_config import UiConfig
from audiobook_generator.ui.web_ui import host_ui


def handle_args():
    parser = argparse.ArgumentParser(description="WebUI for Epub to Audiobook convertor")
    
    # Read from environment or default to localhost
    port = int(os.environ.get("PORT", 7860))
    host = os.environ.get("HOST", "0.0.0.0")

    parser.add_argument("--host", default=host, help="Host address")
    parser.add_argument("--port", default=port, type=int, help="Port number")

    ui_args = parser.parse_args()
    return UiConfig(ui_args)

def main():
    config = handle_args()
    host_ui(config)

if __name__ == "__main__":
    main()


