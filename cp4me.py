import subprocess
import os
import argparse


def cp4me(container_id, path_file, path_destiny):
    try:
        if not os.path.isfile(path_file):
            print(f"Error: File {path_file} not found")
            return
        
        command = ["docker", "cp", path_file, f"{container_id}:{path_destiny}"]

        subprocess.run(command, check=True)
        print(f"File {path_file} send for container {container_id} em {path_destiny} with success")

    except subprocess.CalledProcessError as e:
        print(f"Error to send file")
    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="send file container docker")
    parser.add_argument('container_id', type=str, help='ID container Docker')
    parser.add_argument('path_file', type=str, help="path file send")
    parser.add_argument('path_destiny', type=str, help="path destiny container")

    args = parser.parse_args()

    cp4me(args.container_id, args.path_file, args.path_destiny)

if __name__ == "__main__":
    main()