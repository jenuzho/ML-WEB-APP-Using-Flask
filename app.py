from src.app import create_app  # Import the create_app function

# Create the Flask application instance
app = create_app()

if __name__ == "__main__":
    import os
    # Use the PORT provided by Render or default to 5000
    port = int(os.environ.get("PORT", 5000))
    # Run the app on all interfaces
    app.run(host="0.0.0.0", port=port)
