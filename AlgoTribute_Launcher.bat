@echo off
title AlgoTribute Suite Launcher
color 0A

echo =======================================================
echo             ALGO TRIBUTE - SUITE FINANCE
echo =======================================================
echo.

REM --- CHECK PYTHON VERSION 3.10 ---
py -3.10 --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo [ERREUR] Python 3.10 introuvable.
    echo Installe Python 3.10 pour utiliser cette suite.
    pause
    exit /b
)

echo Python 3.10 detecte.
echo.

REM --- INSTALLATION DES DEPENDANCES ---
echo Installation / verification des dependances...
py -3.10 -m pip install --upgrade pip >nul
py -3.10 -m pip install yfinance numpy pandas matplotlib fpdf >nul

echo Dependances OK.
echo.

:MENU
cls
echo =======================================================
echo                   ALGO TRIBUTE - MENU
echo =======================================================
echo.
echo 1. Lancer Fundamental Analyzer
echo 2. Lancer Portfolio Optimizer
echo 3. Lancer Screener
echo 4. Lancer Stress Test
echo ---------------------------------------
echo 0. Quitter
echo =======================================================
echo.

set /p choix="Votre choix : "

if "%choix%"=="1" goto FUND
if "%choix%"=="2" goto PORT
if "%choix%"=="3" goto SCREEN
if "%choix%"=="4" goto STRESS
if "%choix%"=="0" goto END

echo Choix invalide.
pause
goto MENU

:FUND
echo Lancement de AlgoTribute_FundamentalAnalyzer.py...
py -3.10 AlgoTribute_FundamentalAnalyzer.py
pause
goto MENU

:PORT
echo Lancement de AlgoTribute_PortfolioOptimizer.py...
py -3.10 AlgoTribute_PortfolioOptimizer.py
pause
goto MENU

:SCREEN
echo Lancement de AlgoTribute_Screener.py...
py -3.10 AlgoTribute_Screener.py
pause
goto MENU

:STRESS
echo Lancement de AlgoTribute_StressTest.py...
py -3.10 AlgoTribute_StressTest.py
pause
goto MENU

:END
echo Fermeture du programme...
timeout /t 1 >nul
exit /b
