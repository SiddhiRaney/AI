from rich import print
from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich.traceback import install
import time

# Enable rich tracebacks
install()

console = Console()

# 1️⃣ Styled text
print("[bold cyan]Rich Demo Application[/bold cyan]")

# 2️⃣ Status spinner
with console.status("[bold green]Loading data..."):
    time.sleep(1.5)

# 3️⃣ Progress bar
for _ in track(range(5), description="Processing tasks..."):
    time.sleep(0.4)

# 4️⃣ Table
table = Table(title="Task Results")
table.add_column("Task", style="magenta")
table.add_column("Status", style="green")

table.add_row("Data Load", "Done")
table.add_row("Processing", "Done")
table.add_row("Validation", "Done")

console.print(table)

# 5️⃣ Pretty traceback
def divide(x, y):
    return x / y

divide(10, 0)
