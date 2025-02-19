from gpt_researcher import GPTResearcher
import asyncio


async def main():
    """
    This is a sample script that shows how to run a research report.
    """
    query = sys.argv[1]

    # Report Type
    report_type = "research_report"

    # Run Research
    researcher = GPTResearcher(query=query, report_type=report_type, config_path=None)
    report = await researcher.run()
    return report


if __name__ == "__main__":
    asyncio.run(main())
