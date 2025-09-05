import time
import sys
import subprocess

def read_and_execute_with_delay(filename, delay=2):
    try:
        with open(filename, "r") as file:
            for line in file:
                command = line.strip()
                if not command:
                    continue  # skip empty lines

                print(f"\nExecuting: {command}")
                try:
                    # Run command, suppress curl progress meter
                    result = subprocess.run(
                        command,
                        shell=True,
                        text=True,
                        capture_output=True
                    )

                    # Show only stdout
                    if result.stdout.strip():
                        print(result.stdout.strip())

                    # Show curl errors only (e.g., failed requests)
                    if result.stderr.strip() and "curl:" in result.stderr:
                        print(f"Error: {result.stderr.strip()}")

                except Exception as e:
                    print(f"Failed to run command: {e}")

                time.sleep(delay)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename> [delay_seconds]")
        sys.exit(1)

    filename = sys.argv[1]
    delay = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    read_and_execute_with_delay(filename, delay)
