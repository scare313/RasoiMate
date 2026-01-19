from fastapi import APIRouter
from app.services.engine import RecommendationEngine

router = APIRouter()

@router.get("/deck")
async def get_daily_deck():
    # In a real app, we fetch user info from DB/Auth
    # Mocking user context:
    user_inventory = ["potato", "lentils", "onion"] 
    is_user_veg = True
    
    deck = RecommendationEngine.generate_deck(user_id=1, user_inventory=user_inventory, is_veg=is_user_veg)
    
    return {
        "status": "success",
        "count": len(deck),
        "data": deck
    }

@router.post("/swipe")
async def record_swipe(recipe_id: int, action: str):
    # Here we would save to Postgres 'Interaction' table
    return {"status": "recorded", "action": action, "recipe_id": recipe_id}