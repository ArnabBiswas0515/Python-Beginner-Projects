from question import Question

questions_1 = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": 3,
        "prize" : 1000
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": 2,
        "prize" : 4000
    },
    {
        "question": "Who developed the theory of relativity?",
        "options": ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Galileo Galilei"],
        "answer": 2,
        "prize" : 8000
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Indian Ocean", "Atlantic Ocean", "Pacific Ocean", "Arctic Ocean"],
        "answer": 3,
        "prize" : 10000
    },
    {
        "question": "Which data structure uses FIFO (First In First Out)?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": 2,
        "prize" : 40000
    },
    {
        "question": "In Python, which keyword is used to define a function?",
        "options": ["func", "define", "def", "function"],
        "answer": 3,
        "prize" : 80000
    },
    {
        "question": "What is the chemical symbol for Gold?",
        "options": ["Au", "Ag", "Gd", "Go"],
        "answer": 1,
        "prize" : 100000
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["William Wordsworth", "Charles Dickens", "William Shakespeare", "Jane Austen"],
        "answer": 3,
        "prize" : 250000
    },
    {
        "question": "Which country hosted the 2016 Summer Olympics?",
        "options": ["China", "Brazil", "UK", "Russia"],
        "answer": 2,
        "prize" : 500000
    },
    {
        "question": "What does HTTP stand for?",
        "options": [
            "HyperText Transfer Protocol",
            "HighText Transfer Protocol",
            "Hyper Transfer Text Program",
            "Hyper Tool Transfer Protocol"
        ],
        "answer": 1,
        "prize" : 1000000
    }
]

questions = [
    Question(
        q["question"],
        q["options"],
        q["answer"],
        q["prize"]
    )
    for q in questions_1
]