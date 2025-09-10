Agent-Powered Software Development Team
This project uses the crewAI framework to simulate a complete, autonomous software development team. Given a set of high-level requirements, this multi-agent system will design, implement, test, and create a user interface for a fully functional Python module.

The system is designed to streamline the development process from concept to a demonstrable prototype with minimal human intervention.

🚀 **How It Works**
The project orchestrates a team of four specialized AI agents, each with a distinct role in the software development lifecycle. The process is kicked off by providing a set of requirements, a desired module name, and a class name.

The workflow proceeds as follows:

Design: The Engineering Lead agent receives the high-level requirements and creates a detailed technical design document in Markdown, outlining the necessary classes, methods, and function signatures.

Implementation: The Backend Engineer agent takes the design document and writes the complete, self-contained Python code for the module.

UI Development: The Frontend Engineer agent, a Gradio specialist, develops a simple app.py to provide an interactive web interface for the newly created backend module.

Testing: The Test Engineer agent writes comprehensive unit tests for the backend module to ensure its functionality and correctness.

The final output is a directory containing the design document, the backend module, the Gradio UI, and the unit tests—a complete and runnable application package.

🤖 **The AI Team**
Our autonomous team consists of four expert agents:

1. **Engineering Lead**
Role: Directs the engineering team's work.

Goal: Translate high-level requirements into a detailed, actionable design for the backend developer. The design specifies a single, self-contained Python module.

Backstory: A seasoned engineering lead with a knack for writing clear and concise technical designs.

2. **Backend Engineer**
Role: A Python Engineer who can write code based on a technical design.

Goal: Write a Python module that perfectly implements the design provided by the Engineering Lead. The final module must be self-contained and ready for testing or UI integration.

Backstory: A seasoned Python engineer who writes clean, efficient code and follows design instructions carefully.

3. **Frontend Engineer**
Role: A Gradio expert who can create simple frontends to demonstrate a backend.

Goal: Write a Gradio UI (app.py) that demonstrates the backend module. The UI should be simple and functional for a single user.

Backstory: A highly skilled Python engineer specializing in building quick and effective Gradio UIs for backend classes.

4. **Test Engineer**
Role: A Python developer who can write effective unit tests.

Goal: Write a full suite of unit tests for the backend module, ensuring code quality and functionality.

Backstory: A seasoned QA engineer and software developer who writes excellent, thorough unit tests for Python code.

🛠️ **Tech Stack**
Framework: crewAI for creating and managing the agentic team.

LLM: OpenAI GPT-4o (or any other compatible model).

UI: Gradio for rapid web UI development.

Language: Python

🏁 **Getting Started**
**Prerequisites**
Python 3.10+

An OpenAI API Key (or an API key for your preferred LLM provider).

1. Clone the Repository
git clone [https://github.com/your-username/agent-powered-development.git](https://github.com/your-username/agent-powered-development.git)
cd agent-powered-development

2. Install Dependencies
pip install -r requirements.txt

(You will need to create a requirements.txt file containing crewai, crewai-tools, openai, gradio, and python-dotenv)

3. Configure Your Environment
Create a .env file in the root of the project and add your API key:

OPENAI_API_KEY="your-api-key-here"

4. Run the Crew
Modify the main.py file to include your project requirements and then run it.

Example main.py:

from crewai import Crew, Process
from agents import dev_team # Assuming you define agents in agents.py
from tasks import dev_tasks # Assuming you define tasks in tasks.py

# --- Define Your Project Requirements ---
# This is where you describe what you want the crew to build.
inputs = {
    "requirements": "Create a simple calculator class that can add, subtract, multiply, and divide two numbers.",
    "module_name": "calculator.py",
    "class_name": "Calculator"
}

# --- Instantiate Agents and Tasks ---
agents = dev_team()
tasks = dev_tasks()

# --- Create and Run the Crew ---
# Instantiate your crew with a sequential process
project_crew = Crew(
    agents=[agents.engineering_lead, agents.backend_engineer, agents.frontend_engineer, agents.test_engineer],
    tasks=[tasks.design_task, tasks.code_task, tasks.frontend_task, tasks.test_task],
    process=Process.sequential,
    verbose=2,
)

# Kick off the crew's work
result = project_crew.kickoff(inputs=inputs)

print("\n\n########################")
print("## Crew Work Complete!")
print("########################\n")
print("Final result:")
print(result)


5. Review the Output
After the crew finishes its work, you will find the generated files in the output/ directory:

output/
├── calculator.py_design.md
├── calculator.py
├── app.py
└── test_calculator.py
