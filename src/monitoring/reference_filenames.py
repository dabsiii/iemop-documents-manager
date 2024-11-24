from pathlib import Path

from icecream import ic

"""
This creates a list of the generated invoices used for monitoring
The output of the program is .txt which can then be converted to .csv
"""


def main():
    FOLDER_PATH = "C:\\Users\\ps.public.PS-LT022-813B\\Desktop\\ouput INVOICE 202410"
    SAVE_DIR = "C:\\Users\\ps.public.PS-LT022-813B\\Desktop"
    OUTPUT_FILENAME = "filenames invoice Oct 2024.txt"
    list_files_in_folder(FOLDER_PATH, SAVE_DIR, OUTPUT_FILENAME)


def list_files_in_folder(folder_path: str, save_dir: str, output_filename: str) -> None:
    try:
        folder_path = Path(folder_path)
        save_dir = Path(save_dir)
        if not folder_path.is_dir():
            ic("The provided path is not a valid directory.")
            return
        files = [f.name for f in folder_path.iterdir() if f.is_file()]
        save_dir.mkdir(parents=True, exist_ok=True)
        output_file = save_dir / output_filename
        with open(output_file, "w") as file:
            for f in files:
                file.write(f"{f}\n")
        ic(f"File list saved to {output_file}")
    except Exception as e:
        ic(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
