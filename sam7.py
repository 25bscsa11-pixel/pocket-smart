active_sessions[current_user.username].user_data["last_jewelry_budget"] = {
    "timestamp": datetime.utcnow().isoformat(),
    "budget": budget_input.total_budget,
    "occasion": budget_input.occasion,
    "has_image": image is not None
}

# Get recommendations
result = get_jewelry_recommendations(budget_input, image_path)

# Save to history with image info
input_data = budget_input.dict()
if image:
    input_data["image"] = image.filename

save_to_history(
    username=current_user.username,
    recommendation_type="jewelry",
    input_data=input_data,
    result=result
)

return result


@app.get("/recommendation-history")
async def get_recommendation_history(
    request: Request,
    current_user: UserInDB = Depends(get_current_active_user)
):
    """Get the user's recommendation history"""

    if current_user.username not in user_recommendations:
        return {"history": []}

    # Sort history by timestamp (newest first)
    history = sorted(
        user_recommendations[current_user.username],
        key=lambda x: x.timestamp,
        reverse=True
    )

    # Convert to dict for JSON response
    history_data = []
    for item in history:
        history_data.append({
            "id": item.id,
            "timestamp": item.timestamp,
            "type": item.recommendation_type,
            "input": item.input_summary,
            "summary": item.result_summary
        })

    return {"history": history_data}