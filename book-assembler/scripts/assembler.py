import os
import json

def assemble_book(fragments_dir, output_file):
    if not os.path.exists(fragments_dir):
        print(f"Erro: Diretorio {fragments_dir} não encontrado.")
        return

    # Listar e ordenar fragmentos
    files = sorted([f for f in os.listdir(fragments_dir) if f.endswith('.txt') and f.startswith('fragment_')])
    
    full_text = ""
    for filename in files:
        file_path = os.path.join(fragments_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            full_text += content + "\n\n"
            
        # Tentar integrar infográficos se houver arquivo de proposta
        proposal_path = file_path.replace('.txt', '_infographic.json')
        if os.path.exists(proposal_path):
            with open(proposal_path, 'r', encoding='utf-8') as f:
                proposal = json.load(f)
                full_text += f"\n> [INSERIR INFOGRÁFICO: {proposal['type']} - {proposal['description']}]\n\n"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_text.strip())
        
    print(f"Livro montado com sucesso em {output_file}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Uso: python assembler.py <diretorio_fragmentos> <arquivo_saida>")
    else:
        assemble_book(sys.argv[1], sys.argv[2])
