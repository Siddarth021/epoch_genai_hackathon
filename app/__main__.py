import os
from datetime import datetime
from app.agents import run_readme_agent


def main():
    path = input("Enter project folder path: ").strip()

    if not os.path.exists(path):
        print("Invalid path")
        return

    readme = run_readme_agent(path)

    # Create base folder
    base_output_folder = os.path.join(path, "generated_readme")
    os.makedirs(base_output_folder, exist_ok=True)

    # Create timestamped subfolder
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    version_folder = os.path.join(base_output_folder, timestamp)
    os.makedirs(version_folder, exist_ok=True)

    output_path = os.path.join(version_folder, "README.md")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(readme)

    print(f"README generated at: {output_path}")


if __name__ == "__main__":
    main()
