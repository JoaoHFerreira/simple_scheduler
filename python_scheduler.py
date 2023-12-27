import subprocess
import os

def run_program(language, file_path):
    match language:
        case "go":
            subprocess.run([file_path])
        case "python":
            subprocess.run(["python", file_path])

if __name__ == "__main__":
    programs = [
        ("go", f"{os.getcwd()}/golang/hello"),
        ("python", f"{os.getcwd()}/python/hello.py"),
    ]

    for language, file_path in programs:
        run_program(language, file_path)
