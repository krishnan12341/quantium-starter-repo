#!/bin/bash

echo "Activating virtual environment..."
. venv/Scripts/activate

echo "Running pytest..."
pytest --maxfail=3 --disable-warnings -q

if [ $? -eq 0 ]; then
    echo "All tests passed!"
    exit 0  
else
    echo "Some tests failed!"
    exit 1  
fi

