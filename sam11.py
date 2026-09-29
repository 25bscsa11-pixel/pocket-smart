# Main entry point
if __name__ == "__main__":
    import uvicorn

    print("Starting PocketSmart: AI Budget Planner...")
    uvicorn.run(app, host="0.0.0.0", port=8000)