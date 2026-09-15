# 🎓 Stanford Code in Place

> My programming journey through **Stanford Code in Place** — learning Python, problem solving, and computational thinking through hands-on assignments.

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1200&color=6C63FF&center=true&vCenter=true&width=650&lines=🌸+Creating+your+haiku...;✍️+5+%E2%80%93+7+%E2%80%93+5+syllables;🤖+Powered+by+AI;✨+Python+%2B+Creativity+%2B+AI" alt="Typing Animation" />

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Stanford](https://img.shields.io/badge/Stanford-Code%20in%20Place-8C1515?style=for-the-badge&logo=stanford&logoColor=white)
![AI](https://img.shields.io/badge/AI-Powered-6C63FF?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-2EA44F?style=for-the-badge)

</div>

---

## 📚 Coursework

### 04 · Haiku

A creative Python assignment that uses **AI to generate a personalized haiku** based on the user's name and chosen topic.

<div align="center">

🌸 **Enter Your Name**  
↓  
💡 **Choose a Topic**  
↓  
📝 **Build an AI Prompt**  
↓  
🤖 **Generate Haiku**  
↓  
✨ **Display 5–7–5 Poem**

</div>

---

## 🎯 Task

Create a Python program that asks the user for:

- 👤 Their name
- 💡 A topic

Then use AI to generate a haiku that:

- Contains the user's name
- Is about the chosen topic
- Has exactly **three lines**
- Follows the traditional **5–7–5 syllable structure**
- Returns only the three lines of the haiku

---

## 🧠 How It Works


                 ┌───────────────────┐
                 │    👤 User        │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │   Enter Name      │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │   Enter Topic     │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │   📝 AI Prompt    │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │    🤖 AI Model    │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │    🌸 Haiku       │
                 │      5–7–5        │
                 └───────────────────┘
💻 Program Flow
The program first collects the user's name and topic.
name = input("Enter your name: ")
topic = input("Enter a topic: ")

print("Creating your haiku...")
It then creates a prompt containing the user's information and sends it to the AI model.
haiku = call_gpt(prompt)
Finally, the generated haiku is displayed:
print(haiku)
🌸 Example
Input
Enter your name: Rahul
Enter a topic: Sunrise
Program
Creating your haiku...
Output
Morning light finds Rahul
Golden skies awaken dreams
New journeys begin
📝 The 5–7–5 Structure
A key requirement of the assignment is the traditional three-line haiku structure:
🌸 Line 1 → 5 syllables

🌿 Line 2 → 7 syllables

🌸 Line 3 → 5 syllables
Visual representation:
        🌸 HAIKU 🌸

       ┌─────────────┐
       │   5         │
       │  syllables  │
       └──────┬──────┘
              ↓
       ┌─────────────┐
       │     7       │
       │  syllables  │
       └──────┬──────┘
              ↓
       ┌─────────────┐
       │     5       │
       │  syllables  │
       └─────────────┘
🤖 AI Prompt
The program dynamically creates an AI prompt using the user's inputs.
The prompt instructs the model to:
Write a haiku about {topic} that includes the name {name}.

The haiku must have exactly three lines:

- The first line must have 5 syllables.
- The second line must have 7 syllables.
- The third line must have 5 syllables.

Return only the three lines of the haiku.
This allows the same Python program to create different haikus depending on the user's input.
🔄 Dynamic Generation
        👤 USER
          │
          │
     "Rahul"
          │
          ▼
     ┌─────────┐
     │  NAME   │
     └────┬────┘
          │
          │
     "Sunrise"
          │
          ▼
     ┌─────────┐
     │  TOPIC  │
     └────┬────┘
          │
          ▼
   ┌───────────────┐
   │  AI PROMPT    │
   └───────┬───────┘
           │
           ▼
      ┌─────────┐
      │   🤖    │
      │   AI    │
      └────┬────┘
           │
           ▼
     ┌───────────┐
     │  🌸 5–7–5 │
     │   HAIKU   │
     └───────────┘

🧩 Concepts
<div align="center">
Concept	Used For
🐍 Python	Programming language
⌨️ input()	Collecting user information
📦 Variables	Storing name and topic
⚙️ Functions	Structuring the program
🤖 AI	Generating the haiku
📝 Prompting	Giving instructions to AI
🔤 f-Strings	Creating the dynamic prompt
🖥️ Console I/O	User interaction
</div>

🏗️ Project Structure
Stanford-Code-in-Place-Assignment-4/
│
├── 📄 main.py
├── 📄 README.md
└── 📄 ...
main.py
Contains the Python implementation for generating the AI-powered haiku.
README.md
Contains the project documentation, explanation, examples, and learning notes.

🌟 What I Learned
1. 🐍 Python User Input
The program uses input() to collect information directly from the user.
2. 📝 Dynamic Prompts
User-provided information can be inserted into an AI prompt to produce personalized results.
3. 🤖 AI-Assisted Programming
Python can interact with an AI model to generate creative content dynamically.
4. 🌸 Structured Generation
AI can be guided to produce output following specific structural constraints such as 5–7–5 syllables.
5. 💡 Combining Code & Creativity
This assignment demonstrates how programming can be used not only for calculations and logic, but also for creative applications.

🎨 From Input to Creativity
Python
   │
   ▼
User Input
   │
   ▼
Prompt Engineering
   │
   ▼
AI Generation
   │
   ▼
Structured Output
   │
   ▼
🌸 Haiku

🗺️ Progress
Assignment	Status
Programming is Awesome	✅
Sunrise Message	✅
AI Crystal Ball	✅
Haiku	✅
More assignments coming	🔜
<div align="center">

  💻 Learning by Building
Learn → Practice → Solve → Build → Repeat
<br>
🐍   📝   🤖   🌸   🚀
<br>
"Code can be logical, creative, and expressive."
<br>

🎓 Stanford Code in Place
Python · Problem Solving · Computational Thinking · AI
<br>

⭐ One assignment at a time.
</div>
<p align="center"> <sub>Personal coursework repository · Stanford Code in Place</sub> </p>
