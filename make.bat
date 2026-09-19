@ECHO OFF

pushd %~dp0

if "%SPHINXBUILD%" == "" (
    set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=source
set BUILDDIR=build

if "%1" == "" goto help

%SPHINXBUILD% -b %1 %SOURCEDIR% %BUILDDIR%\%1
goto end

:help
echo Usage: make.bat ^<builder^>
echo.
echo Example:
echo   make.bat html

:end
popd