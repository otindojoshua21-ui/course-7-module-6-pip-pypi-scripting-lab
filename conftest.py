import sys
from pathlib import Path

# Add lib directory to Python path so imports work
lib_path = Path(__file__).parent / "lib"
sys.path.insert(0, str(lib_path))