from typing import Union


def foldername(extension: str) -> Union[str, None]:
    """Returns the folder name based on the file extension."""
    return {
        # Audio file extensions.
        'midi': 'musics',
        'mp3': 'musics',
        'wav': 'musics',

        # Image file extensions.
        'png': 'images',
        'jpeg': 'images',
        'jpg': 'images',
        'raw': 'images',
        'gif': 'images',
        'bmp': 'images',
        'svg': 'images',
        'ico': 'images',

        # Video file extensions.
        'avi': 'videos',
        'm4v': 'videos',
        'mkv': 'videos',
        'mp4': 'videos',

        # Programming file extensions.
        'c': 'c_programs',
        'cpp': 'cpp_programs',
        'java': 'java_programs',
        'class': 'java_programs',
        'js': 'js_files',
        'py': 'python_files',
        'swift': 'swift_programs',
        'php': 'php_files',

        # Compressed file extensions.
        '7z': 'compressed_files',
        'deb': 'compressed_files',
        'pkg': 'compressed_files',
        'rar': 'compressed_files',
        'rpm': 'compressed_files',
        'z': 'compressed_files',
        'zip': 'compressed_files',

        # Disc image file extensions.
        'iso': 'disc_images',
        'vcd': 'disc_images',

        # Data file extensions.
        'csv': 'data_files',
        'json': 'data_files',
        'xml': 'data_files',
        'dat': 'data_files',
        'db': 'data_files',
        'log': 'data_files',
        'sql': 'data_files',
        'tar': 'data_files',

        # Software file extensions.
        'apk': 'software',
        'exe': 'software',

        # Others.
        'txt': 'text_notes',
        'pdf': 'pdf_files',
        'xlsx': 'excel_files',
        'xls': 'excel_files',
        'ppt': 'ppt_files',
        'doc': 'documents',
        'htm': 'html_files',
        'html': 'html_files',
        'css': 'css_styles',
    }.get(extension, 'extras')
