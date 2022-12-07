

def format_to_json(author_GUID, author_name, reviewer_GUID, reviewer_name, question, options, hint, correct_answer, option_count):
    '''
        This function formatts the data into JSON dictionary
        List Of Parameters
        author_GUID, - String
        author_name, - String
        reviewer_GUID, - String
        reviewer_name, - String
        question, - LaTex Formatted String
        options, - LaTex Formatted String list
        hint, - String
        correct_answer, LaTex Formatted String
        option_count - Integer
    '''
    data = {};
    data={"content" : question, "answer":[], "hint": hint, "credits": {
    "author": { "id": author_GUID, "name": author_name},
    "reviewer": { "id": reviewer_GUID, "name": reviewer_name}
    }};

    for i in range(option_count):
        answer_dict = {}
        answer_dict["id"] = i+1;
        answer_dict["value"] = (options[i]);
        if(options[i] == correct_answer):
            answer_dict["is_key"] = True
        data["answer"].append(answer_dict)  

    return data 

