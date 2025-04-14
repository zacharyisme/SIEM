def build_prompt(summary: str, description: str) -> str:
    return f"""
You are an IT support agent. Classify the following ticket based on its content.
Categories: [Account Issue, Network Issue, System Access, Software Installation, Security Incident, Other]

Ticket:
{summary}
{description}

Output:
"""
