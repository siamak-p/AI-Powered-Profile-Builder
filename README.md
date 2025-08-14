# AI-Powered Profile Builder

An interactive, command-line profile builder that uses an AI assistant to create professional profiles for users.  
It also features an employer mode for viewing and searching these profiles.  
The application is built in **Python** and leverages the **OpenAI API** for its conversational AI capabilities.

---

## Features

- **Interactive Profile Creation**: An AI assistant asks users a series of questions to gather information for their professional profile.
- **Dynamic Conversation**: The AI determines when it has collected enough information to complete the profile.
- **Structured JSON Output**: Profiles are saved in a clean, organized JSON format.
- **Employer Portal**: A separate interface for employers to:
  - List all created profiles
  - View the detailed content of any profile
  - Search for profiles based on specific skills
- **Dual Language Support**: The interface supports both Persian and English numbers for menu selections.

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd <your-repository-name>
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install openai==1.99.9
   ```

4. **Set up your environment variables**:
   - Create a file named `.env` in the root directory of the project.
   - Add your OpenAI API key to it:
     ```env
     OPENAI_API_KEY='your_openai_api_key'
     ```

---

## Usage

To start the application, run:

```bash
python main.py
```

You will be presented with the main menu where you can choose between **Employee Mode** and **Employer Mode**.

### Employee Mode
1. Enter your full name to begin.
2. The AI will ask questions about your professional background, work experience, and skills.
3. Answer each question to the best of your ability.
4. Once enough information is collected, the profile will be saved as a JSON file (e.g., `Your_Name.json`) in the `profiles/` directory.

### Employer Mode
You can manage and search through created profiles with the following options:

1. **List Profiles** – Displays filenames of all available profiles.
2. **View a Profile** – Enter a profile name to see its full content.
3. **Search by Skill** – Enter a skill (e.g., `python`, `project management`) to find profiles that include it.
4. **Return to Main Menu** – Exit employer mode and go back to the main menu.

---

## License
This project is licensed under the [MIT License](LICENSE).
