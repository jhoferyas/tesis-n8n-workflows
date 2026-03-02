import json
import sys
from pathlib import Path

WORKFLOWS_DIR = Path("Flujo/workflows")

REQUIRED_TOP_KEYS = ["name", "nodes", "connections"]

def fail(msg: str):
    print(f"❌ {msg}")
    sys.exit(1)

def main():
    if not WORKFLOWS_DIR.exists():
        fail(f"No existe la carpeta: {WORKFLOWS_DIR} (verifica la ruta)")

    files = sorted(WORKFLOWS_DIR.glob("*.json"))
    if not files:
        fail(f"No se encontraron archivos .json en {WORKFLOWS_DIR}")

    errors = 0
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"❌ JSON inválido: {f.name} -> {e}")
            errors += 1
            continue

        missing = [k for k in REQUIRED_TOP_KEYS if k not in data]
        if missing:
            print(f"❌ {f.name}: faltan claves {missing}")
            errors += 1
            continue

        if not isinstance(data["nodes"], list) or len(data["nodes"]) == 0:
            print(f"❌ {f.name}: 'nodes' debe ser lista y no vacía")
            errors += 1

        if not isinstance(data["connections"], dict):
            print(f"❌ {f.name}: 'connections' debe ser objeto/dict")
            errors += 1

    if errors:
        fail(f"Validación falló: {errors} archivo(s) con problemas.")
    print(f"✅ Validación OK: {len(files)} workflows revisados.")

if __name__ == "__main__":
    main()