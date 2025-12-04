# talking-frosty
## Local
```bash
cd talking-frosty
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python src/run_local.py
```
## Pi
```bash
git clone https://github.com/jaebender/talking-frosty.git talking-frosty
cd talking-frosty
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/run_pi.py
```