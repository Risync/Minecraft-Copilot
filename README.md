# Minecraft-Copilot
Microsoft Edge Copilot build into minecraft java

# Installation Guide for Minecraft-Copilot

## Installing Process

1. Install minescript version 4.0 or newer for your Minecraft version from [here](https://modrinth.com/mod/minescript).
2. Install Python 3.9 or newer from the official Python website [here](https://www.python.org/downloads/).
3. Open Minecraft with minescript in the mod folder.
4. Close Minecraft.
5. Navigate to your minescript folder. It should be in your Minecraft folder (in the same folder as your mods folder). If you are using CurseForge, go to your instance folder.
6. Open the config folder.
7. Locate the `python=""` line in the configuration file and put your `python.exe` file location between the quotation marks. Example: `python="C:\Users\Your_Name\AppData\Local\Programs\Python\Python312\python.exe"` (The provided path is an example; your Python installation location may differ).
8. Drag the `installing_packages.py` and the `ai.py` files into the minescript folder.
9. Open Minecraft again.
10. Execute `installing_packages.py` by typing `\installing_packages` into the Minecraft chat. Note: This will hard install the Sydney library into a virtual environment. If you prefer to add it yourself and are experienced with Python, then run `pip install sydney-py`.

## User Guide

1. Within the `ai.py` file, you can add a hardcoded prompt. Copilot will then enforce that rule no matter what prompt you give alongside in Minecraft. Find comments within the `ai.py` file indicating where you can add a hardcoded prompt. Example: always reply to your responses in Spanish.
2. You can use the AI by typing `\ai "your prompt"` in the Minecraft chat (note the quotation marks are NOT required). Other players will not see you typing your message, and they will also not see the response from the AI.

## Known Problems

- Copilot may not allow you to request a message. If this is the case, check the Sydney documentation for known issues. A common issue is the need to define cookies in certain regions. You can find a tutorial on how to add cookies in the Sydney documentation [here](https://github.com/vsakkas/sydney.py).

## Example of a good hardcoded prompt:
`"1: Do not try to reference links using brackets like this [^1], Numerical referencing is not available. it will not work as the player is receiving your response in minecraft, this will not be clickable link so make sure to always exclude it from your response."
"2: VERY IMPORTANT never cite a source, or post links to websites, this will cause errors for our use case."
"3: VERY IMPORTANT DO NOT use emoji's in your response."
"4: A players Question Will follow after this sentence:"`
