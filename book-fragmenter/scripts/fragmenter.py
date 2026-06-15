import os
import re
import json

def fragment_manuscript(file_path, output_dir):
    if not os.path.exists(file_path):
        print(f"Erro: Arquivo {file_path} não encontrado.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Divisão por capítulos (ex: Capítulo 1, # Capítulo, etc.)
    chapters = re.split(r'(?i)(?=\n(?:Capítulo|Chapter|#)\s+\d+)', content)
    
    fragments = []
    for i, chapter in enumerate(chapters):
        if not chapter.strip():
            continue
            
        fragment_id = f"fragment_{i:03d}"
        fragment_path = os.path.join(output_dir, f"{fragment_id}.txt")
        
        # Gerar Mapa de Contexto simplificado
        context_map = {
            "id": fragment_id,
            "previous_summary": "Resumo do conteúdo anterior (a ser preenchido pela análise semântica)" if i > 0 else "Início do livro",
            "next_preview": "Prévia do próximo conteúdo" if i < len(chapters) - 1 else "Fim do livro",
            "metadata": {
                "chapter_index": i,
                "length": len(chapter)
            }
        }
        
        with open(fragment_path, 'w', encoding='utf-8') as f:
            f.write(chapter.strip())
            
        with open(os.path.join(output_dir, f"{fragment_id}_context.json"), 'w', encoding='utf-8') as f:
            json.dump(context_map, f, indent=4, ensure_ascii=False)
            
        fragments.append(fragment_id)
        print(f"Fragmento {fragment_id} criado.")

    return fragments

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Uso: python fragmenter.py <arquivo_entrada> <diretorio_saida>")
    else:
        fragment_manuscript(sys.argv[1], sys.argv[2])
