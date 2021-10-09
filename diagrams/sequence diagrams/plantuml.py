from IPython.core.magic import register_cell_magic
from IPython.display import SVG
import subprocess

@register_cell_magic
def plantuml(line, cell):
    """Generate and display a figure using Plantuml.
    """
    with subprocess.Popen(["plantuml", "-Tsvg", "-p"], 
                          stdout=subprocess.PIPE, 
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as proc:
        proc.stdin.write(f"""
            @startuml {line}
            {cell}
            @enduml""")
        proc.stdin.close()
        return SVG(data=proc.stdout.read()) 
