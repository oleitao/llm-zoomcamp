import os
from pathlib import Path

def get_resource_path(relative_path):
    """
    Get absolute path for a resource, handling different running environments
    (local development, Docker container, etc.)
    """
    # Log the current working directory
    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")
    
    # Try direct access from current directory
    if Path(relative_path).exists():
        return str(Path(relative_path).resolve())
    
    # Try from the script's directory
    script_dir = Path(os.path.dirname(os.path.abspath(__file__))).parent
    path = script_dir / relative_path
    if path.exists():
        return str(path)
    
    # Try from Docker /app directory (if we're in a container)
    docker_path = Path('/app') / relative_path
    if docker_path.exists():
        return str(docker_path)
    
    # Special handling for data files
    if 'data/' in relative_path:
        # Try all possible data directory locations
        for data_base in [
            Path('data'),
            Path('/app/data'),
            Path(script_dir) / 'data',
            Path(cwd) / 'data',
        ]:
            data_file = data_base / Path(relative_path).relative_to(Path('data'))
            if data_file.exists():
                return str(data_file)
        
    # Return the original path if all else fails
    print(f"Warning: Could not find {relative_path} in any standard locations")
    return relative_path
