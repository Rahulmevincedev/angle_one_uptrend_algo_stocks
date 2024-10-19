# Modules Installation Readme

## Setting Up a Python Project with Virtual Environment

### 1. Create a Virtual Environment
To create a virtual environment, run the following command in your project directory:
```bash
python -m venv .venv
```
Replace `myenv` with your desired environment name.

### 2. Activate the Virtual Environment
- **For PowerShell**:
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
- **For Command Prompt**:
  ```cmd
  .venv\Scripts\activate
  ```

### 3. Install Required Packages
Once the virtual environment is activated, you can install packages using `pip`. For example:
```bash
pip install <package_name>
```
To install multiple packages at once:
```bash
pip install requests numpy pandas
```

### 4. Create or Update `requirements.txt`
To keep track of your installed packages, create or update the `requirements.txt` file:
```bash
pip freeze > requirements.txt
```

### 5. Transferring the Project
When moving your project to a different system:
- Copy the entire project folder, including the `requirements.txt` file.

### 6. Set Up on the New System
On the new system, follow these steps:
- Create a new virtual environment:
  ```bash
  python -m venv .venv
  ```
- Activate the virtual environment:
  - **For PowerShell**:
    ```powershell
    .venv\Scripts\Activate.ps1
    ```
  - **For Command Prompt**:
    ```cmd
    .venv\Scripts\activate
    ```
- Install the required packages:
```bash
pip install -r requirements.txt
```

### 7. Handling Execution Policy in PowerShell
If you encounter an error regarding script execution policies, you can change the policy by running PowerShell as an administrator and executing:
```powershell
Set-ExecutionPolicy RemoteSigned
```
To revert to the default setting after activation, run:
```powershell
Set-ExecutionPolicy Restricted
```

### Summary
- Always activate your virtual environment before installing new packages.
- Use `pip install <package_name>` to add new libraries.
- Update your `requirements.txt` file to reflect any changes in your dependencies.

This guide will help you manage your Python project dependencies effectively and ensure a smooth transition between different systems.
