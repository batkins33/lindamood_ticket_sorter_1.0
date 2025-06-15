import sys
import os
print("PYTHONPATH:", sys.path)
print("DLL Directory:", os.environ.get("PATH", ""))

import sys
print("Running interpreter:", sys.executable)
