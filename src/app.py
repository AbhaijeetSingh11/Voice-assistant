"""
Entry point for the Voice Assistant CLI or web app.
"""
import argparse

def main():
    parser = argparse.ArgumentParser(description="Voice Assistant CLI")
    parser.add_argument("--mode", choices=["cli","web"], default="cli")
    args = parser.parse_args()

    if args.mode == "cli":
        print("Starting CLI prototype...")
        # TODO: hook up ASR -> NLU -> TTS pipeline
    else:
        print("Starting web app (Flask/Streamlit)...")
        # TODO: launch web server

if __name__ == "__main__":
    main()