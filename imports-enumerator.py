
import pefile
import sys
from pprint import pprint

suspectedFile = sys.argv[1]
PE_HEADER = pefile.PE(suspectedFile)
if hasattr(PE_HEADER, "DIRECTORY_ENTRY_IMPORT"):
    for entry in PE_HEADER.DIRECTORY_ENTRY_IMPORT:
        importList = []
        print("Import Entry:", entry.dll.decode('utf-8'))
        for imp in entry.imports:
            importList.append(imp.name.decode('utf-8'))
        print(importList)
        print()