from src.app import create_app  # Cambiar la importación para evitar confusión con `app`

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
