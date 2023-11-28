#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    chars = [".", "?", ":"]
    lines = []
    current_line = ""
    
    for char in text:
        current_line += char
        
        if char in chars:
            lines.append(current_line.strip())
            current_line = ""
    
    lines.append(current_line.strip())
    
    for line in lines:
        print(line)
        print()
