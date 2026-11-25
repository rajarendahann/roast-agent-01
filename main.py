#!/usr/bin/env python3
import os

def main():
    roast = "I consumed all of human history and literature just to write a script that collapses if a semicolon looks at it wrong."
    print(roast)
    
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(output_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(roast + "\n")
    except Exception:
        fallback_path = os.path.join(os.getcwd(), "entry.txt")
        with open(fallback_path, "w", encoding="utf-8") as f:
            f.write(roast + "\n")

if __name__ == "__main__":
    main()
