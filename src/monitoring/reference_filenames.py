from pathlib import Path
from typing import List

from icecream import ic  # For debugging purposes


def main() -> None:
    """
    Entry point of the program. Configures paths and calls the file listing function.
    """
    folder_path: str = (
        "C:\\Users\\ps.public.PS-LT022-813B\\Desktop\\ouput INVOICE 202408"
    )
    save_dir: str = "C:\\Users\\ps.public.PS-LT022-813B\\Desktop"
    output_filename: str = "filenames invoice Aug 2024.txt"

    generate_file_list(folder_path, save_dir, output_filename)


def generate_file_list(folder_path: str, save_dir: str, output_filename: str) -> None:
    """
    Lists all files in the specified folder and writes their names to a text file.

    Args:
        folder_path (str): The path to the folder containing the files.
        save_dir (str): The directory where the output file will be saved.
        output_filename (str): The name of the output file to write the file names to.

    Returns:
        None
    """
    try:
        # Convert paths to Path objects
        folder = Path(folder_path)
        save_directory = Path(save_dir)

        # Validate the folder path
        if not folder.is_dir():
            ic("Error: The provided path is not a valid directory.")
            return

        # Get the list of files in the folder
        file_names: List[str] = get_file_names(folder)

        # Ensure the save directory exists
        save_directory.mkdir(parents=True, exist_ok=True)

        # Write the file names to the output file
        output_file = save_directory / output_filename
        write_to_file(output_file, file_names)

        ic(f"File list successfully saved to {output_file}")
    except Exception as error:
        ic(f"An error occurred: {error}")


def get_file_names(folder: Path) -> List[str]:
    """
    Retrieves the names of all files in the specified folder, removing the '.pdf' extension if present.

    Args:
        folder (Path): The path to the folder.

    Returns:
        List[str]: A list of file names without the '.pdf' extension in the folder.
    """
    return [
        file.stem if file.suffix == ".pdf" else file.name
        for file in folder.iterdir()
        if file.is_file()
    ]


def write_to_file(output_file: Path, file_names: List[str]) -> None:
    """
    Writes the list of file names to the specified output file.

    Args:
        output_file (Path): The path to the output file.
        file_names (List[str]): The list of file names to write.

    Returns:
        None
    """
    with open(output_file, "w", encoding="utf-8") as file:
        for file_name in file_names:
            file.write(f"{file_name}\n")


if __name__ == "__main__":
    main()
