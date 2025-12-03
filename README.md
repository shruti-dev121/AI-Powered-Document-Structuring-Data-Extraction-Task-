🚀 Project Goal

#video of this demo link on drive-https://drive.google.com/file/d/1Mk18SSAKuMSyvTTnZHE1FIrmhsj0-EHY/view?usp=sharing

Extract all useful information from Data Input.pdf
Let Gemini auto-detect and generate keys
Add meaningful comments/context
Output everything into a structured Excel:
Key | Value | Comments
Produce consistent results for messy or complex PDFs

.
├── process_pdf.py            # Main script (Gemini API integration)
├── Data Input.pdf            # Input file (not included in repo if confidential)
├── Final_Output.xlsx         # Auto-generated Excel file
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

🛠️ Tech Stack

Python 3.12+
Google Gemini API (genai library)
pdfplumber (PDF text extraction)
pandas (Excel creation)


🔧 Setup Instructions
1. Clone the Repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

2. Install Dependencies
pip install -r requirements.txt

3. Configure Gemini API

In process_pdf.py, replace:
client = genai.Client(api_key="YOUR_GEMINI_API_KEY")


4. Run the Script
python process_pdf.py

5. Output

The extracted structured Excel file will be created as:

Final_Output.xlsx


features Completed============

1]Accurate PDF text extraction
2]Dynamic key generation using Gemini
3]JSON-formatted structured output
4]Excel export
5]Error handling

📌 Use Cases

Resume structuring
Company profiling
Document intelligence tasks
Automated data extraction
PDF → Excel transformation
