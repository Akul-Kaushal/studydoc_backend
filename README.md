# For uv package
`text
    # 1. Clone the repo
    git clone <repo_url>
    cd <repo_folder>

    # 2. Install environment + dependencies
    uv sync

    # 3. Run the project
    uv run <main_script.py>

    # (Optional)
    uv add <package>
    uv remove <package>
    uv tree
    uv add -r requirements.txt
`