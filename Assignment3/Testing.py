from Assignment_3 import HINTS, app, load_score_histories, record_quiz_score

'''
This function was created with copilot under the prompt:
"create a function that tests if the sessions accurately track user information"
'''
def test_sessions_track_different_users():
    alice_client = app.test_client()
    bob_client = app.test_client()

    alice_client.post("/", data={"name": "Alice"})
    bob_client.post("/", data={"name": "Bob"})

    with alice_client.session_transaction() as alice_session:
        assert alice_session["name"] == "Alice"
        assert alice_session["name"] != "Bob"

    with bob_client.session_transaction() as bob_session:
        assert bob_session["name"] == "Bob"
        assert bob_session["name"] != "Alice"

'''
This function was created with copilot under the prompt:
"create a function that checks if the answer to each quiz question is correct"'''
def test_each_quiz_answer_is_marked_correct():
    client = app.test_client()
    client.post("/", data={"name": "Quiz Tester"})
    client.get("/quiz")

    for question_number in range(5):
        with client.session_transaction() as quiz_session:
            question = quiz_session["quiz_questions"][question_number]
            correct_answer = question[1][0]

        client.post("/quiz", data={"answer": correct_answer})

    with client.session_transaction() as quiz_session:
        answers = quiz_session["quiz_answers"]

    assert len(answers) == 5
    assert all(answer["is_correct"] for answer in answers)


'''
This function was created with copilot under the prompt:
"create a function that tests if users are prevented from submitting without
first selecting an answer"
'''
def test_users_must_select_an_answer():
    client = app.test_client()
    client.post("/", data={"name": "Quiz Tester"})
    client.get("/quiz")

    response = client.post("/quiz", data={})
    page = response.data.decode()

    assert response.status_code == 200
    assert "***Please select an answer before submitting." in page

    with client.session_transaction() as quiz_session:
        assert quiz_session["question_number"] == 0
        assert quiz_session["quiz_answers"] == []


'''
This function was created with copilot under the prompt:
"create a function that looks at if the hint feature is displaying the correct
hint and if users are only allowed to use it once per quiz"
'''
def test_hint_is_correct_and_only_used_once():
    client = app.test_client()

    with client.session_transaction() as quiz_session:
        quiz_session["name"] = "Hint Tester"

    client.get("/quiz")

    with client.session_transaction() as quiz_session:
        question = quiz_session["quiz_questions"][0][0]
        correct_answer = quiz_session["quiz_questions"][0][1][0]

    expected_hint = HINTS[question]

    first_hint_response = client.post(
        "/quiz",
        data={"hint": "request"}
    )
    first_hint_page = first_hint_response.data.decode()

    assert expected_hint in first_hint_page

    client.post("/quiz", data={"answer": correct_answer})

    with client.session_transaction() as quiz_session:
        next_question = quiz_session["quiz_questions"][1][0]
        assert quiz_session["hint_used"] is True
        assert quiz_session["hint_question"] is None

    second_hint_response = client.post(
        "/quiz",
        data={"hint": "request"}
    )
    second_hint_page = second_hint_response.data.decode()

    assert HINTS[next_question] not in second_hint_page


'''
This function was created with copilot under the prompt:
"create a function that tests if user scores are stored to the correct user
and in the right order"
'''
def test_scores_are_stored_for_correct_user_in_order():
    original_scores = load_score_histories()

    try:
        for name, score in [
            ("Score Order Alice", 2),
            ("Score Order Bob", 4),
            ("Score Order Alice", 5)
        ]:
            with app.test_request_context():
                from flask import session

                session["name"] = name
                session["quiz_score"] = score
                session["quiz_active"] = True
                record_quiz_score()

        saved_scores = load_score_histories()

        assert saved_scores["Score Order Alice"][-2:] == [
            {"score": 2, "num_questions": 5},
            {"score": 5, "num_questions": 5}
        ]
        assert saved_scores["Score Order Bob"][-1:] == [
            {"score": 4, "num_questions": 5}
        ]
    finally:
        from Assignment_3 import save_score_histories

        save_score_histories(original_scores)

print(test_sessions_track_different_users())
print(test_each_quiz_answer_is_marked_correct())
print(test_users_must_select_an_answer())
print(test_hint_is_correct_and_only_used_once())
print(test_scores_are_stored_for_correct_user_in_order())