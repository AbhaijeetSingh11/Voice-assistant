from setuptools import setup, find_packages

setup(
    name="voice_assistant",
    version="0.1.0",
    author="Your Name",
    description="End-to-end voice assistant with ASR, NLU, and TTS",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # kept in sync with requirements.txt
    ],
    entry_points={
        'console_scripts': [
            'voice-assistant=app:main',
        ],
    },
)