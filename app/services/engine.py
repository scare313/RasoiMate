from typing import List
import random

# Mock Data to simulate Database for V1 MVP Demo
MOCK_RECIPES = [
    {"id": 1, "name": "Aloo Gobi", "ingredients": ["potato", "cauliflower"], "effort": 2, "tags": ["Veg"]},
    {"id": 2, "name": "Butter Chicken", "ingredients": ["chicken", "butter", "tomato"], "effort": 4, "tags": ["Non-Veg"]},
    {"id": 3, "name": "Dal Tadka", "ingredients": ["lentils", "garlic"], "effort": 1, "tags": ["Veg"]},
    {"id": 4, "name": "Paneer Tikka", "ingredients": ["paneer", "yogurt"], "effort": 3, "tags": ["Veg"]},
]

class RecommendationEngine:
    
    @staticmethod
    def calculate_score(recipe, user_inventory):
        score = 50
        
        # Rule 1: Inventory Match
        # If user has an ingredient, add points
        for ingredient in recipe["ingredients"]:
            if ingredient in user_inventory:
                score += 20
        
        # Rule 2: Effort (Simple logic: Lower effort = Higher score for weeknights)
        score -= (recipe["effort"] * 5)
        
        return score

    @staticmethod
    def generate_deck(user_id: int, user_inventory: List[str], is_veg: bool):
        candidates = []
        
        for recipe in MOCK_RECIPES:
            # Hard Filter: Dietary Preference
            if is_veg and "Non-Veg" in recipe["tags"]:
                continue
                
            final_score = RecommendationEngine.calculate_score(recipe, user_inventory)
            
            candidates.append({
                "recipe_id": recipe["id"],
                "name": recipe["name"],
                "score": final_score,
                "match_reason": "Based on your pantry" if final_score > 60 else "Popular today"
            })
            
        # Sort by score descending and return top 5
        candidates.sort(key=lambda x: x["score"], reverse=True)
        return candidates[:5]