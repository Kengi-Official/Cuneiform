"""
Cuneiform vs. Natural Language A/B Test
English Version
"""

import anthropic
import os
import random
import time
import json
from dotenv import load_dotenv
import pandas as pd

# Load environment
load_dotenv()
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Results storage
results = []

# Test cases definition
test_cases = [
    {
        "task": "meeting_email",
        "prompt_natural": """Write a polite business email to Team Leader Kim requesting a project review meeting this week. Use a formal yet friendly tone, suggest 2-3 available time slots, and mention that you're waiting for a response.""",
        "prompt_cuneiform": """Task: Meeting_Request_Email
Purpose: Request a project review meeting with team leader
Input:
  Recipient = "Team Leader Kim"
  Tone = "Formal + Friendly"
  Time_Options = ["Tuesday 2 PM", "Wednesday 11 AM", "Thursday 4 PM"]
  Response_Deadline = "Within 3 days"
Output: "Business Email"
"""
    },
    {
        "task": "tech_summary",
        "prompt_natural": """Summarize the following technical document in 3 sentences. Include important technical terms and numbers. Focus on facts only, without emotional expressions.""",
        "prompt_cuneiform": """Task: Technical_Document_Summary
Purpose: Summarize long document into 3 sentences
Input:
  Document = "Tech_Forum_2025_10.txt"
  Output_Format = "3 sentences, include technical terms, fact-based"
  Exclude = "Emotional expressions, promotional language"
Output: "Core Summary"
"""
    },
    {
        "task": "creative_poem",
        "prompt_natural": """Write a 4-line short poem about autumn. Use metaphors and create a melancholic yet beautiful atmosphere. Reflect a contemplative mood.""",
        "prompt_cuneiform": """Task: Seasonal_Poem_Creation
Purpose: Create an emotional poem
Input:
  Season = "Autumn"
  Lines = 4
  Mood = "Melancholic + Beautiful"
  Technique = "Metaphor"
  Style = "Contemplative"
Output: "Poem"
"""
    }
]

def call_claude(prompt, is_cuneiform=False):
    """Call Claude API"""
    messages = [{"role": "user", "content": prompt}]
    
    try:
        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=500,
            temperature=0.7,
            messages=messages
        )
        return response.content[0].text
    except Exception as e:
        return f"Error: {e}"

# Run experiment
print("🔬 A/B Test Starting (30 executions)")
print("=" * 60)

for case in test_cases:
    print(f"\n📂 Test Case: {case['task']}")
    
    # 5 iterations
    for i in range(5):
        # Execute both methods in random order (prevent order bias)
        order = random.choice([("A", "B"), ("B", "A")])
        
        for version in order:
            if version == "A":
                prompt = case["prompt_natural"]
                method = "natural"
                label = "A"
            else:
                prompt = case["prompt_cuneiform"]
                method = "cuneiform"
                label = "B"
            
            print(f"  Executing: {label} ({method}) - Trial {i+1}")
            output = call_claude(prompt, method=="cuneiform")
            
            # Save result
            results.append({
                "task": case["task"],
                "method": method,
                "prompt": prompt,
                "output": output,
                "trial": i+1,
                "execution_order": label
            })
            
            # Prevent API overload
            time.sleep(1)

# Save results
df = pd.DataFrame(results)
df.to_csv("experiment_results.csv", index=False, encoding='utf-8-sig')
df.to_excel("experiment_results.xlsx", index=False)

print("\n✅ All experiments completed!")
print("📊 Results saved to 'experiment_results.csv' and 'experiment_results.xlsx'")
print(f"\n📈 Summary:")
print(f"  Total API Calls: {len(results)}")
print(f"  Natural Language: {len([r for r in results if r['method'] == 'natural'])}")
print(f"  Cuneiform: {len([r for r in results if r['method'] == 'cuneiform'])}")
