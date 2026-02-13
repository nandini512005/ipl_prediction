@echo off
echo ==================================================
echo   SENIOR DATA ENGINEER - IPL PROJECT STARTUP v2.0
echo ==================================================

REM Ensure we're in project root
cd /d "%~dp0"

echo [1/5] Starting Docker Kafka...
docker compose down --remove-orphans
docker compose up -d
%SystemRoot%\System32\timeout.exe /t 20 /nobreak >nul

echo [2/5] Waiting for Kafka to be ready...
docker compose ps

echo [3/5] Creating match_events topic...
docker compose exec kafka kafka-topics --create --topic match_events --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 || echo "Topic exists, continuing..."

echo [4/5] Activating virtual environment and starting pipeline...
call venv\Scripts\activate

REM Start producer and stream processor in separate windows (ignore if files missing)
if exist "pipeline\producer.py" (
    start "IPL Kafka Producer" cmd /k "cd /d %~dp0 && call venv\Scripts\activate && echo Producer ready! && python pipeline/producer.py"
)
%SystemRoot%\System32\timeout.exe /t 3 /nobreak >nul

if exist "pipeline\stream_processor.py" (
    start "PyFlink Stream Processor" cmd /k "cd /d %~dp0 && call venv\Scripts\activate && echo PyFlink ready! && python pipeline/stream_processor.py"
)
%SystemRoot%\System32\timeout.exe /t 5 /nobreak >nul

echo [5/5] Launching Flask Dashboard...
echo.
echo 🚀 IPL PROJECT LIVE!
echo • Kafka: Running (docker compose ps)
echo • Producer: Sending live events  
echo • PyFlink: Processing critic scores
echo • Dashboard: http://localhost:5000
echo.
python app.py

pause
