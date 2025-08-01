#!/bin/bash

# Activate virtual environment
source venv/Scripts/activate

# Run pytest
pytest test_app.py

# Capture exit code
EXIT_CODE=$?

# Exit with the same code: 0 = success, 1 = failure
if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ All tests passed!"
    exit 0
else
    echo "❌ Some tests failed."
    exit 1
fi
