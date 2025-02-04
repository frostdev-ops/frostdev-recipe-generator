import tkinter as tk
from tkinter import messagebox

class RecipeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Crafting Recipe Generator")

        self.grid_entries = [[None for _ in range(3)] for _ in range(3)]
        self.create_grid()

        self.output_label = tk.Label(root, text="Output Item:")
        self.output_label.grid(row=3, column=0, pady=10)
        self.output_entry = tk.Entry(root)
        self.output_entry.grid(row=3, column=1, pady=10)

        self.quantity_label = tk.Label(root, text="Quantity:")
        self.quantity_label.grid(row=3, column=2, pady=10)
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.grid(row=3, column=3, pady=10)

        self.generate_button = tk.Button(root, text="Generate Recipe", command=self.generate_recipe)
        self.generate_button.grid(row=4, column=0, columnspan=4, pady=10)

    def create_grid(self):
        for i in range(3):
            for j in range(3):
                self.grid_entries[i][j] = tk.Entry(self.root)
                self.grid_entries[i][j].grid(row=i, column=j, padx=(5, 0), pady=(5, 0))

    def generate_recipe(self):
        grid = [[self.grid_entries[i][j].get() for j in range(3)] for i in range(3)]
        output_item = self.output_entry.get()
        quantity = self.quantity_entry.get()

        if not output_item:
            messagebox.showerror("Error", "Output item cannot be empty")
            return

        if not quantity.isdigit() or int(quantity) <= 0:
            messagebox.showerror("Error", "Quantity must be a positive integer")
            return

        if not (output_item.startswith('<item:') and output_item.endswith('>')):
            output_item = f'<item:{output_item}>'
        item_name = output_item.split(":")[-1].strip('>')
        item_name = item_name.replace("_", "")
        recipe = f'craftingTable.addShaped("{item_name}", {output_item} * {quantity}, [\n'
        for row in grid:
            recipe += '[' + ', '.join([item if item.startswith('<item:') and item.endswith('>') else f'<item:{item}>' if item else '<item:minecraft:air>' for item in row]) + '],\n'
        recipe = recipe.rstrip(',\n') + '\n]);\n'

        # Strip <item: and > from the output item for the filename
        output_file = output_item.split(":")[-1].strip('>')
        filename = f"{output_file}.zs"
        with open(filename, "w") as file:
            file.write(recipe)

        messagebox.showinfo("Success", f"Recipe generated and saved to {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeGenerator(root)
    root.mainloop()