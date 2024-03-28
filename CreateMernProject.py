import os
import pprint
import json
from pathlib import Path
import platform

print()
print(f'Current OS: {platform.system()}')
print()

# Create project folder with client and server subfolders
project_name = input("Project Name: ")
Path(f'./{project_name}').mkdir()
Path(f'./{project_name}/server').mkdir()
Path(f'./{project_name}/server/server.js').touch()
Path(f'./{project_name}/client').mkdir()
Path(f'./{project_name}/.gitignore').touch()

# Run npm commands to initialize the server file
os.chdir(Path(f"./{project_name}/server"))
os.system("npm init -y")
os.system("npm install mongoose express dotenv cors")
os.system("npm install --save-dev nodemon")

os.system("mkdir config controllers models routes")

Path("./config/mongoose.config.js").touch()
Path("./.env").touch()

# This code will add the necessary boilerplate for the package.json
with open(Path("./package.json"), "r") as package:
    data = json.load(package)

data["type"] = "module"
data["scripts"]["dev"] = "npx nodemon"

with open(Path("./package.json"), "w") as package:
    json.dump(data, package)
