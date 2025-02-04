# Frostdev Recipe Generator

Frostdev Recipe Generator is a tool designed to help you create crafting recipes for CraftTweaker. This tool provides a user-friendly interface to generate the necessary scripts for adding custom recipes to your Minecraft modpacks.

## Features

- **Grid-based Input**: Easily input your recipe ingredients using a 3x3 grid.
- **Output Item**: Specify the output item and quantity for your recipe.
- **Error Handling**: Provides error messages for invalid inputs.
- **Script Generation**: Automatically generates the CraftTweaker script for your custom recipe.

## Installation

1. Clone the repository:
    ```sh
    git clone https://gitlab.com/yourusername/wowid-recipe-generator.git
    ```
2. Navigate to the project directory:
    ```sh
    cd wowid-recipe-generator
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python generator.py
    ```
2. Use the grid to input your recipe ingredients.
3. Specify the output item and quantity.
4. Click "Generate Recipe" to create the CraftTweaker script.

## Example

Here is an example of a generated CraftTweaker script:

```zs
craftingTable.addShaped("example_item", <item:example_item> * 1, [
    [<item:ingredient1>, <item:ingredient2>, <item:ingredient3>],
    [<item:ingredient4>, <item:ingredient5>, <item:ingredient6>],
    [<item:ingredient7>, <item:ingredient8>, <item:ingredient9>]
]);
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue on GitLab or contact the project maintainer at your.email@example.com.
## Generating an Executable

To generate an executable (.exe) file for the Wowid Recipe Generator, follow these steps:

1. Ensure you have `pyinstaller` installed:
    ```sh
    pip install pyinstaller
    ```

2. Navigate to the project directory:
    ```sh
    cd wowid-recipe-generator
    ```

3. Run `pyinstaller` to generate the executable:
    ```sh
    pyinstaller --onefile generator.py
    ```

4. The executable will be created in the `dist` directory:
    ```sh
    dist/generator.exe
    ```

You can now distribute the `generator.exe` file to users who can run the Wowid Recipe Generator without needing to install Python or any dependencies.