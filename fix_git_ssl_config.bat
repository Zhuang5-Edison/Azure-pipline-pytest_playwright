@echo off
REM Git SSL Configuration Fix Script for Azure DevOps Self-hosted Agent

REM Set Git to use Windows certificate store
git config --system http.sslBackend schannel

REM Enable SSL verification
git config --system http.sslVerify true

REM Display current Git SSL configuration
echo.
echo === Git SSL Configuration ===
git config --list --show-origin | findstr ssl
