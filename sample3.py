@app.get("/party-planner", response_class=HTMLResponse)
async def party_planner(request: Request, current_user: UserInDB = Depends(get_current_active_user)):
    """Party budget planner page"""
    return templates.TemplateResponse(
        "party_planner.html",
        {"request": request, "user": current_user}
    )


def get_party_recommendations(budget_input: PartyBudgetInput) -> dict:
    """Generate party planning recommendations within budget in INR for Indian market"""
    try:
        response = call_gemini_for_AI_model(
            prompt=f"""
I need party planning recommendations for India with a total budget of
₹{budget_input.total_budget:.2f}.

Party details:
- Type: {budget_input.party_type}
- Number of guests: {budget_input.num_guests}
- Venue type: {budget_input.venue_type or "Not specified"}
- Catering needed: {"Yes" if budget_input.needs_catering else "No"}
- Decoration needed: {"Yes" if budget_input.needs_decoration else "No"}
- Entertainment needed: {"Yes" if budget_input.needs_entertainment else "No"}

Additional requirements: {budget_input.additional_requirements or "None"}

Please provide a detailed budget breakdown with specific recommendations
available in India using INR prices. Use Indian brands, services, and typical
cost expectations.

Format your response as JSON with the following structure:
{{
    "total_budget": {budget_input.total_budget:.2f},
    "budget_breakdown": [
        {{
            "category": "venue",
            "allocation": 0.0,
            "items": [
                {{
                    "name": "",
                    "description": "",
                    "estimated_price": 0.0,
                    "quantity": 1,
                    "search_terms": ""
                }}
            ]
        }}
    ]
}}
"""
        )
        return response
    