# Copilot Instructions for escenario_8_zalando

## Project Overview
This project is a Streamlit web app for classifying Zalando fashion images using a Keras model. The app is containerized with Docker and uses TensorFlow and NumPy as core dependencies.

## Architecture & Data Flow
- **streamlit_app.py**: Main entry point. Handles UI, image upload, preprocessing, and model inference.
- **Model**: Expects a Keras model file named `zalando.keras` in the project root (not present in the current workspace snapshot; ensure it is available for inference).
- **Image Preprocessing**: Uploaded images are converted to grayscale, inverted, resized to 28x28, and autocontrasted before prediction.
- **Classes**: Hardcoded in the app as a list of 10 clothing categories.

## Developer Workflows
- **Run Locally (Docker)**:
  - Build and start: `docker-compose up --build`
  - The app will be available at [http://localhost:8501](http://localhost:8501)
- **Dependencies**: Managed via `requirements.txt`. Update this file and rebuild the Docker image to add packages.
- **Model Updates**: Replace `zalando.keras` in the root to update the model.

## Project Conventions
- All code is in `streamlit_app.py`.
- Model and mapping files are expected in the root or `model/` directory.
- Only image files (`jpg`, `jpeg`, `png`) are accepted for upload.
- No explicit test suite or CI/CD is present.

## Integration Points
- **TensorFlow/Keras**: For model loading and inference.
- **Streamlit**: For the web UI and file upload.
- **Docker**: For reproducible deployment. See `Dockerfile` and `docker-compose.yml` for build/run details.

## Examples
- To add a new class, update the `classes` list in `streamlit_app.py` and retrain the model accordingly.
- To change preprocessing, modify the image pipeline in `streamlit_app.py`.

## Key Files
- `streamlit_app.py`: Main app logic
- `Dockerfile`, `docker-compose.yml`: Containerization
- `requirements.txt`: Python dependencies
- `model/`: (Optional) Store additional model artifacts

---
For questions about model format, preprocessing, or deployment, check the above files for current conventions.
