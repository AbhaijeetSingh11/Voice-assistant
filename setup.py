from setuptools import setup, find_packages

setup(
    name="voice_assistant",
    version="0.1.0",
    author="Abhaijeet Singh",
    author_email="asingh37_be22@thapar.edu",
    description="End-to-end voice assistant with ASR, NLU, and TTS",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AbhaijeetSingh11/Voice-assistant.git",
    license="MIT",
    python_requires=">=3.8",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.0.0",
        "datasets>=2.0.0",
        "speechrecognition>=3.8.1",
        "flask>=2.0.0",
        "pydantic>=1.10.0",
        "pyyaml>=6.0"
    ],
    entry_points={
        "console_scripts": [
            "voice-assistant=app:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
)
