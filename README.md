# DescargarVideos
This a repository where you can find code to be able to download videos from YT or other platforms.

# STEPS WALKED TO CREATE THIS CODE
# 1.- Creating a virtual environment in your project
    virtualenv -p python3 env

# 2.- To activate the virtual environment
    ./env/Scripts/activate
    
    or
    
    .\env\Scripts\activate

# 3.- To see what libraries we have in our project
    pip list

# 4.- To install the libraries required
    pip install pytube pyinstaller 

# 5.- To create a folder where we'll have our proyect (This is already done, the folder is called "src")
    mkdir src

# 6.- To initilize the project (You must be into the project)
    python ./src/nombre_de_tu_script.py
    
    or
    
    python .\src\nombre_de_tu_script.py

# 7.- To be able to create an executable do this one:
    pyinstaller --onefile nombre_de_tu_script.py

    Once the build process is complete, you can find the executable file in the dist folder. To run it, simply double-click the .exe file and your application will open in Windows     without needing to have Python installed.

- If you want to leave from your virtual environment, you must do:
    
    nombre_del_entorno/Scripts/deactivate

    or

    nombre_del_entorno\Scripts\deactivate



