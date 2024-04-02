import os
import json
from pathlib import Path
import platform

print()
print(f'Current OS: {platform.system()}')
print()

# Create project folder
project_name = input("Project Name: ")

# Client
Path(f'./{project_name}').mkdir()
os.chdir(Path(f"./{project_name}"))
os.system("npm create vite@latest client -- --template react")
os.chdir(Path("./client"))
os.system("npm install")
os.system("npm install axios react-router-dom")
os.chdir(Path("./src"))
os.system("mkdir components views")
os.chdir(Path("../.."))

# Server
Path('./server').mkdir()
Path('./server/server.js').touch()
Path('./.gitignore').touch()

# Run npm commands to initialize the server file
os.chdir(Path("./server"))
os.system("npm init -y")
os.system("npm install mongoose express dotenv cors")
os.system("npm install --save-dev nodemon")

os.system("mkdir config controllers models routes")

Path("./config/mongoose.config.js").touch()
Path("./.env").touch()

# Add the necessary boilerplate for the package.json
with open(Path("./package.json"), "r") as package:
    data = json.load(package)
data["type"] = "module"
data["scripts"]["dev"] = "npx nodemon"
with open(Path("./package.json"), "w") as package:
    json.dump(data, package)

# Add the boilerplate inside the mongoose.config.js
with open(Path("./config/mongoose.config.js"), "w") as mongoose:
    mongoose.writelines([
        "import { connect } from 'mongoose';\n",
        "import dotenv from 'dotenv';\n",
        "dotenv.config()\n",
        "const MONGODB_URI = process.env.MONGODB_URI;\n",
        "async function dbConnect() {\n",
        "  try {\n",
        "    await connect(MONGODB_URI, {\n",
        "    dbName: 'booksDB', //Make sure to change this here\n",
        "    });\n",
        "    console.log('Pinged your deployment. You successfully connected to MongoDB!');\n",
        "  } catch (error) {\n",
        "    console.log(error);\n",
        "    throw error;\n",
        "  }\n",
        "}\n",
        "export default dbConnect\n"])

# Add the boilerplate inside the server.js
with open(Path("./server.js"), "w") as server:
    server.write("import express from 'express';\n")
    server.write("import cors from 'cors';\n")
    server.write("import dotenv from 'dotenv';\n")
    server.write("import dbConnect from './config/mongoose.config.js';\n")
    server.write("const app = express();\n")
    server.write("app.use(express.json(), cors());\n")
    server.write("dotenv.config();\n")
    server.write("const PORT = process.env.PORT;\n")
    server.write("dbConnect();\n")
    server.write(
        "app.listen(PORT, console.log(`Listening on port: ${PORT}`)) \n")

# Add .env boilerplate
with open(Path("./.env"), "w") as environment:
    environment.write("PORT=8000")
    environment.write("MONGODB_URI=<add your link here>")
