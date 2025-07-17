import streamlit as st 
import streamlit.components.v1 as components
import decimal
from itertools import permutations

st.set_page_config(page_title="Midterm", layout="centered")
st.title("Midterm")

st.header("Student Information")
class_options = ["1/11", "1/12"]
selected_class = st.selectbox("Select your class:", class_options)
nickname = st.text_input("Nickname")
student_number = st.text_input("Student Number")

answers = st.secrets["answers"]

# ==== Part I: Sudoku Puzzle (3pts) ====
st.header("Part I: Sudoku Puzzle (4pts)")
st.write("**Instruction:** Solve the 6x6 Sudoku puzzle using the numbers 1 to 6.")

puzzle = st.secrets["sudoku"]["puzzle"]
solution = st.secrets["sudoku"]["solution"]

sudoku = components.declare_component("sudoku", path="sudoku_component")
# Call the sudoku component passing the puzzle as default
board = sudoku(default=puzzle)
# st.write(board)

# ==== Part II: Counting Combinations I (3pts) ====
st.header("Part II: Counting Combinations I (3pts)")
st.write("**Instruction:** Given the colors below, make the possible combinations and answer the following questions. Then circle the correct answer to the question below.")
st.image("rby.png")
# Question 2 - Placeholder
st.write("**2. Color the following tower of blocks of the possible combinations you can make based on the statement above.**")

colors = ["", "Red", "Blue", "Yellow"]
tower_inputs = {}

# Display 6 towers side by side
cols = st.columns(6)
for i, col in enumerate(cols):
    with col:
        st.markdown(f"**Tower {i+1}**")
        tower_inputs[i] = []
        for block in range(3):
            block_color = st.selectbox(f"Select", colors, key=f"tower{i}_block{block}")
            tower_inputs[i].append(block_color)

# Questions 3–7
questions_3_7 = {
    3: ("How many three block towers can you make out of them?", 
        ["a. 5", "b. 6", "c. 8", "d. 12"], 
        answers["q3"]),
    4: ("If there is a restriction that you cannot put the red block at the top, how many towers can you make?", 
        ["a. 2", "b. 4", "c. 6", "d. 8"], 
        answers["q4"]),
    5: ("If there is a restriction that you cannot put the red block and blue block at the top, how many towers can you make?", 
        ["a. 2", "b. 4", "c. 6", "d. 8"], 
        answers["q5"]),
    6: ("If there is a restriction that you cannot put the yellow block at the bottom, how many towers can you make?", 
        ["a. 2", "b. 4", "c. 6", "d. 8"], 
        answers["q6"]),
    7: ("If there is a restriction that you cannot put the blue or yellow in the middle, how many towers can you make?", 
        ["a. 2", "b. 4", "c. 6", "d. 8"], 
        answers["q7"]),
}

for qnum in questions_3_7:
    q, opts, _ = questions_3_7[qnum]
    st.radio(f"**{qnum}. {q}**", options=opts, key=f"q{qnum}")

st.header("Part III: Counting Combinations II (10pts)")
st.write("Suppose that the five-character code has the following restrictions. Select the correct answers to the questions below.")
st.markdown("""
- Numbers and letters  
- Uppercase and lowercase letters  
""")
st.image("5ch.png")

questions_8_12 = {
    8: ("What characters can make up the code?", 
        ["a. 10 numbers", "b. 26 letters", "c. 10 numbers and 26 letters", "d. 10 numbers and 52 letters"], 
        answers["q8"]),
    9: ("What sets of characters can the code contain?", 
        ["a. a-z (lowercase letters)", "b. 0-9 (numbers)", "c. A-Z (uppercase letters)", "d. All of the above"], 
        answers["q9"]),
    10: ("How many possible characters are there for the first spot in the password?", 
         ["a. 60 possible letters and numbers", "b. 62 possible letters and numbers", "c. 61 possible letters and numbers", "d. 59 possible letters and numbers"], 
         answers["q10"]),
    11: ("How many possible characters are there for the fifth spot in the password?", 
         ["a. 60 possible letters and numbers", "b. 62 possible letters and numbers", "c. 61 possible letters and numbers", "d. 59 possible letters and numbers"], 
         answers["q11"]),
    12: ("How many total password combinations are possible?", 
         ["a. 44,261,653,680 possible combinations", 
          "b. 916,132,832 possible combinations", 
          "c. 776,520,240 possible combinations", 
          "d. 13,388,280 possible combinations"], 
         answers["q12"]),
}

for qnum in questions_8_12:
    q, opts, _ = questions_8_12[qnum]
    st.radio(f"**{qnum}. {q}**", options=opts, key=f"q{qnum}")

st.markdown("""
**Suppose that the five-character code has the following restrictions. Select the correct answers to the questions below.**  
- Numbers  
- Cannot repeat characters  
""")
st.image("5ch.png")

questions_13_17 = {
    13: ("What characters can make up the code?", 
         ["a. 10 numbers", "b. 26 letters", "c. 10 numbers and 26 letters", "d. 10 numbers and 52 letters"], 
         answers["q13"]),
    14: ("What sets of characters can the code contain?", 
         ["a. a-z (lowercase letters)", "b. 0-9 (numbers)", "c. A-Z (uppercase letters)", "d. All of the above"], 
         answers["q14"]),
    15: ("How many possible characters are there for the first spot in the password?", 
         ["a. 52 possible letters and numbers", "b. 10 possible numbers", "c. 62 possible letters and numbers", "d. 9 possible numbers"], 
         answers["q15"]),
    16: ("How many possible characters are there for the fifth spot in the password?", 
         ["a. 52 possible letters and numbers", "b. 10 possible numbers", "c. 62 possible letters and numbers", "d. 6 possible numbers"], 
         answers["q16"]),
    17: ("How many total password combinations are possible?", 
         ["a. 44,261,653,680 possible combinations", 
          "b. 380,204,032 possible combinations", 
          "c. 100,000 possible combinations", 
          "d. 30,240 possible combinations"], 
         answers["q17"]),
}

for qnum in questions_13_17:
    q, opts, _ = questions_13_17[qnum]
    st.radio(f"**{qnum}. {q}**", options=opts, key=f"q{qnum}")

# ==== Part IV: Problem Solving - Finding the LCM (3pts) ====
st.header("Part III: Problem Solving - Finding the LCM (3pts)")

lcm_questions = {
    18: "Find the Least Common Multiple of 5, 7 using the listing method.",
}
for qnum, qtext in lcm_questions.items():
    st.text_input(f"**{qnum}. {qtext}**", key=f"lcm{qnum}")

tree = components.declare_component("tree", path="tree_component")
st.write("**19 - 20. Find the Prime Factors of the following numbers.**")
tree_result = tree(key="factor_tree")
# Optional debug:
# st.write("Tree result:", tree_result)

# ==== Grading Functions ====
def grade_sudoku(user_board, puzzle, solution):
    total = correct = 0
    if not user_board:
        return 0
    for i in range(6):
        for j in range(6):
            if puzzle[i][j] == 0:
                total += 1
                if user_board[i][j] == solution[i][j]:
                    correct += 1
    return round(correct / total * 4, 2) if total else 0

def grade_blocks():
    correct = 0
    total_mcq = 5  # questions 3–7

    # Grading Q3–Q7 (0.5 pts each)
    for qnum, (_, _, corr) in questions_3_7.items():
        ans = st.session_state.get(f"q{qnum}", "")
        if ans and ans[0].lower() == corr:
            correct += 0.5

    # Grading Q2 (tower permutations)
    valid_towers = list(permutations(['Red', 'Blue', 'Yellow']))
    student_towers = []

    for i in range(6):
        t = [
            st.session_state.get(f"tower{i}_block0", ""),
            st.session_state.get(f"tower{i}_block1", ""),
            st.session_state.get(f"tower{i}_block2", "")
        ]
        if all(c in ("Red", "Blue", "Yellow") for c in t) and len(set(t)) == 3:
            student_towers.append(tuple(t))

    # Count unique valid permutations
    unique_valid = set(student_towers) & set(valid_towers)
    if len(unique_valid) == 6:
        correct += 0.5  # Full credit for Q2

    return round(correct, 2)

def grade_count():
    correct = 0
    total = 0
    for group in (questions_8_12, questions_13_17):
        for qnum, (_, _, corr) in group.items():
            ans = st.session_state.get(f"q{qnum}", "")
            if ans and ans[0].lower() == corr:
                correct += 1
            total += 1
    return round(correct / total * 10, 2)

def grade_trees(tree_result):
    score = 0
    if not tree_result:
        tree_result = {}
        
    # Tree 1
    t1_node1 = tree_result.get("tree1", {}).get("node1", "").strip()
    t1_leaf1 = tree_result.get("tree1", {}).get("leaf1", "").strip()
    t1_leaf2 = tree_result.get("tree1", {}).get("leaf2", "").strip()

    if t1_node1 == answers["t1_node1"] and sorted([t1_leaf1, t1_leaf2]) == answers["t1_leaves"]:
        score += 1

    # Tree 2
    t2_node1 = tree_result.get("tree2", {}).get("node1", "").strip()
    t2_leaf1_left = tree_result.get("tree2", {}).get("leaf1_left", "").strip()
    t2_leaf2_left = tree_result.get("tree2", {}).get("leaf2_left", "").strip()
    t2_leaf1 = tree_result.get("tree2", {}).get("leaf1", "").strip()
    t2_leaf2 = tree_result.get("tree2", {}).get("leaf2", "").strip()

    left_correct = sorted([t2_leaf1_left, t2_leaf2_left]) == answers["t2_leaves_left"]
    right_correct = (t2_node1 == answers["t2_node1"] and sorted([t2_leaf1, t2_leaf2]) == answers["t2_leaves"])

    if left_correct and right_correct:
        score += 1

    return score

def grade_lcm(tree_result, lcm_answer):
    score = 0

    # 1 point for LCM question 18
    correct_lcm_answer = answers["lcm"]
    if lcm_answer.strip() == correct_lcm_answer:
        score += 1

    # Add factor tree score
    score += grade_trees(tree_result)

    return score

# if st.button("Grade Test"):
#    lcm_answer = st.session_state.get("lcm18", "")
#    if not tree_result:
#        tree_result = {}
        
#    s1 = grade_sudoku(board, puzzle, solution)
#    s2 = grade_blocks()
#    s3 = grade_count()
#    s4 = grade_lcm(tree_result, lcm_answer)

#    total = s1 + s2 + s3 + s4
#    st.success(f"Scores → Part I: {s1}/4 · Part II: {s2}/3 · Part III: {s3}/10 · Part IV: {s4}/3 · **Total: {total:.2f}/20**")

decimal.getcontext().rounding = decimal.ROUND_HALF_UP

if st.button("Submit Test"):
    if not nickname or not student_number:
        st.error("Please fill in your nickname and student number.")
    else:
        # Grade parts
        s1 = grade_sudoku(board, puzzle, solution)
        s2 = grade_blocks()
        s3 = grade_count()
        lcm_answer = st.session_state.get("lcm18", "")
        s4 = grade_lcm(tree_result, lcm_answer)
        total = s1 + s2 + s3 + s4

        # Build submission record
        submission = {
            "nickname": nickname,
            "student_number": student_number,
            "scores": {
                "part1_sudoku": s1,
                "part2_blocks": s2,
                "part3_count": s3,
                "part4_lcm": s4,
                "total": total
            },
            "answers": {
                "sudoku": board,

                # Part II: Blocks answers (Q2 to Q7 and tower inputs)
                "blocks": {
                    # Tower inputs (6 towers × 3 blocks)
                    "towers": {
                        f"tower{i}": [
                            st.session_state.get(f"tower{i}_block0", ""),
                            st.session_state.get(f"tower{i}_block1", ""),
                            st.session_state.get(f"tower{i}_block2", "")
                        ]
                        for i in range(6)
                    },
                    # Q3 to Q7 multiple choice answers
                    **{f"q{q}": st.session_state.get(f"q{q}", "") for q in range(3, 8)}
                },

                # Part III: Counting Combinations (Q8 to Q17)
                "count": {
                    # Q8 to Q12 (first group)
                    **{f"q{q}": st.session_state.get(f"q{q}", "") for q in range(8, 13)},
                    # Q13 to Q17 (second group)
                    **{f"q{q}": st.session_state.get(f"q{q}", "") for q in range(13, 18)},
                },

                # Part IV: LCM and factor trees (Q18, 19, 20)
                "lcm": {
                    "lcm_answer": st.session_state.get("lcm18", ""),
                    "factor_trees": tree_result if tree_result else {},
                }
            }
                    }

        
        # Save to file
        import json, os
        os.makedirs("submissions", exist_ok=True)
        #file_path = f"submissions/{student_number}.json"
        #with open(file_path, "w") as f:
        #    json.dump(submission, f, indent=2)

        # st.markdown("### 📄 Submission Preview")
        # st.json(submission)

        import gspread
        from google.oauth2.service_account import Credentials

        # Set up creds and open your sheet
        scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        
        # Load credentials from Streamlit secrets
        service_account_info = st.secrets["gcp_service_account"]
        creds = Credentials.from_service_account_info(service_account_info, scopes=scopes)
        
        client = gspread.authorize(creds)
        import datetime
        
        # Timestamp for filenames and sheets
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename_ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        # Define your folder mapping for Drive
        DRIVE_FOLDERS = {
            "1/11": "1NY3CXwbEhd3KVvZNTxwu5qjrTmVEt_5a",
            "1/12": "1lfQOav8SeRCvVJnxfeBrLQjX4PA6rnyF"
        }
        folder_id = DRIVE_FOLDERS.get(selected_class)

        # from fpdf import FPDF

        def create_submission_pdf(data, path):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=10)
            pdf.multi_cell(0, 8, txt=json.dumps(data, indent=2))
            pdf.output(path)
        pdf_path = f'submissions/{selected_class.replace("/", "-")}_{nickname}_{student_number}_{filename_ts}.pdf'
        # create_submission_pdf(submission, pdf_path)

        json_path = f'{selected_class.replace("/", "-")}_{nickname}_{student_number}_{filename_ts}.json'
        with open(json_path, "w") as f:
            json.dump(submission, f, indent=2)
            
        # from googleapiclient.discovery import build
        # from googleapiclient.http import MediaFileUpload

        # from googleapiclient.errors import HttpError

        def upload_to_drive(file_path, filename, folder_id, creds):
            try:
                if not os.path.exists(file_path):
                    st.error(f"File not found: {file_path}")
                    return None

                service = build("drive", "v3", credentials=creds)
                metadata = {"name": filename}
                if folder_id:
                    metadata["parents"] = [folder_id]

                media = MediaFileUpload(file_path, resumable=False)
                uploaded = service.files().create(
                    body=metadata, media_body=media, fields="id"
                ).execute()

                st.success(f"Uploaded to Drive: {filename}")
                return uploaded.get("id")

            except HttpError as error:
                st.error("❌ Google Drive upload failed.")
                st.write(f"Error: {error}")
                st.write(f"File: {file_path}")
                st.write(f"Folder ID: {folder_id}")
                raise
        # upload_to_drive(json_path, os.path.basename(json_path), folder_id, creds)
        # upload_to_drive(pdf_path, os.path.basename(pdf_path), folder_id, creds)

        try:
            sheet = client.open("Midterm").worksheet(selected_class)
        except gspread.WorksheetNotFound:
            st.error(f"Worksheet '{selected_class}' not found. Please check your Google Sheet.")

        # Convert your submission dict into a list of values (flatten if needed)
        row = [
            submission["student_number"],
            submission["nickname"],
            submission["scores"]["part1_sudoku"],
            submission["scores"]["part2_blocks"],
            submission["scores"]["part3_count"],
            submission["scores"]["part4_lcm"],
            submission["scores"]["total"],
            timestamp
            # add other fields or stringify answers if needed
        ]

        sheet.append_row(row)
        # st.success("Submission sent to Google Sheets! ✅")
        st.success(f"Submission received! ✅ Total Score: {round(total)}/20")
        
        with open(json_path, "rb") as f:
            st.download_button(
            "Download answers",
                data=f,
                file_name=os.path.basename(json_path),
                mime="application/json"
            )
