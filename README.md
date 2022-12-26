# robin

Simple Genius lyrics scraper.
Running as console script:
```bash
# 452 is an example genius song ID
python3 service.py 452 -cm
```
Running as one-endpoint flask api:
```bash
# Create python3 venv
python3 -m venv venv
# Activate venv
source venv/bin/activate
# Install dependencies
pip3 install -r requirements.txt
# Copy .env.example to .env file
cp .env-example .env
# Fill API_KEY value in .env with some long random string, e.g. afc5212c-116f-4987-917a-e9332fb25e29
# Now, when requesting flask server for lyrics, X-Api-Key header with value afc5212c-116f-4987-917a-e9332fb25e29
# must be present on http request.
# You can test it with curl request script:
chmod +x ./scripts/test_request.sh
./scripts/test_request.sh
```
