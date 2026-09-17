import json
import re
from difflib import SequenceMatcher


class CustomerSupportBot:
    """Simple, explainable customer-support chatbot using a local knowledge base."""

    def __init__(self, knowledge_base_path: str):
        with open(knowledge_base_path, "r", encoding="utf-8") as file:
            self.knowledge_base = json.load(file)

    @staticmethod
    def _normalize(text: str) -> str:
        return re.sub(r"[^a-z0-9 ]", " ", text.lower()).strip()

    def get_response(self, message: str) -> dict:
        clean_message = self._normalize(message)
        best_item = None
        best_score = 0.0

        for item in self.knowledge_base:
            for question in item.get("questions", []):
                score = SequenceMatcher(None, clean_message, self._normalize(question)).ratio()
                if score > best_score:
                    best_score = score
                    best_item = item

        if best_item and best_score >= 0.38:
            return {
                "reply": best_item["answer"],
                "category": best_item.get("category", "General"),
                "confidence": round(best_score, 2),
            }

        return {
            "reply": "I'm not completely sure about that. Please contact our support team for further assistance.",
            "category": "Fallback",
            "confidence": round(best_score, 2),
        }
