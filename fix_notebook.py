import nbformat

NOTEBOOK = "Stuttering_Whisper.ipynb"   # 🔴 change this to your notebook name

nb = nbformat.read(NOTEBOOK, as_version=4)

# Remove broken widget metadata
nb.metadata.pop("widgets", None)

# Save fixed notebook
nbformat.write(nb, "your_notebook_FIXED.ipynb")

print("✅ Notebook fixed successfully")
