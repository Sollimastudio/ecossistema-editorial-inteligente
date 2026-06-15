import json
import os

def suggest_infographics(fragment_text, context_map):
    suggestions = []
    
    # Lógica simplificada de detecção de densidade informacional
    if len(fragment_text.split()) > 500:
        suggestions.append({
            "type": "Resumo Visual",
            "reason": "Alta densidade de palavras no fragmento.",
            "description": "Um diagrama de blocos conectando os principais conceitos discutidos."
        })
        
    if "data" in fragment_text.lower() or "ano" in fragment_text.lower():
        suggestions.append({
            "type": "Linha do Tempo",
            "reason": "Menção a datas ou sequências temporais.",
            "description": "Uma linha do tempo horizontal marcando os eventos críticos descritos."
        })

    return suggestions

if __name__ == "__main__":
    # Exemplo de uso
    text = "Em 1990, os eventos começaram a se desenrolar..."
    context = {"id": "fragment_001"}
    print(json.dumps(suggest_infographics(text, context), indent=2, ensure_ascii=False))
