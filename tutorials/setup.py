import cx_Freeze #https://cx-freeze.readthedocs.io/en/latest/

executables = [cx_Freeze.Executable("idle-tutorial4041.py")]

cx_Freeze.setup(
    name="Slither",
    options={"build_exe":{"packages":["pygame"],
    "include_files":["./extras/apple_img.png",
    "./extras/icon.png",
    "./extras/snake_head.png"]}},
    description= "Slither Game Tutorial - ync",
    executables=executables
    )

#run python3 setup.py build
#windows = python setup.py bdist_msi = create an installer
