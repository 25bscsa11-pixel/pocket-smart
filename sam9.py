# Step 7: Add a new endpoint to serve the history page
@app.get("/history", response_class=HTMLResponse)
async def history_page(
    request: Request,
    current_user: UserInDB = Depends(get_current_active_user)
):
    """History page to view past recommendations"""
    return templates.TemplateResponse(
        "history.html",
        {"request": request, "user": current_user}
    )