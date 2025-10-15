from app import create_app
from app.extensions import db   
from flask import send_from_directory

app = create_app()
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory("uploads", filename)

if __name__ == "__main__":
    app.run(debug=True)
    

