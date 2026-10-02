import json
import os

def parse_blueprint(input_path, output_path):
    with open(input_path, 'r') as f:
        data = json.load(f)

    markdown_content = f"# {data['system_name']} - Blueprint Model\n\n"
    markdown_content += "## System Components\n"
    for comp in data['components']:
        markdown_content += f"- **{comp['name']}** ({comp['type']}): {comp['purpose']}\n"

    markdown_content += "\n## Key Trade-offs\n"
    for t in data['trade_offs']:
        markdown_content += f"- **{t['priority']}**: {t['choice']}\n"

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(markdown_content)

    print(f"Successfully generated {output_path}")

if __name__ == "__main__":
    parse_blueprint("data/mosaic_blueprint.json", "docs/mosaic_architecture.md")
