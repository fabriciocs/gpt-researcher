import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from examples.permchain_agents.researcher import Researcher
from examples.permchain_agents.editor_actors.editor import EditorActor
from examples.permchain_agents.reviser_actors.reviser import ReviserActor
from examples.permchain_agents.search_actors.gpt_researcher import GPTResearcherActor
from examples.permchain_agents.writer_actors.writer import WriterActor
from examples.permchain_agents.research_team import ResearchTeam
from scraping.processing.text import md_to_pdf

if __name__ == '__main__':
    output_path = "./output"
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    query = sys.argv[1]
    researcher = Researcher(GPTResearcherActor(), WriterActor())
    research_team = ResearchTeam(researcher, EditorActor(), ReviserActor())

    draft = research_team.run(query)
    with open(f"{output_path}/query.md", "w") as f:
        f.write(draft)
    md_to_pdf(f"{output_path}/query.md", f"{output_path}/query.pdf")
